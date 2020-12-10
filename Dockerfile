FROM python:3.7-alpine
WORKDIR /car_configurator
COPY . .
RUN pip install flask
RUN pip install -r requirements.txt
ENTRYPOINT [ "python" ]
CMD [ "run.py" ]
