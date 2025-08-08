# 🌍 Climate Change Sentiment Analysis

This project focuses on analyzing the **sentiments** (positive, negative, or neutral) in public **Facebook comments** related to climate change. It includes data preprocessing, model training, evaluation, and a simple web app to predict sentiment from new comments.

---

## 🧠 Project Goals

- Classify comments into: `Positive`, `Negative`, or `Neutral`
- Use machine learning models to compare their performance
- Build and deploy an interactive **Streamlit web app**
- Save and reuse the best model for real-time predictions

---

## 📁 Project Structure

```
Climate_Change_Modeling/
│
├── app.py                          # Streamlit web application
├── sentiment_model.py             # Model training and evaluation
├── data/
│   └── climate_comments.csv       # Cleaned dataset
├── saved_models/
│   ├── best_sentiment_model.pkl   # Best performing model
│   └── tfidf_vectorizer.pkl       # Vectorizer for transforming text
├── notebooks/
│   └── EDA_and_Modeling.ipynb     # Exploratory Data Analysis and training
├── requirements.txt               # Python libraries needed
└── README.md                      # Project documentation (this file)
```

---

## 📊 Machine Learning Models Used

We tested and compared the following models:

| Model                | Accuracy |
|---------------------|----------|
| Logistic Regression | 89.77%   |
| Random Forest       | 86.20%   |
| XGBoost             | 84.66%   |
| Naive Bayes         | 84.09%   |

✅ **Best Model**: Logistic Regression (saved as `.pkl`)

---

## 📌 Features

- Text preprocessing (cleaning, tokenization)
- TF-IDF vectorization
- Multiple ML models trained
- Confusion matrix and classification report
- Interactive app to test your own sentences

---

## 🚀 How to Run the Project

### ✅ 1. Install Requirements

```bash
pip install -r requirements.txt
```

### ✅ 2. Run the App

```bash
streamlit run app.py
```

---

## 🧪 Example Input & Output

**Input:**  
> *"The weather is very amazing today, there are no clouds and the sky is clear."*

**Output:**  
> **Predicted Sentiment:** Neutral  
> **Confidence:** 44.99%  
>  
> 🔍 Class Probabilities:  
> - Negative: 15.74%  
> - Neutral: 44.99%  
> - Positive: 39.26%

---

## 🔐 .gitignore Setup

To keep the repo clean, make sure you ignore:

```
venv/
*.pkl
*.egg-info/
__pycache__/
.DS_Store
```

---

## 👩‍💻 Author

**Iqra Shaikh**  
[GitHub Profile](https://github.com/Iqra-Shaikh1503)

---

## 📌 Future Improvements

- Add LSTM / Transformer models for deep learning
- Train on larger datasets
- Deploy with Docker or Hugging Face Spaces

---

## 🙌 Special Thanks

- [Scikit-learn](https://scikit-learn.org/)
- [XGBoost](https://xgboost.ai/)
- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org/)
- [Matplotlib](https://matplotlib.org/)
