import streamlit as st
from transformers import MarianMTModel, MarianTokenizer, pipeline
import torch

# Translation setup
@st.cache_resource
def load_translation_model(model_name):
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)
    return tokenizer, model

def translate(text, src_lang):
    model_name = f"Helsinki-NLP/opus-mt-{src_lang}-en"
    tokenizer, model = load_translation_model(model_name)
    tokenized = tokenizer(text, return_tensors="pt", padding=True)
    translated = model.generate(**tokenized)
    return tokenizer.decode(translated[0], skip_special_tokens=True)

# Classification setup
@st.cache_resource
def load_classifier():
    return pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

classifier = load_classifier()
labels = ["spam", "question", "opinion", "complaint", "request"]

# UI
st.title("🌍 Multilingual Text Classifier")
st.markdown("Translate from any language ➜ English ➜ Classify ➜ Show Prediction")

user_text = st.text_area("✍️ Enter your message in any language:")
language = st.text_input("🌐 Source Language Code (e.g., `hi`, `fr`, `es`, `de`):", value="hi")

if st.button("Analyze"):
    if user_text.strip() == "":
        st.warning("Please enter some text.")
    else:
        try:
            with st.spinner("Translating..."):
                translated = translate(user_text, language)
                st.success("Translation done ✅")
                st.write("🔤 Translated Text:", translated)

            with st.spinner("Classifying..."):
                result = classifier(translated, labels)
                st.success("Classification done ✅")
                st.write("🏷️ Predicted Label:", result['labels'][0])
                st.write("📊 Scores:", {l: f"{s:.2f}" for l, s in zip(result['labels'], result['scores'])})

        except Exception as e:
            st.error(f"Error: {str(e)}")
