


# --- Step 1: Prepare the data ---
# This cell builds `faq_text` and `lines` (list of chunks). 
# If you already have a `faq.txt` or variable `faq_text`, it will use that; otherwise it uses a small example.


import os
import re
from textwrap import dedent

# Try to load a local faq file if it exists
faq_path = "faq.txt"
if os.path.exists(faq_path):
    with open(faq_path, "r", encoding="utf-8") as f:
        faq_text = f.read()
else:
    faq_text = dedent("""
    Q: What are the library opening hours?
    A: The library is open Monday-Friday 8am-10pm, Saturday-Sunday 9am-6pm.

    Q: How do I register for classes?
    A: Use the student portal: register under "Course Enrollment" before the deadline.

    Q: Where is the student services office?
    A: Student Services is in the Student Union building, room 101.
    """)

# ✅ Improved chunking: separate each Q&A block (Q# + A#)
pattern = r"(Q\d+:.*?(?:A\d+:.*?))(?=Q\d+:|$)"  # matches Q–A pairs
matches = re.findall(pattern, faq_text, flags=re.DOTALL)

# Clean up each match
lines = [m.strip().replace("\n", " ") for m in matches]

print(f"Loaded {len(lines)} FAQ chunks.")
# print("Example chunk:", lines[0][:200])




# lines = [line.strip() for line in faq_text.split("\n") if line.strip()]
lines = [line.strip() for line in faq_text.split("\n") if line.strip().startswith("Q")]
lines_with_answers = []
splitfaq = [l.strip() for l in faq_text.split('\n') if l.strip()]
for i in range(len(splitfaq)):
    if splitfaq[i].startswith("Q") and i+1 < len(splitfaq) and splitfaq[i+1].startswith("A"):
        lines_with_answers.append(f"{splitfaq[i]} {splitfaq[i+1]}")
lines = lines_with_answers


# --- Step 3: Create Embeddings ---
# Make sure sentence-transformers is installed (you have earlier pip cell).
from sentence_transformers import SentenceTransformer
import numpy as np

# Choose a lightweight model (fast, good for RAG demos)
model_name = "all-MiniLM-L6-v2"
print("Loading embedding model:", model_name)
model = SentenceTransformer(model_name)

# Create embeddings for each chunk in `lines`
# Make sure lines exists (from Step 1)
if 'lines' not in globals():
    raise RuntimeError("`lines` is not defined. Run the data-prep cell first.")

embeddings = model.encode(lines, show_progress_bar=True, convert_to_numpy=True)
print("Embeddings shape:", embeddings.shape)



# import faiss
# import numpy as np

# dimension = embeddings.shape[1]
# index = faiss.IndexFlatL2(dimension)
# index.add(np.array(embeddings))



# --- Step 4: Build the FAISS Index ---
import faiss
import numpy as np

# Confirm embeddings variable exists
if 'embeddings' not in globals():
    raise RuntimeError("`embeddings` not defined. Run the embedding creation cell first.")

dimension = embeddings.shape[1]

# Build a simple L2 index for demo (IndexFlatL2). For larger data consider IndexIVFFlat or HNSW.
index = faiss.IndexFlatL2(dimension)

# Add embeddings to index (FAISS expects float32)
emb_np = np.array(embeddings).astype('float32')
index.add(emb_np)
print("FAISS index: n_vectors =", index.ntotal, "dimension =", dimension)

# Optional: keep a mapping from index number to the original text chunk (we already have `lines`)
# lines[i] -> embedding i







# --- Step 5: Query the FAISS index (fixed for single-line Q&A) ---
import re
import numpy as np

def answer_question(question, top_k):
    if not question or question.strip() == "":
        return "Please ask a non-empty question."
    
    # Encode question
    q_emb = model.encode([question], convert_to_numpy=True).astype('float32')
    
    # Search top matches
    D, I = index.search(q_emb, k=top_k)
    results = []
    for dist, idx in zip(D[0], I[0]):
        if idx == -1:
            continue
        results.append({"idx": int(idx), "score": float(dist), "text": lines[int(idx)]})
    
    if not results:
        return "I couldn't find a relevant answer in the FAQ."
    
    # ✅ Extract the answer text (even if Q and A are on same line)
    top = results[0]
    text = top["text"]

    # Updated regex: captures everything after A#:
    match = re.search(r"A\d*:\s*(.*)", text, re.IGNORECASE | re.DOTALL)
    if match:
        answer = match.group(1).strip()
    else:
        # fallback: try to split by 'A:' directly
        parts = re.split(r"A\d*:", text, maxsplit=1, flags=re.IGNORECASE)
        answer = parts[1].strip() if len(parts) > 1 else text.strip()
    
    resp = f"Answer: {answer}\n\n(Source: {text.splitlines()[0]})"
    return resp

# Quick test
print(answer_question("What should you do when a customer complains?", top_k=2))





import streamlit as st

# Page config for wide layout and title
st.set_page_config(page_title="Campus FAQ Chatbot", layout="wide")

# Custom title with emoji and bigger font
st.markdown("<h1 style='text-align: center; color: cyan;'>🤖 Campus FAQ Chatbot</h1>", unsafe_allow_html=True)

st.write("")  # Spacer

# Centered input using columns
col1, col2, col3 = st.columns([1,2,1])
with col2:
    st.markdown("#### Ask your question:")
    user_question = st.text_input("", key="question_box")

    if user_question:
        q_emb = model.encode([user_question])
        D, I = index.search(np.array(q_emb), k=1)
        text = lines[I[0][0]]
        import re
        match = re.search(r"A\d*:\s*(.*)", text, re.IGNORECASE | re.DOTALL)
        answer = match.group(1).strip() if match else text
        st.success(f"**Answer:** {answer}")


