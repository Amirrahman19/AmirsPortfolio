
# Translation Program: Text input and Translation System Based on Deep Learning Models  

This is an end to end LLM project based on Semantic Search and Sentence Transformers. We are building a Translation System with higher accuracy

## Project Highlights

- Input English, Indonesian or Chinese (Traditional) text and choose target language to translate to
- Anyone can use this platform for higher accuracy
- We will build an LLM based translation system that can reduce the workload of human staff.
- Customers should be able to use this system to conveniently get translated text quickly.
- Number of languages to be translated to can be adjusted by including the required deep learning model into the current project code structure and integrating the UI with the DL logic smoothly

## You will learn following,
  - Semantic Search + Sentence Transformers: LLM based Translation
  - Streamlit: UI
  - Huggingface instructor embeddings: Text embeddings

## Installation

1.Clone this repository to your local machine using:

```bash
  git clone git@gitlab.com:cgl-digitalmarketing/faq_nlp_searchengine.git
```
2.Navigate to the project directory:

```bash
  cd 'internship'
```
3. Install the required dependencies using pip:

```bash
  pip install -r requirements.txt
```

5. Switch to 'translationproj' branch
```bash
  git checkout translationproj  
```
## Usage

1. Run the Streamlit app by executing:
```bash
streamlit run main.py

```

2.The web app will open in your browser.

- Simply input text and select target language for translation and click 'Translate'
- Wait while the program runs and the output will pop out below.


## Project Structure

- main.py: The main Streamlit application script.
- langchain_helper.py: This has all the langchain code
- requirements.txt: A list of required Python packages for the project.