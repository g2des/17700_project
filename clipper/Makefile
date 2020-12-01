
SCRIPTS=./scripts
DOCKERFILE=./dockerfiles
IS_CUDA?=True
MODEL_PATH?=./model/model.pkl
APP_NAME?=nmt
MODEL_NAME?=nmtfairseq
SLO?=1000000
CONTAINERS=$(shell docker ps -a -q)
## Shell ENV
init_env_local:
	$ pip install pipenv 
	$ pipenv install
	$ pipenv Shell
	$ chmod u+x scripts/*.py
	start_clipper

init_env_aws:
	$ pip install clipper_admin cloudpickle git+git://github.com/pytorch/fairseq.git
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

deploy_model: $(MODEL_PATH) build_custom_image build_model
	$ echo "Deploying model"
	$ ${SCRIPTS}/deploy_model.py $(IS_CUDA) $(MODEL_PATH) $(APP_NAME) ${MODEL_NAME} ${SLO}

undeploy_model:
	@ ${SCRIPTS}/remove_model.py ${APP_NAME} ${MODEL_NAME}
	# $ echo ${CONTAINERS}
	- docker rm $(shell docker ps -a -q)

clean: stop_clipper
	- docker rm $(shell docker ps -a -q)
	- docker image prune -a -f
	@rm ${MODEL_PATH}
	
