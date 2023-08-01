# API_Python_Flask_SQL
 Praticando Python Data Analyst

## Crie o ambiente virtual para o projeto
python3 -m venv .venv && source .venv/bin/activate

# PIP
flask

mysql-connector-python

# Testando no Postman

Here's how you can do it in Postman:

- Open Postman and go to the request builder.
- Select the HTTP method as POST.
- Enter the URL: http://127.0.0.1:5000/carros
- Click on the "Headers" tab.
- Add a new header with the key Content-Type and the value application/json.
- Go to the "Body" tab.
- Select the "raw" option.
- Enter the JSON data in the request body:


# Docker
docker build -t dbcarros-db .

docker run --name dbCarros -d -p 3306:3306 -e MYSQL_ROOT_PASSWORD=root -e MYSQL_DATABASE=DbCarros -e MYSQL_USER=user -e MYSQL_PASSWORD=123456 dbcarros-db 