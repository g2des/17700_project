import csv, logging, requests, re, numpy as np
from locust import HttpUser, TaskSet, task, constant_pacing ##ADD THIS
import pdb


USER_CREDENTIALS = None
sentences = None
np.random.seed(17700)

with open('./data/training/news-commentary-v9.fr-en.en') as file:
  sentences = file.readlines()
logging.info("Reading sentences completed.")

class LoginWithUniqueUsersSteps(TaskSet):
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
        print("list req ", self.users_requests)
        for i in self.users_requests:
            print("#######", len(sentences), i)
            sentence = sentences[int(i)].split()
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
            sentence = str([self.requests.pop()])
            f = open("temp.txt", "w")
            f.write(sentence)
            f.close()
            url = '/predictions/TransformerEn2Fr'
            payload = {'data': open('temp.txt', 'r')}
            files = {'file': open('temp.txt', 'r' ,encoding= 'utf-8')}
            headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
            #response = requests.put(url, files=files, data =payload)
            response = self.client.post(url , files= files, data =payload)
            #print("receiving response------->", response.text)

            ##write to file
            with open('results.txt','a') as f:
                f.write("\n")
                f.write(str(response.text))

            #response = self.client.post("/nmt/predict", json={'input' : sentence})
            logging.info(f"TASK : Sent with request {sentence} with {response.json()}")
            logging.warn(f"TASK : Number of requests remaining {len(self.requests)}")
        else:
            self.interrupt()

    def on_stop(self):
        logging.info("STOP : Stopping client")


class LoginWithUniqueUsersTest(HttpUser):
    tasks = {LoginWithUniqueUsersSteps}
    host = 'http://ec2-3-134-113-245.us-east-2.compute.amazonaws.com:8080'
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
