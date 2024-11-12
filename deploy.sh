#!/bin/bash

PROJECT_ID="chatbot-zaap"
SERVICE_NAME="magneto-app"
REGION="southamerica-west1"
IMAGE_NAME="gcr.io/$PROJECT_ID/$SERVICE_NAME"

echo "Building the Docker image..."
docker build -t $IMAGE_NAME .

echo "Authenticating to Google Cloud"
gcloud auth configure-docker

echo "Uploading image to Google Container Registry..."
docker push $IMAGE_NAME

echo "Deploying to Cloud Run..."
gcloud run deploy $SERVICE_NAME --image $IMAGE_NAME --region $REGION

echo "Deployment completed on Cloud Run."

