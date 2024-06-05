FROM python:3.9-bookworm

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /RelovistaBot

COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . ./
RUN chmod -R 755 ./

CMD ["python3", "main.py"]