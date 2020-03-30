FROM mongo:4.0

# copy the raw data and source code to the image
copy init/* /init/
RUN apt-get update \
     &&apt-get install -y python\
     &&apt-get install -y python-pip\
     &&pip install --upgrade pip

# install python library
COPY ./requirements.txt /requirements.txt
RUN pip install -r requirements.txt

