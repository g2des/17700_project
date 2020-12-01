FROM device-query:latest
# RUN pip install https://download.pytorch.org/whl/cpu/torch-1.0.0-cp36-cp36m-linux_x86_64.whl torchvision
# RUN apt-get update && apt-get install -y git
# RUN sudo apt-get install apt-transport-https
# RUN sudo apt-get install gcc
# RUN pip install wget
ARG url=https://raw.githubusercontent.com/ucbrise/clipper/develop/containers/python

RUN touch /model_is_ready.check
RUN apt-get  update &&  apt-get install -y -qq libzmq5 libzmq5-dev redis-server libsodium18 build-essential
RUN pip install numpy==1.18.1
RUN pip install -q cloudpickle==0.5.3 pyzmq==17.0.* prometheus_client==0.1.* \
    pyyaml>=4.2b1 jsonschema==2.6.* redis==2.10.* psutil==5.4.* flask==0.12.2 
RUN pip install dataclasses hydra-core regex fastBPE zmq requests sacremoses subword_nmt
RUN pip install git+git://github.com/pytorch/fairseq.git
RUN pip install clipper_admin
RUN mkdir /model
RUN echo alias python="python3" >> ~/.bashrc
RUN wget --directory-prefix=/container $url/pytorch_container.py $url/rpc.py $url/container_entry.sh $url/__init__.py 
RUN wget --directory-prefix=/container $url/../../monitoring/metrics_config.yaml 
RUN chmod 777 /container/pytorch_container.py
RUN chmod 777 /container/container_entry.sh
# RUN wget --directory-prefix=/container/ $url/pytorch_container.py $url/container_entry.sh

HEALTHCHECK --interval=3s --timeout=3s --retries=1 CMD test -f /model_is_ready.check || exit 1

ENV CLIPPER_MODEL_PATH=/model
CMD ["/container/container_entry.sh", "pytorch-container", "/container/pytorch_container.py"]
