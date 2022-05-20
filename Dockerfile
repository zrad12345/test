FROM python:3.9.13
ENV PYTHONPATH="."
RUN mkdir /app
COPY ./calculator.py /app/
COPY ./test_calculator.py /app/
ENTRYPOINT ["python3", "/app/test_calculator.py"]
