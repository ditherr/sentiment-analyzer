<h1 align="center"><a href="https://sentyzer.streamlit.app/">🕵️SentyZer</a></h1>
<h3 align="center">|</h4>

## 🚀 About SentyZer
SentyZer is a Web-app Sentiment Analyzer that allows users to input single or multiple inputs into the LLM model. And analyzer will classified the inputs into positive or negative.

### 🔧 How does it work?
<p>
This is an Implementation of the LLM model that is built with Streamlit and it encapsulates a comprehensive Python environment that includes all necessary libraries. The WebApp can predict the sentiment of the input text.
</p>

### ⚠️ **Update**
This application runs according to its function, but in the future there will be updates in the form of:
- Pre-trained LLM model
- Push pretrained model to Hugging Face Hub
- Specify trained model by using [Amazon Reviews](https://huggingface.co/datasets/McAuley-Lab/Amazon-Reviews-2023) dataset.
- ...

## ⚙️Requirements & Installation
- `Requirements`, you need to have a **Hugging Face account** to push the pretrained model.
- `Installation`, the packages and libraries required in the `requirements.txt` file.
    - ⚠️ in the requirements.txt file, there are `'transformers[torch]'`, because this project running on CPU (local) so we need to installed one of the PyTorch or TensorFlow 2.0 (in this case using PyTorch). But still you can install separately (e.g. `tensorflow==2.x.x`, `transformers==4.x.x`, etc.)

### ⚙️Interact with the Project
1. **Clone the repository**
    ```
    git clone https://github.com/ditherr/sentyzer.git
    ````
2. Navigate to the repository
3. **Create and Activate Environment**
    ```
    conda create -p venv python==3.10.12 -y
    conda activate venv/
    ```
4. **Install The Requirements**
    ```
    pip install -r requirements.txt
    ```
5. **Run the Application**
    ```
    streamlit run sentyzer.py
    ```