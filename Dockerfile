FROM python:3.11.0 AS library_system

WORKDIR /app

RUN pip install 'poetry==1.2.2'

COPY . /app/

RUN poetry install

#CMD ["tail", "-f", "/dev/null"]
CMD ["poetry", "run", "python", "-m", "src"]