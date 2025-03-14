
FROM ubuntu:22.04

WORKDIR /app

ENV DEBIAN_FRONTEND noninteractive
ENV LD_LIBRARY_PATH=/lib/x86_64-linux-gnu:$LD_LIBRARY_PATH
ENV NVIDIA_VISIBLE_DEVICES all
ENV NVIDIA_DRIVER_CAPABILITIES compute
RUN apt-get update && \
    apt-get install -y  clinfo nvidia-cuda-toolkit python3 python3-pip libvcflib-tools libvcflib-dev nano\
    samtools ocl-icd-libopencl1 ocl-icd-opencl-dev nvidia-opencl-dev tabix bcftools && \
    rm -rf /var/lib/apt/lists/*

ENV PATH="$PATH:/usr/lib/vcflib/bin"
COPY requirements.txt /app

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt


COPY . /app
EXPOSE 8000
