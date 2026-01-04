# Campus FAQ Chatbot with RAG

An intelligent, production-ready Streamlit web application that answers campus and business FAQs using Retrieval-Augmented Generation (RAG) and semantic vector search. Built for scalability, ease of use, and customization.

---

## ✨ Features

- **Custom FAQ Upload** – Import your own FAQ documents (`.txt` format with Q&A pairs) without code changes
- **Natural Language Understanding** – Ask questions in your own words and receive contextually relevant answers
- **Vector-Based Retrieval** – Fast semantic search using transformer embeddings and FAISS indexing
- **Modern UI/UX** – Dark mode support with a clean, intuitive Streamlit interface
- **Production-Ready** – Minimal dependencies, straightforward setup, and easy deployment
- **Fully Customizable** – Swap embedding models, adjust styling, and extend functionality with ease

---

## 🎯 Demo

![Campus FAQ Chatbot Interface](https://github.com/user-attachments/assets/df52d8eb-2c4a-4029-a676-2fe15a0b7ec5)

*Type a question → Get instant, contextually relevant answers from your FAQ database*

---

## 🔍 How It Works

### Architecture

1. **Vector Embedding** – Each Q&A pair is converted into semantic embeddings using a pre-trained transformer model (Sentence Transformers)
2. **FAISS Indexing** – Embeddings are indexed in FAISS for O(1) similarity search across large FAQ datasets
3. **Semantic Retrieval** – User queries are embedded and matched against the FAQ index to find the most relevant answers
4. **Streamlit UI** – Clean, interactive interface for uploading FAQs and querying the system in real-time

### Technical Stack

- **Frontend:** Streamlit
- **Embeddings:** Sentence Transformers (`all-MiniLM-L6-v2`)
- **Vector Store:** FAISS
- **Language:** Python 3.8+

---

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- pip or conda

### Setup

```bash
# Clone the repository
git clone https://github.com/Jenishbhai-dev/Rag_bot.git
cd Rag_bot

# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run app.py
```

The app will be available at `http://localhost:8501` by default.

---

## 📄 FAQ Format

Your FAQ document should be in plain text format with alternating question-answer pairs:

```
Q1: What is office timing?
A1: Monday to Friday, 9am-5pm.

Q2: How do I reset my password?
A2: Visit the online portal and follow the reset instructions.

Q3: What are the contact hours for support?
A3: Support is available Monday–Friday, 9am–5pm EST.
```

**Format Requirements:**
- Each question line starts with `Q#:` followed by the question text
- Each answer line starts with `A#:` followed by the answer text
- Questions and answers must be numbered sequentially
- Use a blank line between Q&A pairs for readability

See `faq.txt` in the repository for a complete template.

---

## ⚙️ Customization

### Using Different Embedding Models

Modify the embedding model in `app.py`:

```python
from sentence_transformers import SentenceTransformer

# Default (fast, lightweight)
model = SentenceTransformer('all-MiniLM-L6-v2')

# Alternative (higher quality)
model = SentenceTransformer('all-mpnet-base-v2')
```

### Theming and Styling

Customize the Streamlit interface by updating `app.py`:

```python
st.set_page_config(
    page_title="Campus FAQ Chatbot",
    layout="wide",
    initial_sidebar_state="expanded"
)
```

### Adding New Features

The modular structure makes it easy to extend functionality:
- Add conversation history tracking
- Implement multi-language support
- Integrate feedback mechanisms
- Add admin panels for FAQ management

---

## 🎓 Use Cases

- **Campus Support** – Answer student questions about enrollment, facilities, and policies
- **Customer Service** – Deploy as an internal knowledge base for support teams
- **Tech Support** – Build troubleshooting guides and technical FAQ systems
- **Onboarding** – Create interactive orientation bots for new employees or students
- **Knowledge Bases** – Organize and serve documentation intelligently

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. **Report Issues** – Open an issue on GitHub with a clear description of the bug or feature request
2. **Submit Changes** – Fork the repository, create a feature branch, and submit a pull request
3. **Code Standards** – Follow PEP 8 conventions and include docstrings for new functions

```bash
# Typical workflow
git checkout -b feature/your-feature-name
# Make changes
git commit -m "Add your descriptive commit message"
git push origin feature/your-feature-name
# Open a pull request
```

---

## 📧 Contact & Support

**Developer:** Jenishbhai

For questions, suggestions, or collaboration opportunities:
- Open an issue on [GitHub](https://github.com/Jenishbhai-dev/Rag_bot)
- Reach out via email or direct message

---

## 🚀 Quick Start

```bash
git clone https://github.com/Jenishbhai-dev/Rag_bot.git
cd Rag_bot
pip install -r requirements.txt
streamlit run app.py
```

Upload your FAQ file, ask a question, and get instant answers!

---

**Made with ❤️ by Jenishbhai**

