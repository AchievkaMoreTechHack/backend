FROM python:3.9

ENV PYTHONUNBUFFERED 1

EXPOSE 8000
WORKDIR /src

COPY poetry.lock pyproject.toml ./
RUN pip install poetry==1.1 && \
    poetry config virtualenvs.in-project true && \
    poetry install --no-dev

COPY src ./

CMD poetry run python main.py
