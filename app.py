import streamlit as st
import requests

# -----------------------------
# Configuration
# -----------------------------
API_URL = "http://127.0.0.1:8000/query"

TENANTS = {
    "Client A": "tenantA_key",
    "Client B": "tenantB_key",
}

# UI
st.set_page_config(page_title="Multi-tenant RAG Demo", layout="centered")

st.title("📄 Multi-tenant Document Search")
st.write("Simple dashboard to query documents per client.")

# Select client (tenant)
client_name = st.selectbox(
    "Select client",
    options=list(TENANTS.keys())
)

# Question input
question = st.text_input("Enter your question")

# Submit button
if st.button("Search"):
    if not question.strip():
        st.warning("Please enter a question.")
    else:
        # Prepare request
        headers = {
            "X-API-KEY": TENANTS[client_name],
            "Content-Type": "application/json"
        }
        payload = {
            "question": question
        }

        # Call backend
        try:
            response = requests.post(API_URL, json=payload, headers=headers)
            response.raise_for_status()
            data = response.json()
        except Exception as e:
            st.error(f"Backend error: {e}")
            st.stop()

        # -----------------------------
        # Display result
        # -----------------------------
        if data["no_answer"]:
            st.warning(data.get("reason", "No answer available."))
        else:
            st.subheader("Answer")
            st.write(data["answer"])

            st.subheader("Sources")
            for src in data["sources"]:
                st.markdown(f"**{src['filename']}**")
                st.caption(src["snippet"])
