FROM python:alpine3.7
WORKDIR /app
COPY . .
ENTRYPOINT ["python", "./mainapp.exe"]
# CMD python ./mainapp.exe