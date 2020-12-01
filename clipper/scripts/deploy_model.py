#!/usr/bin/env python
import cloudpickle, torch, sys
from clipper_admin import ClipperConnection, DockerContainerManager
from clipper_admin.deployers.pytorch import deploy_pytorch_model

def translate(model, inputs):
    return model.translate(inputs, beam=5)

clipper_conn = ClipperConnection(DockerContainerManager())
clipper_conn.connect()
print("CLIPPER\t\t: Connected to cluster")
try:
    is_cuda = eval(sys.argv[1])
    model_path = str(sys.argv[2])
    app_name = str(sys.argv[3])
    model_name = str(sys.argv[4])
    SLO = eval(sys.argv[5])
    assert type(is_cuda) == bool
    assert type(model_name) == str
    assert type(app_name) == str
    assert type(model_path) == str
    assert type(SLO) == int
    print("Evaluating with ", is_cuda, model_path, app_name, model_name, SLO)
except Exception as e:
    print("ERROR!!"+str(e))
    print("USAGE:\n\tpython build_deploy.py <True|False> <model_path> <app_name> <model_name> <SLO>")

# Load an En-Fr Transformer model trained on WMT'14 data :
model = cloudpickle.load(open(model_path ,'rb'))
# Use the GPU (optional):
if torch.cuda.is_available() and is_cuda:
    model.cuda()

print(model.translate(['Hello world!','This is clipper world','Wait whaat!'], beam=5))
print("RUNNING APPS:\t\t",clipper_conn.get_all_apps(),
    "RUNNING MODELS:",clipper_conn.get_all_models())
clipper_conn.register_application(name=app_name, input_type="strings", default_output="default", slo_micros=SLO)
print("REGISTERED APP\t\t",app_name,"WITH SLO",SLO)

deploy_pytorch_model(
    clipper_conn,
    name=model_name,
    version=1,
    input_type="strings",
    func=translate,
    base_image='custom-image',
    pytorch_model=model)
print("MODEL DEPLOYED")
print("RUNNING APPS:\t\t",clipper_conn.get_all_apps(),
    "RUNNING MODELS:",clipper_conn.get_all_models())
clipper_conn.link_model_to_app( app_name=app_name,model_name=model_name)

print(f"Model {model_name} attached to app {app_name}")


