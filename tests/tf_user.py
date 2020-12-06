import csv, logging, requests, re, numpy as np
from locust import HttpUser, TaskSet, task, constant_pacing ##ADD THIS
import json
import pyonmttok


USER_CREDENTIALS = None
sentences = None
np.random.seed(17700)

with open('./data/training/news-commentary-v9.fr-en.en') as file:
  sentences = file.readlines()
logging.info("Reading sentences completed.")

class LoginWithUniqueUsersSteps(TaskSet):


    tokenizer = pyonmttok.Tokenizer("none", sp_model_path="ende/1/assets.extra/wmtende.model")

    regex = re.compile('(?<=\[)(.*?)(?=\])')
    ## ADD THIS
    MAX_LENGTH = 10
    ## STOP
    def on_start(self):
        self.user_id = np.random.randint(len(USER_CREDENTIALS))
        self.users_requests = USER_CREDENTIALS[self.user_id]
        logging.info(f"START : Created user with id {self.user_id}. Remaining {len(USER_CREDENTIALS)} users")
        ## ADD THIS
        self.requests = []
        for i in self.users_requests:
            sentence = sentences[int(i)%len(self.users_requests)].split()
            if len(sentence) < self.MAX_LENGTH:
                continue
            else:
                self.requests.append(" ".join(sentence[:self.MAX_LENGTH]))
        ## STOP
        #   [sentences[int(i)] for i in self.users_requests]
        logging.info(f"START : Total Number of requests :  {len(self.requests)}")

    @task
    def translate(self):
        if len(self.requests) > 0:
            sentence = [self.requests.pop()]
            batch_input = [self.tokenizer.tokenize(text)[0] for text in sentence]
            request = {"inputs": {"tokens":batch_input, "length":[len(batch_input[0])]}}
            response = self.client.post("/invocations", json=request)
            logging.info(f"TASK : Sent with request ##{sentence}## with ##{response.json()}##")
            logging.warn(f"TASK : Number of requests remaining {len(self.requests)}")
        else:
            self.interrupt()

    def on_stop(self):
        logging.info("STOP : Stopping client")


class LoginWithUniqueUsersTest(HttpUser):
    tasks = {LoginWithUniqueUsersSteps}
    host = 'http://ec2-3-132-170-187.us-east-2.compute.amazonaws.com:8080'
    ## ADD THIS
    wait_time = constant_pacing(1.0)
    ## STOP
    # # sock = None
    def __init__(self, *args, **kwargs):
        super(LoginWithUniqueUsersTest, self).__init__( *args, **kwargs)
        logging.info(f"Logging onto {self.host}")
        global USER_CREDENTIALS
        if (USER_CREDENTIALS == None):
            with open('./data/users_random_sentences.csv', 'r') as f:
                reader = csv.reader(f)
                USER_CREDENTIALS = list(reader)
        logging.info("Reading sentences and user list completed")