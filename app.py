import streamlit as st
from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.vectorstores import Chroma
from gtts import gTTS
import os
from transformers import GPT2LMHeadModel, GPT2Tokenizer
from IPython.display import Audio, display

# Load and initialize documents
@st.cache_resource
def initialize_db(directory):
    loader = DirectoryLoader(directory)
    documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=100000, chunk_overlap=200)
    docs = text_splitter.split_documents(documents)
    embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
    db = Chroma.from_documents(docs, embeddings)
    return db


# Text-to-speech
def speak_text(text, output_file="output.mp3"):
    try:
        # Generate the audio file
        tts = gTTS(text)
        tts.save(output_file)

        # Play the audio file in Colab
        display(Audio(output_file, autoplay=True))
    except Exception as e:
        st.error(f"Error in text-to-speech: {e}")

# Ingredient substitution using GPT-2
def suggest_alternative(ingredient):
    try:
        tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
        model = GPT2LMHeadModel.from_pretrained("gpt2")

        input_text = f"{ingredient} alternatives:"
        inputs = tokenizer.encode(input_text, return_tensors="pt")

        outputs = model.generate(inputs, max_length=50, num_return_sequences=1)
        suggestion = tokenizer.decode(outputs[0], skip_special_tokens=True)
        print()
        return suggestion
    except Exception as e:
        st.error(f"Error generating alternative: {e}")
        return "No alternative found"

# Streamlit app
def main():
    st.title("Recipe Finder and Ingredient Substitution")
    # Recipe search
    query = st.text_input("Enter a dish name to find its recipe:", "")
    if st.button("Find Recipe"):
        try:
            directory = '/content/sample_data/reci'  # Replace with your recipe directory path
            db = initialize_db(directory)
            matching_docs = db.similarity_search(query)
            recipe = matching_docs[0].page_content
            st.text_area("Recipe:", recipe, height=200)
            if st.button("Speak Recipe"):
              recipe = matching_docs[0].page_content
              speak_text(recipe)
            else:
                st.warning("No matching recipes found.")
        except Exception as e:
            st.error(f"Error searching for recipe: {e}")

    # Ingredient substitution
    ingredient = st.text_input("Enter an ingredient to find an alternative:", "")
    if st.button("Suggest Alternative"):
        alternative = suggest_alternative(ingredient)
        st.write(f"Suggested Alternative: {alternative}")

if __name__ == "__main__":
    main()
