# 🏏 IPL Final Score Predictor

An interactive web app built with **Streamlit** that predicts the **final score** of an IPL innings based on live match data. The model uses historical IPL data and machine learning to forecast the final total during the first innings.

---

## 🔍 Project Overview

This project uses IPL data from **2008 to 2024** and applies feature engineering and regression modeling to predict the final score during the match. It takes into account:

- Current match status
- Last 5 overs performance
- Wickets lost
- Venue
- Playing teams

---

## 🚀 App Features

- ✅ User-friendly Streamlit interface
- ✅ Real-time prediction as match progresses
- ✅ Input last 5 overs performance
- ✅ Uses **Random Forest Regressor**
- ✅ Final score prediction with good accuracy

---

## 📸 App Screenshot

![App Screenshot](Screenshots\App.png)

---

## 📁 File Structure

```

ipl-score-predictor/
│
├── app.py                  # Streamlit web app
├── requirements.txt        # Python dependencies
├── Untitled1.ipynb         # Jupyter notebook (model training)
├── Dataset.zip             # Zipped dataset (matches.csv + deliveries.csv)
├── Pickle/Refer.txt        # Google Drive link to the model (.pkl)
├── Screenshots/            # Screenshots of running app and folder struture
└── README.md               # You’re here!

````

---

## 🧠 Model Info

- **Algorithm Used:** `RandomForestRegressor`
- **Libraries:** Scikit-learn, Pandas, NumPy

---

## 🧪 Sample Inputs

Here are some examples to test:

| Current Runs | Balls Bowled | Wickets Lost | Last 5 Runs | Last 5 Wkts | Predicted Score |
|--------------|----------------|---------------|----------------|------------------|------------------|
| 80           | 60             | 3             | 42             | 2                | 177              |
| 56           | 70             | 5             | 31             | 3                | 138              |
| 94           | 66             | 2             | 47             | 1                | 175              |

---

## 📸 Local Folder Structure

![Folder Structure](Screenshots\Folder.png)


---

## 📦 Installation

### Step 1: Clone the repo

```bash
git clone https://github.com/your-username/ipl-score-predictor.git
cd ipl-score-predictor
````

### Step 2: Create virtual environment

```bash
python -m venv venv
On Windows: venv\Scripts\activate
```

### Step 3: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Download Pickle File

🔗 [Download score\_predictor.pkl from Google Drive](https://drive.google.com/file/d/1sPW9aq5Tuwrww_J_cy7vCKzFuE2QlbBh/view?usp=drive_link)


```

### Step 5: Run the app

```bash
streamlit run app.py
```

---
## 👤 Author

**Omkar Abhaykumar Patil**
📧 [patilomkar0307@gmail.com.com](mailto:patilomkar0307@gmail.com)
🔗 [GitHub](https://github.com/omkarpatil2004)
🔗 [LinkedIn](https://www.linkedin.com/in/omkar-patil-6a2275263?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app))

---
