FROM python:3.8.6
RUN mkdir /usr/src/app
WORKDIR /usr/src/app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt 
ENTRYPOINT ["python"] 
CMD ["/home/main.py"]
WORKDIR /home
