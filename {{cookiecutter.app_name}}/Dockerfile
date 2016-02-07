FROM python:2.7
RUN pip install tox
ADD setup.py /tmp/setup.py
RUN cd /tmp && pip install -e . && rm -rf /tmp/*
RUN pip install Flask-Migrate MySQL-python
USER www-data