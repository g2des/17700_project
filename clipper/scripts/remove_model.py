#!/usr/bin/env python
import sys
from clipper_admin import ClipperConnection, DockerContainerManager

clipper_conn = ClipperConnection(DockerContainerManager())
clipper_conn.connect()
print("CLIPPER\t\t: Connected to cluster")

try:
    app_name = str(sys.argv[3])
    model_name = str(sys.argv[4])
    assert type(app_name) == str
    assert type(model_name) == str
except Exception as e:
    print("ERROR!!"+str(e))
    print("USAGE:\n\tpython build_deploy.py  <app_name> <model_name>")

print("Unlinking Model")
clipper_conn.unlink_model_from_app(model_name=model_name, app_name=app_name)
clipper_conn.stop_all_model_containers()
print("Model Containers Stopped")
clipper_conn.delete_application(app_name)
print("Application deleted")
