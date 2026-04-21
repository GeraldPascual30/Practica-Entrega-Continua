# Práctica DevOps: Hola Mundo con Docker

## Objetivo
Crear una aplicación web sencilla, contenerizarla con Docker y subir la imagen a Docker Hub como parte del ciclo básico de DevOps.

## Tecnologías utilizadas
- Python
- Flask
- Docker
- Docker Hub

## Estructura del proyecto
- app.py
- requirements.txt
- Dockerfile
- README.md

## Ejecución local
```bash
pip install -r requirements.txt
python app.py

Abrir en el navegador:
http://localhost:5000

Construcción de la imagen Docker:
docker build -t geraldpascual30/hola-devops:1.0 .

Ejecución del contenedor:
docker run -p 5000:5000 geraldpascual30/hola-devops:1.0

Subir a Docker Hub:
docker login
docker push geraldpascual30/hola-devops:1.0




