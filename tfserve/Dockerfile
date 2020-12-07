# Using the official tensorflow serving image from docker hub as base image
FROM tensorflow/serving

# Installing NGINX, used to rever proxy the predictions from SageMaker to TF Serving
RUN apt-get update && apt-get install -y --no-install-recommends nginx git

# Copy our model folder to the container
COPY ende /ende

# Copy NGINX configuration to the container
COPY nginx.conf /etc/nginx/nginx.conf

# Copy batching params
COPY batching_parameters.txt batching_parameters.txt

# starts NGINX and TF serving pointing to our model
ENTRYPOINT service nginx start | tensorflow_model_server \--enable_batching=true \--batching_parameters_file=batching_parameters.txt \
 --rest_api_port=8501 \
 --model_name=ende \
 --model_base_path=/ende