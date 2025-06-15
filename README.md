# Machine Learning MNIST Model and Pipeline 🚀

[![Build, train, scan and deploy the model](https://github.com/kalined/ml-model-infra-task/actions/workflows/cicd.yml/badge.svg)](https://github.com/kalined/ml-model-infra-task/actions/workflows/cicd.yml)

## Table of Contents
- [Overview](#overview)
- [Key Components](#key-components)
- [Pipeline Diagram](#pipeline-diagram)
  - [Model Retraining and Evaluation](#1-model-retraining-and-evaluation)
  - [Model Training, Building, Image Scanning and Deployment](#2-model-training-building-image-scanning-and-deployment-to-the-local-kubernetes-cluster)

---

## Overview

This repository contains a machine learning pipeline for training, evaluating and deploying models using GitHub Actions workflows. The pipeline is designed to automate the retraining of models, evaluate their performance against the current production model and deploy the new model if it performs better. The repository also includes CI/CD workflow for building, scanning and deploying the application to a Kubernetes cluster.

## Key Components

### **1. Retrain Workflow**
- **Purpose**: Retrains the model using new data and evaluates its performance against the production model.
- **Logic**:
  - If the retrained model performs better, the check passes, allowing the user to merge changes to the main (default) branch and deploy the new model to production.
  - If the retrained model performs worse, the check fails, preventing deployment.

### **2. CI/CD Workflow**
- **Purpose**: Deliver new model and use it in the API endpoint `/predict`.
- **Jobs**:
  - **Build and Train**:
    - Retrieves the latest dataset.
    - Trains the model.
    - Builds a Docker image for the application.
  - **Scan**:
    - Runs a vulnerability scan on the Docker image using Trivy.
  - **Create Cluster and Deploy**:
    - Sets up a Minikube cluster.
    - Deploys the application using Helm.
    - Tests the `/predict` endpoint of the deployed application.


## Pipeline Diagram

Below are Mermaid diagrams that illustrate the logic of the pipeline. It consist mainly of two parts:

### **1. Model retraining and evaluation**

```mermaid
    graph TD
        A[Create a Pull Request from the Feature Branch] --> B[Retrieve Latest Data]
        B --> C[Train the Model on the Latest Data]
        C --> D[Evaluate Model Performance]
        D --> E{Performance Check}
        E -->|Pass| F[Check Passed, Allow Merge]
        E -->|Fail| G[Check Failed, Prevent Merge]

        style A fill:#f9f,stroke:#333,stroke-width:2px,color:#000
        style B fill:#bbf,stroke:#333,stroke-width:2px,color:#000
        style C fill:#bbf,stroke:#333,stroke-width:2px,color:#000
        style D fill:#bbf,stroke:#333,stroke-width:2px,color:#000
        style E fill:#f96,stroke:#333,stroke-width:2px,color:#000
        style F fill:#9f9,stroke:#333,stroke-width:2px,color:#000
        style G fill:#f99,stroke:#333,stroke-width:2px,color:#000
```

### **2. Model training, building, image scanning and deployment to the local kubernetes cluster**

```mermaid
    graph TD
        A[Push to Main Branch] --> B[Build and Train Job]
        B --> C[Retrieve Latest Dataset]
        C --> D[Train Model Using Notebook]
        D --> E["Push Created Artifact (Docker Image) to Registry"]
        E --> G[Scan Docker Image]
        G --> I[Create Local Cluster]
        I --> J["Deploy Application with the Latest Model Using Helm"]
        J --> K[Test /predict Endpoint]

        style A fill:#f9f,stroke:#333,stroke-width:2px,color:#000
        style B fill:#bbf,stroke:#333,stroke-width:2px,color:#000
        style C fill:#bbf,stroke:#333,stroke-width:2px,color:#000
        style D fill:#bbf,stroke:#333,stroke-width:2px,color:#000
        style E fill:#f96,stroke:#333,stroke-width:2px,color:#000
        style G fill:#bbf,stroke:#333,stroke-width:2px,color:#000
        style I fill:#bbf,stroke:#333,stroke-width:2px,color:#000
        style J fill:#9f9,stroke:#333,stroke-width:2px,color:#000
        style K fill:#9f9,stroke:#333,stroke-width:2px,color:#000
```