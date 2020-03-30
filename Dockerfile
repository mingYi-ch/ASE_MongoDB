FROM mongo:4.0

# copy the raw data and source code to the image
copy init_db/* /init_db/
RUN apt-get update \
     &&apt-get install -y python\
     &&apt-get install -y python-pip\
     &&pip install --upgrade pip
# copy sh
COPY ./init_db.sh /docker-entrypoint-initdb.d/
# install python library
COPY ./pylib_list /pylib_list
RUN pip install -r pylib_list
