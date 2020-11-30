FROM nvidia/cuda:10.1-base-ubuntu16.04

# Install some basic utilities
RUN apt-get update && apt-get install -y \
    software-properties-common \
#    sudo \
    curl \
    ca-certificates \
    git \
    bzip2 \
    wget \
    gcc \
    g++ \
    # python3.6 \
    libx11-6 \
 && rm -rf /var/lib/apt/lists/*
# RUN add-apt-repository ppa:deadsnakes/ppa
# RUN apt-get update && apt-get install -y python3.6 python3-pip
# RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.6 1
# RUN echo alias python="python3.6" >> ~/.bashrc
# RUN echo alias pip="pip3" >> ~/.bashrc
# RUN pip3 install --upgrade pip
# RUN pip3 install torch==1.4.0 torchvision==0.5.0 numpy==1.18.1
# Create a working directory
RUN mkdir /container
WORKDIR /container

# Create a non-root user and switch to it
# RUN adduser --disabled-password --gecos '' --shell /bin/bash user \
#  && chown -R user:user /app
# RUN echo "user ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/90-user
# USER user

# All users can use /home/user as their home directory
ENV HOME=/root
RUN chmod 777 /root

# Install Miniconda and Python 3.6
ENV CONDA_AUTO_UPDATE_CONDA=false
ENV PATH=/root/miniconda/bin:$PATH
RUN curl -sLo ~/miniconda.sh https://repo.continuum.io/miniconda/Miniconda3-4.7.12.1-Linux-x86_64.sh \
 && chmod +x ~/miniconda.sh \
 && ~/miniconda.sh -b -p ~/miniconda \
 && rm ~/miniconda.sh \
 && conda install -y python==3.6.9 \
 && conda clean -ya

# CUDA 10.1-specific steps
RUN conda install -y -c pytorch \
    cudatoolkit=10.1 \
    "pytorch=1.4.0=py3.6_cuda10.1.243_cudnn7.6.3_0" \
    "torchvision=0.5.0=py36_cu101" \
 && conda clean -ya

# Set the default command to python3
CMD ["python3"]
