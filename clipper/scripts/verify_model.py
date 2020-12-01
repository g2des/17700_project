#!/usr/bin/env python\
print("Importing model...")
model = cloudpickle.load(open('./models.pkl','rb'))
print(model.translate(['Hello world!','This is clipper world','Wait whaat!'], beam=5))