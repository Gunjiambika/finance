# 💰 Finance Dashboard — Backend Project

A backend-focused finance dashboard system built using FastAPI with role-based access control, analytics APIs, and frontend integration.

---

## 🚀 Live Demo

🔗 https://finance-9zlg.onrender.com

---

## ✨ Features

✅ Role-based access control (Admin, Analyst, Viewer)  
✅ Financial records management (income & expense)  
✅ Dashboard analytics APIs  
✅ Category-wise aggregation  
✅ Monthly trends analysis  
✅ Graph visualization using Chart.js  
✅ Input validation and error handling  
✅ Simple frontend UI for API interaction  

---

## 🔐 Roles & Permissions

| Action | Viewer | Analyst | Admin |
|--------|--------|---------|-------|
| View records | ✅ | ✅ | ✅ |
| Add records | ❌ | ❌ | ✅ |
| View analytics | ❌ | ✅ | ✅ |
| Manage users | ❌ | ❌ | ✅ |

---

## 📊 Dashboard Analytics

### 🔹 Summary API
- Total income  
- Total expense  
- Net balance  

### 🔹 Category-wise Breakdown
- Group data by category  

### 🔹 Trends
- Monthly financial trends  

---

## 📡 API Endpoints

### 👤 Users

| Method | Route | Description |
|--------|------|-------------|
| POST | /users | Create user |

---

### 💸 Records

| Method | Route | Description |
|--------|------|-------------|
| POST | /records/{user_id} | Add record |
| GET | /records/{user_id} | Get records |

---

### 📊 Analytics

| Method | Route | Description |
|--------|------|-------------|
| GET | /summary/{user_id} | Summary |
| GET | /summary/category/{user_id} | Category breakdown |
| GET | /summary/trends/{user_id} | Monthly trends |

---

## 📊 Example Outputs

### 🔹 Summary

``` json
{
  "total_income": 1000,
  "total_expense": 300,
  "balance": 700
}
```

### 🔹 Category Breakdown

``` json
{
  "salary": 1000,
  "food": 200,
  "travel": 100
}
```

### 🔹 Monthly Trends

``` json
{
  "2026-04": 1300,
  "2026-05": 2000
}
```

------------------------------------------------------------------------

## 📂 Project Structure

```bash
finance-backend/
│
├── main.py
├── models.py
├── service.py
├── auth.py
├── requirements.txt
│
├── templates/
│ └── index.html
│
├── static/
│ ├── script.js
│ └── style.css
```

------------------------------------------------------------------------

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

git clone https://github.com/Gunjiambika/finance.git cd finance

### 2️⃣ Install Dependencies

pip install fastapi uvicorn

### 3️⃣ Run Server

uvicorn main:app --reload

### 4️⃣ Open Browser

http://127.0.0.1:8000

------------------------------------------------------------------------

## 📊 Dashboard Analytics Explained

-   Summary → income, expense, balance
-   Category → grouped data
-   Trends → monthly analysis

------------------------------------------------------------------------

## 🧠 Key Concepts

-   REST API design
-   Role-based access control (RBAC)
-   Data aggregation
-   Error handling
-   Frontend-backend integration

------------------------------------------------------------------------

## 🚀 Why This Project Stands Out

-   Clean backend structure
-   Real-world analytics
-   Role-based security
-   Graph visualization
-   Live deployed

------------------------------------------------------------------------

## 🛠 Tech Stack

-   FastAPI
-   HTML, CSS, JS
-   Chart.js
-   GitHub
-   Render

------------------------------------------------------------------------

## 👩‍💻 Author

Ambika Gunji
B.Tech (IoT) | Backend Developer
