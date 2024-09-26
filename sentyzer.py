import pandas as pd
import numpy as np
import streamlit as st
import transformers
import datasets
from transformers import pipeline


# Model
model_checkpoint = "distilbert-base-uncased-finetuned-sst-2-english"
analyzer = pipeline("sentiment-analysis", model=model_checkpoint)

# Initialize session state for storing input texts
if 'texts' not in st.session_state:
    st.session_state['texts'] = []


st.set_page_config(page_title="SentyZer", page_icon="🔎")
st.title("🕵️SentyZer | Sentiment Analyzer")

cont = st.container()
with cont:
    choice = st.selectbox("Input", ['Single Input', 'Multiple Inputs'], index=None, placeholder='Choice type of inputs...')
    
    if choice == 'Single Input':
        input = st.text_input("Enter Text to Analyze", placeholder="Text to Analze")
        if st.button('Analyze'):
            result = analyzer(input)
            
            label = result[0]['label']
            score = np.round(result[0]['score'], 4)
            st.success(f"Based on your Input: *'{input}'*, it is a **{label}** with a score of **{score}**.")
                
    if choice == 'Multiple Inputs':
        input = st.text_input("Enter your text:", placeholder="Text to Analze")
        
        b1, b2, b3, b4 = st.columns([2, 2, 2, 6], gap="small")
        with b1:
            add_text = st.button('➕ Text', type="primary")
        with b2:
            analyze = st.button('🔎 Analyze')
        
        if add_text:
            if input:
                st.session_state['texts'].append(input)
            else:
                st.warning("Please enter a valid text!")
        
        # Show the added texts:
        with st.expander("👀 Show Stored Texts"):
            if st.session_state['texts']:
                st.write(st.session_state['texts'])
        
        # Analyze the texts
        if analyze:
            if st.session_state['texts']:
                results = analyzer(st.session_state['texts'])
                
                # Create a DataFrame with the results
                df = pd.DataFrame({
                    'Text': st.session_state['texts'],
                    'Label': [res['label'].lower() for res in results],
                    'Score': [res['score'] for res in results]
                })
                
                #  Display the DataFrame
                st.write("### Sentiment Results:")
                st.dataframe(df)
            else:
                st.warning("No texts to analyze!")
        
        # Optional: Button to clear the stored texts
        with b3:
            if st.button("🗑️ Texts"):
                st.session_state['texts'] = []
                with b4:
                    st.success("Cleared all texts!")