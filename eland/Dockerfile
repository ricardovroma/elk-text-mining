FROM python:3-slim

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

COPY ./load_data.py /app/load_data.py

RUN chmod +x /app/load_data.py

CMD ["python", "/app/load_data.py"]