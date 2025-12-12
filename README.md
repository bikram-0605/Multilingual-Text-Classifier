# 🌍 Multilingual Text Classifier Using Translation + Zero-Shot Learning

## 🧾 Detailed Project Description

This project implements a multilingual text classification system that combines machine translation with zero-shot learning to analyze text written in any language. The app first translates the input text to English using **Helsinki-NLP MarianMT models**, and then uses **Facebook BART MNLI** to classify the translated text into one of several categories, such as **spam**, **question**, **complaint**, **request**, or **opinion**. The entire system is deployed using a simple and interactive **Streamlit** web interface.

## 💡 Motivation

Language diversity makes automated text classification difficult. Most NLP models are trained only on English text. This project solves that challenge by automatically translating any language to English and then performing intent classification. It demonstrates a practical and powerful multilingual NLP pipeline suitable for applications like chatbots, customer service automation, and social media analysis.

## 🔧 System Workflow

1. User enters text in any language  
2. User specifies the source language code (e.g., `hi`, `fr`, `es`, `de`)  
3. App loads corresponding MarianMT translation model  
4. Text is translated into English  
5. BART MNLI classifier predicts the text’s intent  
6. Output includes:  
   - Translated text  
   - Predicted label  
   - Confidence scores  

## ✨ Features

- 🌐 **Multilingual Input Support**  
- 🔄 **Automatic Translation to English**  
- 🎯 **Zero-Shot Classification**  
- ⚡ **Fast Inference with Model Caching**  
- 🖥️ **Streamlit-Based Web Interface**  
- 📊 **Clean Output with Predicted Labels + Scores**  

## 📁 Project Structure

```
multilingual-text-classifier/
├── app.py                # Main Streamlit application
├── translator.ipynb      # Notebook for testing and experiments
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
└── .gitignore            # Files ignored by Git
```

## 🚀 Installation & Usage

### 1️⃣ Clone the Repository
```
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
```

### 2️⃣ Install Dependencies
```
pip install -r requirements.txt
```

### 3️⃣ Run the Application
```
streamlit run app.py
```

## 📦 Deployment

Deploy easily on **Streamlit Cloud**:

1. Push repository to GitHub  
2. Go to https://share.streamlit.io  
3. Select your repo  
4. Deploy  

## ⚠️ Notes & Limitations

- Translation models must support the selected language pair  
- First model load may take a few seconds  
- Zero-shot classification is limited to predefined labels  

