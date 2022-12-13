FROM python:3.11 as base

ENV POETRY_HOME=/poetry
ENV PATH=${POETRY_HOME}/bin:${PATH}
ENV PYTHONPATH=/app

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python -

RUN mkdir /app
COPY pyproject.toml poetry.toml /app/
WORKDIR /app
RUN poetry install

COPY . /app

EXPOSE 5000

FROM base as development
ENTRYPOINT ["poetry", "run", "flask", "run", "--host=0.0.0.0"]

FROM base as production
ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0:5000", "todo_app.wsgi:app"]

FROM base as test
ENTRYPOINT [ "poetry", "run", "pytest" ]