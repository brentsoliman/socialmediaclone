FROM python:3.10-alpine
ENV DATABASE_HOSTNAME=172.17.0.2
ENV DATABASE_PORT=5432
ENV DATABASE_USERNAME=postgres
ENV DATABASE_PASSWORD=password123
ENV DATABASE_NAME=socialMedia
RUN mkdir -p /home/application && cd /home
RUN python -m venv env
RUN source env/bin/activate
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev \
    && apk add libffi-dev
RUN pip install --upgrade pip
RUN pip3 install fastapi uvicorn sqlalchemy psycopg2-binary 'passlib[bcrypt]' python-multipart
RUN pip3 install 'python-jose[cryptography]'
COPY ./application /application
CMD ["uvicorn","application.app:app","--host","0.0.0.0","--port","7001", "--root-path='/api'"]