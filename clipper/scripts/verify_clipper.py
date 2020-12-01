#!/usr/bin/env python\
import requests, json, sys, numpy as np
from clipper_admin import ClipperConnection, DockerContainerManager

try:
    app_name = str(sys.argv[1])
    print("Evaluating with ",  app_name,)
except Exception as e:
    print("ERROR!!"+str(e))
    print("USAGE:\n\tpython build_deploy.py <app_name>")


clipper_conn = ClipperConnection(DockerContainerManager())

query_address =clipper_conn.get_query_addr()

headers = {"Content-type": "application/json"}
print(requests.post(f"http://{query_address}/{app_name}/predict", headers=headers, data=json.dumps({
    "input": "[Hello world!]"})).json())