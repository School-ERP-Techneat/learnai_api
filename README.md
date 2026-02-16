# Flask + MongoDB + JWT API

A modular **Flask REST API** featuring **JWT authentication**, **MongoDB Atlas integration**, **video upload**, and **user progress tracking**.  
Designed for scalability and easy extension.

---

## 🚀 Features

- User Signup & Login (JWT-based authentication)
- Secure API routes with JWT protection
- MongoDB Atlas integration
- Video upload support
- User learning progress tracking
- Modular and clean project structure

---

## 📂 Project Structure

project/
│── app.py                # Main entry point
│── config.py             # Configuration (loads .env)
│── extensions.py         # Mongo + JWT setup
│── models.py             # Helper functions for MongoDB
│── routes/
│   ├── auth.py           # Signup & login routes
│   ├── video.py          # Video upload routes
│   ├── progress.py       # Progress tracking routes
│── uploads/              # Uploaded video files
│── .env                  # Environment variables
│── requirements.txt


---

## ⚙️ Setup

### 1. Clone & Install
```bash
git clone <repo-url>
cd project
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

Create a .env file in the project root:
SECRET_KEY=super_secret_key_here
JWT_SECRET_KEY=super_jwt_secret_here
MONGO_URI=mongodb+srv://<username>:<password>@cluster0.mongodb.net/flask_api?retryWrites=true&w=majority
UPLOAD_FOLDER=uploads

Run the App
python app.py
Server runs at: http://127.0.0.1:5000/

🔑 API Routes
Auth
POST /auth/signup

json
{
  "username": "ankit",
  "email": "ankit@example.com",
  "password": "mypassword"
}
→ {"message": "Signup successful"}

POST /auth/login

json
{
  "email": "ankit@example.com",
  "password": "mypassword"
}
→ {"access_token": "JWT_TOKEN"}

Video
POST /video/upload

Headers: Authorization: Bearer <JWT_TOKEN>

Body: form-data → key=video, type=File, value=sample.mp4

Response:

json
{"message": "Video uploaded", "progress": 33}
Progress
GET /progress/

Headers: Authorization: Bearer <JWT_TOKEN>

Response:

json
{"progress": 33}
🛠️ Debugging
Ensure MongoDB Atlas URI includes a database name (/flask_api).

Whitelist your IP in Atlas.

Use fresh JWT tokens after restarting the app.

🚀 Next Steps
Add refresh tokens for JWT expiration handling.

Store video metadata (filename, upload time, user ID).

Add file type validation for uploads.

📜 License
MIT

---

This README is ready to drop into your project root. It explains **setup, environment, running, and API usage** in Markdown format.  

👉 Do you want me to also generate a **Postman collection JSON file** so you can import all routes directly into Postman without manual setup?



