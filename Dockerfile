FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

WORKDIR /src
COPY ./ /src/

RUN pip3 install -r requirements.txt

EXPOSE 8000

CMD ["python3", "main.py"]