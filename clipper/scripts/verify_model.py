#!/usr/bin/env python\
try:
    model_path = str(sys.argv[1])
    print("Evaluating with ",  model_path,)
except Exception as e:
    print("ERROR!!"+str(e))
    print("USAGE:\n\tpython build_deploy.py <model_path>")

print("Importing model...")
model = cloudpickle.load(open( model_path,'rb'))
print(model.translate(['Hello world!','This is clipper world','Wait whaat!'], beam=5))