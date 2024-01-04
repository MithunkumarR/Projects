#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pdfplumber

def read_pdf(file_path):
    with pdfplumber.open(file_path) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
    return text
file_path = "D://RAG//Mithunkumar Resume.pdf"
text = read_pdf(file_path)
print(text)


# In[ ]:


from sentence_transformers import SentenceTransformer
import faiss
from transformers import pipeline
import numpy as np

def create_embedding(text, model):
    embedding = model.encode([text])
    return embedding[0]

def store_in_vector_db(vector_db, vector, document_id):
    vector_db.add(np.array([vector]), np.array([document_id]))

def similarity_search(query_vector, vector_db, k=5):
    _, result_ids = vector_db.search(np.array([query_vector]), k)
    return result_ids[0]

def query_to_llm(query):
    llm = pipeline('text-generation', model='EleutherAI/gpt-neo-1.3B')
    result = llm(query)
    return result[0]['generated_text']

def display_results(results):
    for idx, document_id in enumerate(results):
        print(f"Result {idx+1}: Document ID {document_id}")

embedding_model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

d = 768 
index = faiss.IndexFlatL2(d)
document_id = 'document_1'
pdf_embedding = create_embedding(text, embedding_model)
store_in_vector_db(index, pdf_embedding, document_id)

query = "Your query goes here"
llm_result = query_to_llm(query)

query_embedding = create_embedding(llm_result, embedding_model)

search_results = similarity_search(query_embedding, index)
display_results(search_results)

