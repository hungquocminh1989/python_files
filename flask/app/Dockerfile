FROM python:3.8.6
RUN apt-get update

# install manually all the missing libraries
RUN apt-get install -y gconf-service libasound2 libatk1.0-0 libcairo2 libcups2 libfontconfig1 libgdk-pixbuf2.0-0 libgtk-3-0 libnspr4 libpango-1.0-0 libxss1 fonts-liberation libappindicator1 libnss3 lsb-release xdg-utils

# install chrome
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN dpkg -i google-chrome-stable_current_amd64.deb; apt-get -fy install

# Miniconda3 missing libraries
RUN apt-get install -y libgl1-mesa-glx libegl1-mesa libxrandr2 libxss1 libxcursor1 libxcomposite1 libasound2 libxi6 libxtst6

RUN mkdir /usr/src/app
WORKDIR /usr/src/app
COPY requirements.txt requirements.txt
COPY Miniconda3-latest-Linux-x86_64.sh Miniconda3-latest-Linux-x86_64.sh
RUN ./Miniconda3-latest-Linux-x86_64.sh -bfp ./miniconda3
RUN export PATH=/usr/src/app/miniconda3/bin:$PATH
RUN conda create -n -y abc python=3
RUN pip install -r requirements.txt 
ENTRYPOINT ["python"] 
CMD ["/home/main.py"]
WORKDIR /home