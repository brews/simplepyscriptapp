FROM python:3.8-slim
WORKDIR /usr/src/app
COPY . .
CMD ["python", "simplescript.py"]
