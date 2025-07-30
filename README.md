# 🚀 Flask App Deployment via GitHub Actions CI/CD to Docker Hub

This project demonstrates how to automate the deployment of a **Dockerized Flask application** to **Docker Hub** using **GitHub Actions**. It showcases a basic CI/CD pipeline setup where the app is built, tested, and published every time changes are pushed to the `main` branch.

This repository was created to highlight my understanding of DevOps workflows as part of an internship application.

---

## 📁 Project Structure

- `.github/workflows/` – Contains GitHub Actions workflow for CI/CD
  - `cicd.yml` – Main workflow that builds and pushes the Docker image
- `app.py` – The main Flask application
- `test_app.py` – Unit tests for the Flask app
- `requirements.txt` – Python dependencies
- `DockerFile` – Instructions to build the Docker image

---

## 🔧 Technologies Used

- **Python 3.x**
- **Flask**
- **Docker**
- **GitHub Actions**
- **Docker Hub**

---

## 📌 CI/CD Workflow Overview

1. **Trigger**: On every push to the `main` branch
2. **Build**: Docker image for the Flask app
3. **Test**: Runs `test_app.py` to validate the app
4. **Push**: The image is pushed to Docker Hub using credentials stored in GitHub Secrets

---

## 🔐 GitHub Secrets Configuration

To push the Docker image securely, set up the following GitHub Actions secrets:

- `DOCKER_USERNAME` – Your Docker Hub username
- `DOCKER_PASSWORD` – Your Docker Hub password or access token

---

## 🐳 Running Locally

```bash
docker build -t flask-app .
docker run -p 5000:5000 flask-app
```

Visit `http://localhost:5000` to view the app.

---

## 📬 Contact

**Name:** *[Bhavesh Mishra]*  
**Email:** *sloth1135@gmail.com*

---

