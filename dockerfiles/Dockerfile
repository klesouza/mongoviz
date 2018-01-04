FROM python:2.7

RUN mkdir /home/ww

WORKDIR /home/www

COPY requirements.txt /home/www/
RUN pip install -r requirements.txt

COPY ./web /home/www/

EXPOSE 5000

CMD ["python", "runserver.py"]