FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app
RUN pip install --upgrade pip
RUN apt-get update
RUN apt-get install libasound-dev libportaudio2 libportaudiocpp0 portaudio19-dev -y
RUN pip install -r requirements.txt
RUN apt install -y espeak
RUN apt-get install -y pulseaudio
COPY . /app
CMD [ "python", "test.py" ]