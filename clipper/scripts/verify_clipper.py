#!/usr/bin/env python
import requests, json, sys, re, numpy as np
# from clipper_admin import ClipperConnection, DockerContainerManager

regex = re.compile('(?<=\[)(.*?)(?=\])')
try:
    app_name = str(sys.argv[1])
    url = str(sys.argv[2])
    print("Evaluating with ",  app_name, url)
except Exception as e:
    print("ERROR!!"+str(e))
    print("USAGE:\n\tpython build_deploy.py <app_name> <url>")


# clipper_conn = ClipperConnection(DockerContainerManager())
# clipper_conn.connect()
# query_address =clipper_conn.get_query_addr()

headers = {"Content-type": "application/json"}
response = (requests.post(f"http://{url}/{app_name}/predict", headers=headers, data=json.dumps({
    "input": "[Hello world!]"})).json())
## Expected Result : {'query_id': 2, 'output': "b '[Bonjour monde !]'", 'default': False}
print(regex.findall(response['output']))

