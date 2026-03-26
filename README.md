#  Cloud-Native Three-Tier Java Application with CI/CD on AWS

##  Overview
This project demonstrates the end-to-end deployment of a **three-tier Java application** using modern DevOps practices. The application is containerized using Docker, integrated with a CI/CD pipeline using GitHub Actions, and deployed on AWS EC2 with images stored in Amazon ECR.

The goal of this project is to gain hands-on experience with:
- Containerization
- CI/CD automation
- Cloud deployment on AWS

---

##  Architecture

[ Client ]
↓
[ Web Tier (Java App) ]
↓
[ Application Tier ]
↓
[ Database Tier ]


- **Frontend / Web Layer**: Handles user requests  
- **Backend / Application Layer**: Business logic  
- **Database Layer**: Data persistence  

---

##  Tech Stack

| Category        | Tools / Technologies |
|----------------|---------------------|
| Language       | Java |
| Containerization | Docker |
| CI/CD          | GitHub Actions |
| Cloud          | AWS EC2, Amazon ECR |
| Version Control| Git & GitHub |

---

##  CI/CD Pipeline

The CI/CD pipeline is implemented using **GitHub Actions** and performs the following steps:

1. Code Checkout  
2. Build Docker Image  
3. Authenticate with AWS  
4. Push Image to Amazon ECR  
5. Deploy to EC2 Instance  

---

##  Docker Setup

### Build Docker Image
```bash
docker build -t your-image-name .
```
#  AWS Deployment
## Prerequisites
- AWS Account
- IAM user with ECR & EC2 access
- EC2 instance (Docker installed)
- ECR repository created
## Steps
- Create ECR repository
- Configure GitHub Secrets:
- AWS_ACCESS_KEY_ID
- AWS_SECRET_ACCESS_KEY
- AWS_REGION
- AWS_ACCOUNT_ID
- Push code → GitHub Actions triggers pipeline
- Image is built & pushed to ECR
- EC2 pulls latest image and runs container
#  GitHub Secrets Configuration

## Add the following secrets in your repository:

- AWS_ACCESS_KEY_ID
- AWS_SECRET_ACCESS_KEY
- AWS_REGION
- AWS_ACCOUNT_ID
