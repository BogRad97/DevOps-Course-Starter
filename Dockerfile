FROM python:3.9 as base
RUN pip install "poetry"
RUN pip install "flask"
RUN pip install "gunicorn"
RUN pip install "pytest"
RUN pip install "python-dotenv"
RUN mkdir /app
COPY . /app
WORKDIR /app
RUN poetry install
EXPOSE 5000

FROM base as development
ENTRYPOINT ["poetry", "run", "flask", "run", "--host=0.0.0.0"]

FROM base as production
ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0:5000", "todo_app.wsgi:app"]

FROM base as test
ENTRYPOINT [ "poetry", "run", "pytest" ]