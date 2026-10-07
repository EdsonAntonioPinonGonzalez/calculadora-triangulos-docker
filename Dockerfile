FROM python:3.11-slim

RUN apt-get update && apt-get install -y git ca-certificates

WORKDIR /app

RUN git clone https://github.com/EdsonAntonioPinonGonzalez/calculadora-triangulos-docker.git .

CMD ["python", "calculadoraAreaTriangulo.py"]