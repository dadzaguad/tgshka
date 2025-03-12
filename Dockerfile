FROM python:3.13-slim-bullseye

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

CMD [ "python", "main.py" ]