FROM python:3.8-slim-buster

WORKDIR /app
COPY . /app
COPY artifacts/model.pkl /app/artifacts/model.pkl

RUN apt-get update && apt-get install -y build-essential
RUN pip install --no-cache-dir -r requirement.txt
RUN chmod 777 /app/artifacts/model.pkl


EXPOSE 5000


CMD ["python" , "app.py"]