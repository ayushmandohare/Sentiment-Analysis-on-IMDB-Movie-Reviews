# 📝 Sentiment Analysis on Reviews (SVM Model)

A machine learning project that performs **binary sentiment classification** (Positive / Negative) on text reviews using **TF-IDF Vectorization** and a **Support Vector Machine (SVM)** classifier.  
The project includes a deployed **Streamlit web app** where users can test the model in real time.

---

## 🚀 Features
- Preprocessing of text reviews
- Balanced dataset handling
- TF-IDF vectorization
- Trained **SVM classifier**
- Interactive **Streamlit app** for prediction
- Exported model as `.pkl` files for reusability

---

## 🛠️ Tech Stack
- Python
- Scikit-learn
- Pandas & Numpy
- Streamlit

---

## 📂 Project Structure
├── app.py # Streamlit web app

├── sentiment_svm_model.pkl # Trained SVM model

├── tfidf_vectorizer.pkl # TF-IDF vectorizer

├── requirements.txt # Dependencies

└── README.md # Project documentation

---

## ⚡ How to Run Locally
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/sentiment-analysis-svm.git
   cd sentiment-analysis-svm

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   
4. Run the Streamlit app:
   ```bash
   streamlit run app.py

6. Open your browser and go to:
   ```bash
   http://localhost:8501
   
---    

## 🖼️ Demo Screenshot
<img width="1916" height="848" alt="Image" src="https://github.com/user-attachments/assets/de68b8a7-6f51-4629-9258-44fd967229fe" />

---

## ✨ Future Improvements
- Add more datasets for training
- Experiment with deep learning models (LSTM, BERT)
- Multi-class sentiment (positive, negative, neutral)
