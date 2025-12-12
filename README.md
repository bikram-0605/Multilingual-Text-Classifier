🌍 Multilingual Text Classifier

A Streamlit web application that translates text from any supported language to English using Helsinki-NLP MarianMT models and classifies the translated text using BART MNLI zero-shot classification. The app predicts intents such as spam, question, opinion, complaint, and request.

🚀 Features

Translate text from multiple languages → English

Zero-shot classification using BART MNLI

Clean and simple Streamlit UI

Fast performance with model caching

```
📁 Project Structure
├──app.py                # Main Streamlit application
├──translator.ipynb      # Notebook used for testing and experiments
├──requirements.txt      # Dependencies
├──README.md             # Project documentation
├──.gitignore
```




⚙️ Installation
1. Clone the repository
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>

2. Create & activate virtual environment
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate

3. Install dependencies
pip install -r requirements.txt

4. Run the app
streamlit run app.py

🧠 How It Works

User enters text + language code (e.g., hi, fr, es)

App loads the MarianMT model for translation

Translated English text is passed to BART MNLI classifier

App returns:

Translated text

Predicted label

Confidence scores

📌 Example

Input:
"मुझे अपने ऑर्डर के बारे में शिकायत है" (hi)

Output:

Translation: "I have a complaint about my order"

Label: complaint

📦 Deployment

You can deploy the app directly to Streamlit Cloud by connecting this repo.
