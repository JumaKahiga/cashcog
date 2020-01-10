FROM python:3.7

MAINTAINER Kenneth Kabiru "kabirumwangi@gmail.com"

WORKDIR /usr/cashcog

# copy the file containing the app dependencies
COPY ./requirements.txt ./

# install all the dependencies
RUN pip3 install -r requirements.txt

COPY . .

ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.7.2/wait /wait
RUN chmod +x /wait

CMD /wait && /usr/cashcog/entry_point.sh