FROM python:3.9-slim

WORKDIR /metafox-langchain-python

COPY . .

RUN pip3 install --upgrade pip

RUN pip3 install -r requirements.txt

CMD ["python", "main.py"]
