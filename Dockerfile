FROM python:latest

COPY . /app

WORKDIR /app

RUN pip install -r requirement.txt

CMD [ "python", "ascii2pdf.py" ]