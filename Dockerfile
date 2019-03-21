FROM python:3

WORKDIR /workspace

RUN chmod -R 777 /workspace
COPY requirements.txt /workspace
RUN pip install --no-cache-dir -r requirements.txt

COPY . /workspace
