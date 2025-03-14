FROM python:3.11-slim

WORKDIR /app

#ENV DEBIAN_FRONTEND noninteractive
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && \
    apt-get install -y python3 python3-pip libvcflib-tools libvcflib-dev nano\
    samtools ocl-icd-libopencl1 ocl-icd-opencl-dev tabix bcftools && \
    rm -rf /var/lib/apt/lists/*

#ENV PATH="$PATH:/usr/lib/vcflib/bin"
COPY . /app

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt
ENTRYPOINT ["python", "vcf-cas-offinder.py"]
