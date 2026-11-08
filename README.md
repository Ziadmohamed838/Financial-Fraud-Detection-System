
# 💳 Financial Fraud Detection System

## 📌 Project Overview
This project focuses on detecting fraudulent credit card transactions using Machine Learning techniques.

The goal is to build a classification model that can identify suspicious transactions while addressing the highly imbalanced nature of financial transaction data.

## 📊 Dataset Description
- Dataset: Credit Card Fraud Detection (Kaggle)
- Total Transactions: 284,807
- Fraudulent Transactions: 492
- Target: Class (0 = Legitimate, 1 = Fraudulent)

## 🧹 Data Cleaning & EDA
- Data inspection and quality checks.
- Duplicate detection and handling.
- Exploratory Data Analysis (EDA).
- Analysis of class distribution.
- Understanding transaction patterns.

## ⚙️ Feature Engineering
- Log transformation for transaction Amount.
- Feature scaling using StandardScaler.
- Handling class imbalance using SMOTE.
- Preparing features for model training.

## 🤖 Machine Learning Models
The following models were explored:
- Logistic Regression
- Random Forest
- XGBoost

## 📈 Model Evaluation
Models were evaluated using metrics suitable for imbalanced classification:
- Precision
- Recall
- F1-Score
- ROC-AUC
- Precision-Recall AUC

## 🏆 Results
Best Performing Model: XGBoost

- ROC-AUC: 0.966
- PR-AUC: 0.834

## 🛠️ Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Imbalanced-learn
- XGBoost
- Jupyter Notebook

## 📁 Project Files
- `nti.finaal.ipynb` – Main Jupyter Notebook.
- `app.py` – Application source code.
- `2025-09-18 11-54-52.mp4` – Project demonstration video.

## 👨‍💻 Author
**Ziad Mohamed**

Junior Data Engineer | Data Analyst

[GitHub Profile](https://github.com/Ziadmohamed838)
