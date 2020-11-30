SCRIPTS=./scripts
DOCKERFILE=./dockerfiles
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

