# Sentiment Analysis API (ML Based)

This project is a Machine Learning–based backend API that analyzes text input
and predicts whether the sentiment is **Positive**, **Negative**, or **Neutral**,
along with a confidence score.

---

## 🚀 What This Project Does

- Accepts raw text as input
- Uses a trained Machine Learning model to analyze sentiment
- Returns sentiment label with a confidence score
- Exposes the model via a REST API using FastAPI

This API can be integrated with websites, mobile apps, or other backend services.

---

## 🧠 Tech Stack

- Python
- FastAPI
- scikit-learn
- Naive Bayes Classifier
- REST API
- Swagger UI

---

## 📁 Project Structure

sentiment-api/
├── app/
│ └── main.py
├── trainmodel.py
├── sentimentmodel.pkl
├── requirements.txt
└── README.md


---

## ⚙️ How It Works

1. A Machine Learning model is trained using labeled text data
2. The trained model is saved as a `.pkl` file
3. FastAPI loads the model when the server starts
4. Incoming text is analyzed via a POST API endpoint
5. The API returns sentiment and confidence score as JSON

---

## 🔧 Setup Instructions

### 1️⃣ Install dependencies
```bash
pip install -r requirements.txt


```md
 2️⃣ Train the model
```bash
python trainmodel.py

3️⃣ Run the API server

uvicorn app.main:app --reload

---

## 📌 API Usage

Once the server is running, open the interactive API documentation:

http://127.0.0.1:8000/docs


This opens **Swagger UI**, where you can test the API directly from the browser.

---

## 🔁 Sentiment Analysis Endpoint

**Endpoint**


**Request Body (JSON)**
```json
{
  "text": "This service was amazing and fast"
}

🌍 Live Deployment

This API is live and publicly accessible, deployed on Render.

Base URL:

https://sentiment-api-it1p.onrender.com/docs
  "sentiment": "Positive",
  "confidence_score": 0.63
}

