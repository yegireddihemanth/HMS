# FROM nginx:alpine
# COPY . /usr/share/nginx/html

# FROM python:3.9
# WORKDIR  .
# COPY app.py .
# CMD ["hostel management system","app.py"]
FROM ubuntu
RUN apt update
RUN apt install python3-pip -y
RUN pip3 install Flask
WORKDIR C:\Users\heman\PycharmProjects\Hostel Management System\app.py
COPY . .
CMD ["python3","-m","flask","run","--host=0.0.0.0"]

