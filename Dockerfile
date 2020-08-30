FROM python:3.8
MAINTAINER Computer Science House Drink Admins <drink@csh.rit.edu>

WORKDIR /opt/potion-seller
RUN pip install pipenv

COPY Pipfile* /opt/potion-seller/
RUN pipenv lock --requirements > requirements.txt \
    && pipenv --rm \
    && pip install -r requirements.txt

COPY . /opt/potion-seller

CMD gunicorn -w 1 -b 0.0.0.0:5000 potion_seller:app
