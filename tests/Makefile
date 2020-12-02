
ifndef BATCH_SIZE
$(error BATCH_SIZE is not set. USE : make RECIPY BATCH_SIZE=<int> REMEMBER BATCH_SIZE values are [1,2,4,8,16,32,64])
endif	

RESULT_FOLDER=./results
LOGS_FOLDER = ./logs

CLIPPER_USER?=./clipper_user.py
CLIPPER_CSV_NAME?=${RESULT_FOLDER}/clipper_${BATCH_SIZE}
CLIPPER_LOG_FILE?=$(LOGS_FOLDER)/clipper_logs_${BATCH_SIZE}

TFSERVE_USER?=./tfserve_user.py
TFSERVE_CSV_NAME?=${RESULT_FOLDER}/tfserve
TFSERVE_LOG_FILE?=$(LOGS_FOLDER)/tfserve_logs

TORCH_USER?=./torch_user.py
TORCH_CSV_NAME?=${RESULT_FOLDER}/torch
TORCH_LOG_FILE?=$(LOGS_FOLDER)/torch_logs


CONDITION1 := --users 100 --spawn-rate 10 --run-time 4 --csv-full-history
CONDITION2 := --users 1000 --spawn-rate 10 --run-time 4 --csv-full-history
CONDITION3 := --users 5000 --spawn-rate 10 --run-time 4 --csv-full-history
CONDITION4 := --users 100 --spawn-rate 10 --run-time 4 --csv-full-history
CONDITION5 := --users 1000 --spawn-rate 100 --run-time 4 --csv-full-history
CONDITION6 := --users 5000 --spawn-rate 1000 --run-time 4 --csv-full-history

init:
	@pip install locust numpy requests
	@wget -qO- http://www.statmt.org/wmt14/training-parallel-nc-v9.tgz | tar zxvf - -C ./data/
	# @curl   | tar -  
	# --directory=./data/


clipper: 
	@locust --headless -f ${CLIPPER_USER} ${CONDITION1} --csv ${CLIPPER_CSV_NAME}_1 --logfile ${CLIPPER_LOG_FILE}_1
	@locust --headless -f ${CLIPPER_USER} ${CONDITION2} --csv ${CLIPPER_CSV_NAME}_2 --logfile ${CLIPPER_LOG_FILE}_2
	@locust --headless -f ${CLIPPER_USER} ${CONDITION3} --csv ${CLIPPER_CSV_NAME}_3 --logfile ${CLIPPER_LOG_FILE}_3
	@locust --headless -f ${CLIPPER_USER} ${CONDITION4} --csv ${CLIPPER_CSV_NAME}_4 --logfile ${CLIPPER_LOG_FILE}_4
	@locust --headless -f ${CLIPPER_USER} ${CONDITION5} --csv ${CLIPPER_CSV_NAME}_5 --logfile ${CLIPPER_LOG_FILE}_5
	@locust --headless -f ${CLIPPER_USER} ${CONDITION6} --csv ${CLIPPER_CSV_NAME}_6 --logfile ${CLIPPER_LOG_FILE}_6

tfserve: 
	@locust --headless -f ${TFSERVE_USER} ${CONDITION2} --csv ${TFSERVE_CSV_NAME}_1 --logfile ${TFSERVE_LOG_FILE}_1
	@locust --headless -f ${TFSERVE_USER} ${CONDITION2} --csv ${TFSERVE_CSV_NAME}_2 --logfile ${TFSERVE_LOG_FILE}_2
	@locust --headless -f ${TFSERVE_USER} ${CONDITION3} --csv ${TFSERVE_CSV_NAME}_3 --logfile ${TFSERVE_LOG_FILE}_3
	@locust --headless -f ${TFSERVE_USER} ${CONDITION4} --csv ${TFSERVE_CSV_NAME}_4 --logfile ${TFSERVE_LOG_FILE}_4
	@locust --headless -f ${TFSERVE_USER} ${CONDITION5} --csv ${TFSERVE_CSV_NAME}_5 --logfile ${TFSERVE_LOG_FILE}_5
	@locust --headless -f ${TFSERVE_USER} ${CONDITION6} --csv ${TFSERVE_CSV_NAME}_6 --logfile ${TFSERVE_LOG_FILE}_6
	
torch: 
	@locust --headless -f ${TORCH_USER} ${CONDITION2} --csv ${TORCH_CSV_NAME}_1 --logfile ${TORCH_LOG_FILE}_1
	@locust --headless -f ${TORCH_USER} ${CONDITION2} --csv ${TORCH_CSV_NAME}_2 --logfile ${TORCH_LOG_FILE}_2
	@locust --headless -f ${TORCH_USER} ${CONDITION3} --csv ${TORCH_CSV_NAME}_3 --logfile ${TORCH_LOG_FILE}_3
	@locust --headless -f ${TORCH_USER} ${CONDITION4} --csv ${TORCH_CSV_NAME}_4 --logfile ${TORCH_LOG_FILE}_4
	@locust --headless -f ${TORCH_USER} ${CONDITION5} --csv ${TORCH_CSV_NAME}_5 --logfile ${TORCH_LOG_FILE}_5
	@locust --headless -f ${TORCH_USER} ${CONDITION6} --csv ${TORCH_CSV_NAME}_6 --logfile ${TORCH_LOG_FILE}_6
	