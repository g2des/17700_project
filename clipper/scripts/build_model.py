#!/usr/bin/env python
import sys
import torch, cloudpickle

try:
    is_cuda = eval(sys.argv[1])
    output_path = str(sys.argv[2])
    print("Evaluating with ", is_cuda, output_path)
except Exception as e:
    print("ERROR!!"+str(e))
    print("USAGE:\n\tpython build_deploy.py <True|False> <output_path>")

en2fr = torch.hub.load('pytorch/fairseq', 'transformer.wmt14.en-fr', tokenizer='moses', bpe='subword_nmt',force_reload=True)
if torch.cuda.is_available() and is_cuda:
    print("Enabling cuda")
    en2fr.cuda()

func = cloudpickle.dumps(en2fr)
file = open(output_path,'wb') 
file.write(func)
file.close()
print("Model successfully written to", output_path)