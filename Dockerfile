FROM centos:latest

RUN yum install python36 -y

RUN pip3 install --upgrade pip
RUN pip3 install sklearn
RUN pip3 install matplotlib
RUN pip3 install seaborn
RUN pip3 install pandas
RUN pip3 install opencv-python
RUN pip3 install keras
RUN pip3 install pillow

CMD ["python3"."/root/Desktop/task3/fr1.py"]


