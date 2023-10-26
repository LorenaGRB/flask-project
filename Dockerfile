FROM python:3.10
EXPOSE 5000
WORKDIR /app
COPY ./requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY . .
CMD ["flask", "run", "--host", "0.0.0.0"]
# docker build -t flask-smorest-api .
#  docker run -dp 5000:5000 -w /app -v "/c/Users/LorenaGabbyRojasBell/Desktop/Estudiando/flask:/app" flask-smorest-api