FROM quay.io/pypa/manylinux2014-x86_64:latest

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /RelovistaBot

COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . ./
RUN chmod -R 755 ./

CMD ["python3", "main.py"]