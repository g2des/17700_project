import csv
from locust import HttpLocust, TaskSet

USER_CREDENTIALS = None
sentences = None
with open('/content/training/news-commentary-v9.fr-en.en') as file:
  sentences = file.readlines()

class LoginWithUniqueUsersSteps(TaskSet):
    email = "NOT_FOUND"
    password = "NOT_FOUND"

    def on_start(self):
            if len(USER_CREDENTIALS) > 0:
                self.requests = USER_CREDENTIALS.pop()

    @task
    def translate(self):
        sentence = sentences[self.requests.pop()]
        # code to send request to the aws server

class LoginWithUniqueUsersTest(HttpLocust):
    task_set = LoginWithUniqueUsersSteps
    host = None
    sock = None

    def __init__(self):
        super(LoginWithUniqueUsersTest, self).__init__()
        global USER_CREDENTIALS
        if (USER_CREDENTIALS == None):
            with open('credentials.csv', 'r') as f:
                reader = csv.reader(f)
                USER_CREDENTIALS = list(reader)