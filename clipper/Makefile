SCRIPTS=./scripts
DOCKERFILE=./dockerfiles
IS_CUDA?=True
MODEL_PATH?=./model/model.pkl
APP_NAME?=nmt
MODEL_NAME?=nmtfairseq
SLO?=1000000
## Shell ENV
init_env:
	$ pip install pipenv 
	$ pipenv install
	$ pipenv Shell
	$ chmod u+x /scripts/*.py
	start_clipper	

build_custom_image:
	$ docker build -t device-query ${DOCKERFILE}/nvidia/
	$ docker build -t custom-image ${DOCKERFILE}/custom/

start_clipper:
	$ ${SCRIPTS}/start_clipper.py

stop_clipper:
	$ ${SCRIPTS}/stop_clipper.py

build_model: 
	$ ${SCRIPTS}/build_model.py $(IS_CUDA) $(MODEL_PATH)

deploy_model: $(MODEL_PATH)
	$ echo "Deploying model"
	$ ${SCRIPTS}/deploy_model.py $(IS_CUDA) $(MODEL_PATH) $(APP_NAME) ${MODEL_NAME} ${SLO}

remove_model:
	$ ${SCRIPTS}/remove_model.py ${APP_NAME} ${MODEL_NAME}
	$ docker rm ${docker ps -a -q}