FROM python:3.11.5-slim-bullseye

ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . code
WORKDIR /code

EXPOSE 8000

ENTRYPOINT ["python", "./manage.py"]
CMD ["runserver", "0.0.0.0:8000"]