FROM sunpeek/poetry:py3.10-slim

RUN apt-get update
RUN apt install -y ffmpeg libsm6 libxext6

WORKDIR /root/
COPY README.md /root
COPY pyproject.toml /root
COPY poetry.lock /root

RUN poetry install --only main
RUN pip3 cache purge
RUN apt-get clean

RUN mkdir api
WORKDIR /root/api
COPY api /root/api/api
COPY main.py /root/api

ENTRYPOINT ["poetry", "run", "python", "-m", "uvicorn", "main:app", "--host=0.0.0.0", "--port=80"]