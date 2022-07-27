FROM python:3.9-slim-bullseye
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
RUN python setup.py
COPY ./geckodriver.exe /bin/
ENV PATH /bin/:$PATH