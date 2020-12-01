
SCRIPTS=./scripts
DOCKERFILE=./dockerfiles
IS_CUDA?=True
MODEL_PATH?=./model/model.pkl
APP_NAME?=nmt
MODEL_NAME?=nmtfairseq
SLO?=1000000
CONTAINERS=$(shell docker ps -a -q)
BATCH_SIZE?=-1
## Shell ENV

all: init_env_aws start_clipper build_model deploy_model

init_env_local:
	$ pip install pipenv 
	$ pipenv install
	$ pipenv Shell
	$ chmod u+x scripts/*.py
	start_clipper

init_env_aws:
	$ pip install clipper_admin cloudpickle==0.5.3 git+git://github.com/pytorch/fairseq.git
	$ chmod u+x scripts/*.py

build_custom_image:
	$ docker build -t device-query ${DOCKERFILE}/nvidia/
	$ docker build -t custom-image ${DOCKERFILE}/custom/

start_clipper:
	$ ${SCRIPTS}/start_clipper.py

stop_clipper:
	$ ${SCRIPTS}/stop_clipper.py

build_model: 
	$ ${SCRIPTS}/build_model.py $(IS_CUDA) $(MODEL_PATH)
	$ ${SCRIPTS}/verify_model.py ${MODEL_PATH}

deploy_model: $(MODEL_PATH) build_custom_image
	$ echo "Deploying model"
	$ ${SCRIPTS}/deploy_model.py $(IS_CUDA) $(MODEL_PATH) $(APP_NAME) ${MODEL_NAME} ${SLO} ${BATCH_SIZE}

undeploy_model:
	@ ${SCRIPTS}/remove_model.py ${APP_NAME} ${MODEL_NAME}
	# $ echo ${CONTAINERS}
	# docker rm $(shell docker ps -a -q)

clean: stop_clipper
	-docker rm $(shell docker ps -a -q)
	-docker image prune -a -f
	-pip uninstall -y clipper_admin cloudpickle fairseq
	-rm ${MODEL_PATH}
	
