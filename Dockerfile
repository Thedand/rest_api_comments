FROM python:3.9.6-buster
ENV PYTHONUNBUFFERED=1

# Creating working directory
RUN mkdir /blog
WORKDIR /blog

# Copying requirements
COPY . /blog

RUN pip install -r requirements.txt

ENTRYPOINT ["sh", "/usr/src/blog/entrypoint.sh"]