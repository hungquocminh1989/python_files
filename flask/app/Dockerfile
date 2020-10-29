FROM python:3.8.6

# UPDATE LINUX CORE
RUN apt-get update

# INSTALL MANUALLY ALL THE MISSING LIBRARIES
RUN apt-get install -y gconf-service libasound2 libatk1.0-0 libcairo2 libcups2 libfontconfig1 libgdk-pixbuf2.0-0 libgtk-3-0 libnspr4 libpango-1.0-0 libxss1 fonts-liberation libappindicator1 libnss3 lsb-release xdg-utils libgl1-mesa-glx libegl1-mesa libxrandr2 libxcursor1 libxcomposite1 libxi6 libxtst6

# INSTALL CHROME
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN dpkg -i google-chrome-stable_current_amd64.deb; apt-get -fy install

RUN mkdir /usr/src/app
WORKDIR /usr/src/app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt 
ENTRYPOINT ["python"] 
CMD ["/home/main.py"]
WORKDIR /home

# ================== MINICONDA===================
# CREATE FOLDER APP
#RUN mkdir /usr/src/app
#WORKDIR /usr/src/app

# COPY FILE INSTALL
#COPY . .

# INSTALL MINICONDA3
#RUN ./Miniconda3-latest-Linux-x86_64.sh -bfp ./miniconda3
#ENV PATH=/usr/src/app/miniconda3/bin:$PATH

# CREATE NEW ENV
#RUN . /usr/src/app/miniconda3/etc/profile.d/conda.sh \
	# IMPORT WITH FILE REQUIREMENTS.TXT
	#&& conda create -y -n docker_env python=3.8 \
	#&& conda activate docker_env \
	#&& pip install -r requirements.txt
	# IMPORT WITH FILE ENVIRONMENT.YML
	#&& conda env create -f environment.yml
	
# SET ENV PATH
#ENV PATH=/usr/src/app/miniconda3/envs/docker_env/bin:$PATH

#ENTRYPOINT ["python"] 
#CMD ["/home/main.py"]
#WORKDIR /home

# NOTE SCRIPT EXPORT
# conda env export > environment.yml

# ================== MINICONDA===================

