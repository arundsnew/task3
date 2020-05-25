

FROM centos:latest

RUN yum install python36 -y
RUN curl "https://bootstrap.pypa.io.get-pip.py" -o "get-pip.py"
RUN python3 get-pip.py

RUN pip3 install sklearn -y
RUN pip3 install matplotlib -y
RUN pip3 install seaborn -y
RUN pip3 install pandas -y
RUN pip3 install opencv-python -y
RUN pip3 install tensorflow -y
RUN pip3 install scipy -y
RUN pip3 install keras -y
RUN pip3 install pillow -y
