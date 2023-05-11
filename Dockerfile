FROM python:3.9.13
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY app .
COPY .gitignore .
CMD python main.py
