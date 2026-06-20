# API Demo Deployment

A Simple FastAPI Project that Provides Demo User SignUp Data for Testing, Learning, Frontend Development, and API Integration Practice.

## Live Deployments

[![Vercel](https://img.shields.io/badge/Vercel-Live-black?logo=vercel)](https://api-demo-deployment.vercel.app)

[![Render](https://img.shields.io/badge/Render-Live-brown?logo=render)](https://api-demo-deployment.onrender.com)

---

## Base URLs

### Vercel

```text
https://api-demo-deployment.vercel.app
```

### Render

```text
https://api-demo-deployment.onrender.com
```

---

## Routes

### Health Check

```http
GET /
```

Returns API status information.

#### Example Response

```json
{
  "success": true,
  "message": "Connection Successful!"
}
```

---

### Get Demo SignUp Users

```http
GET /sign-up-data
```

Returns all available demo user records.

#### Example Response

```json
{
  "success": true,
  "message": "Data Successfully Retrieved",
  "total_users": 1,
  "users_data": [
    {
      "username": "demo_user",
      "name": "Demo User",
      "country": "India",
      "email": "demo@example.com",
      "password": "demo123",
      "phone": "9876543210"
    }
  ]
}
```

---

## API Documentation

### Swagger UI

```text
https://api-demo-deployment.vercel.app/docs
```

### Render

```text
https://api-demo-deployment.onrender.com/docs
```

---

## Run Locally

### Clone Repository

```bash
git clone https://github.com/TanishkBhatt/API-Demo-Deployment.git
```

### Navigate to Project

```bash
cd API-Demo-Deployment
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Start Server

```bash
uvicorn main:app --reload
```

Server will start at:

```text
http://127.0.0.1:8000
```

---

## Author

Tanishk Bhatt - A Student And A Programmer. 

---
