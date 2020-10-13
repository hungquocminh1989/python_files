FROM python:3.8.6

RUN apt-get update

# Install manually all the missing libraries
RUN apt-get install -y gconf-service libasound2 libatk1.0-0 libcairo2 libcups2 libfontconfig1 libgdk-pixbuf2.0-0 libgtk-3-0 libnspr4 libpango-1.0-0 libxss1 fonts-liberation libappindicator1 libnss3 lsb-release xdg-utils libgl1-mesa-glx libegl1-mesa libxrandr2 libxcursor1 libxcomposite1 libxi6 libxtst6

# Install chrome
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN dpkg -i google-chrome-stable_current_amd64.deb; apt-get -fy install

RUN mkdir /usr/src/app
WORKDIR /usr/src/app

# Copy file
COPY requirements.txt requirements.txt
COPY Miniconda3-latest-Linux-x86_64.sh Miniconda3-latest-Linux-x86_64.sh

# Install miniconda3
RUN ./Miniconda3-latest-Linux-x86_64.sh -bfp ./miniconda3
ENV PATH=/usr/src/app/miniconda3/bin:$PATH

RUN	conda init bash
RUN conda create -y -n docker_env python=3.8
RUN conda activate docker_env
RUN pip install -r requirements.txt 
ENTRYPOINT ["python"] 
CMD ["/home/main.py"]
WORKDIR /home