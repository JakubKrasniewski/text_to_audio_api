FROM python:3.11-alpine
WORKDIR /text_to_audio_api
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
