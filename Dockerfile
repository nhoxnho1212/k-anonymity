FROM python:3.8.7-slim
WORKDIR /k-anonymity
COPY requirements.txt ./
RUN pip install -r requirements.txt

CMD python3 main.py -k ${K:-2} -d ${DATA_SOURCE} -r ${RETURN_SOURCE}
