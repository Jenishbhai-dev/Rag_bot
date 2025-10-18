🤖 Campus FAQ Chatbot with RAG
An interactive Streamlit web app that answers campus or business FAQs using Retrieval-Augmented Generation and vector search.

🚀 Features
Upload your own FAQ document (faq.txt format with Q&A pairs)

Ask natural language questions and get instant contextual answers!

Built with Streamlit, Sentence Transformers, and FAISS

Modern dark mode UI, fully customizable

Fast, easy setup and use

👀 Demo
![Campus FAQ Chatbot Screenshot](
<img width="1913" height="1000" alt="Screenshot 2025-10-18 150745" src="https://github.com/user-attachments/assets/df52d8eb-2c4a-4029-a676-2fe15a0b7ec5" />

Ask your question—get smart answers instantly!

🛠️ How it Works
Vector Embedding: Each Q&A pair is embedded using a transformer model

FAISS Indexing: Vectors are indexed for fast similarity search

Streamlit UI: Clean input/output display and FAQ upload options

📦 Installation
bash
git clone https://github.com/Jenishbhai-dev/Rag_bot.git
cd Rag_bot
pip install -r requirements.txt
streamlit run app.py
📄 FAQ Format Example
text
Q1: What is office timing?
A1: Monday to Friday, 9am-5pm.

Q2: How to reset my password?
A2: Use the online portal and follow the instructions.
See faq.txt for a simple template—each question line is followed by its answer line.

✨ Customization
Use your own FAQ document with Q&A pairs

Modify app.py for themes, styles, or new features

Swap out Sentence Transformer models easily

💡 Use Cases
College campus help desk bots

Company/customer support assistants

Tech support and knowledge bases

Personal FAQ assistants or onboarding bots

🤝 Contributing
Contributions and suggestions are welcome!

Open issues for bugs or requests

Fork and submit a pull request

📝 License
MIT

📧 Contact
Made by Jenishbhai

Clone, run, ask, and impress—with your simple campus chatbot repo!
