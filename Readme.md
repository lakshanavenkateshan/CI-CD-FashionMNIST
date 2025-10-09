# Fashion-MNIST API

## Project Overview
This is a Dockerized ML API for the Fashion-MNIST dataset.

## Features
- Predicts fashion items from image vectors
- Deployed on AWS ECS
- Monitored with Prometheus + Grafana
- CI/CD pipeline via GitHub Actions

## Screenshots
1. Grafana dashboard (real-time metrics)
2. GitHub Actions CI/CD success
3. Running Docker containers

## How to Run Locally
1. Build Docker image:
   docker build -t fashion-mnist-api .
2. Run container:
   docker run -p 5000:5000 fashion-mnist-api
3. Test API:
   curl -X POST http://localhost:5000/predict -H "Content-Type: application/json" -d '{"features":[0,0,...,0]}'
