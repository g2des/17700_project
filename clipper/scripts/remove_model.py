#!/usr/bin/env python
import sys
from clipper_admin import ClipperConnection, DockerContainerManager

clipper_conn = ClipperConnection(DockerContainerManager())
clipper_conn.connect()
print("CLIPPER\t\t: Connected to cluster")

try:
    app_name = str(sys.argv[1])
    model_name = str(sys.argv[2])
    assert type(app_name) == str
    assert type(model_name) == str
except Exception as e:
    print("ERROR!!"+str(e))
    print("USAGE:\n\tpython build_deploy.py  <app_name> <model_name>")

print("Unlinking Model")
try:
    clipper_conn.unlink_model_from_app(model_name=model_name, app_name=app_name)
    print(f"Unlinked model {model_name} from app {app_name}")
except Exception as e:
    print("No link to be removed")
clipper_conn.stop_all_model_containers()
print("Model Containers Stopped")
try:
    clipper_conn.delete_application(app_name)
    print("Application deleted")
except Exception as e:
    print(f"No app by name {app_name} detected")
