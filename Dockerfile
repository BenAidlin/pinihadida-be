FROM ubuntu
COPY . /app 
WORKDIR /app
RUN apt-get update -y
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN pip install --no-cache-dir -r requirements.txt
CMD python3 hello_world.py