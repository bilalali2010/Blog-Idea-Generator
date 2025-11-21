import streamlit as st
import requests

st.set_page_config(page_title="Blog Idea & Blog Generator", page_icon="📝", layout="wide")

# ---------------------------------------
# CALL OPENROUTER API
# ---------------------------------------
def generate_text(prompt, api_key):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "HTTP-Referer": "http://localhost",
        "Content-Type": "application/json",
    }

    payload = {
        "model": "x-ai/grok-4.1-fast:free",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 1500,
        "temperature": 0.8
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code != 200:
        return f"⚠️ Error: {response.text}"

    return response.json()['choices'][0]['message']['content']


# ---------------------------------------
# STREAMLIT UI
# ---------------------------------------
st.title("📝 Blog Idea + Blog Generator (OpenRouter - Grok 4.1 Fast Free)")
st.write("Generate ideas or a full blog using your free OpenRouter API key.")

api_key = st.text_input("🔑 Enter your OpenRouter API Key", type="password")

topic = st.text_input("🧠 Blog Topic", placeholder="e.g., AI in Healthcare")
tone = st.selectbox("🎨 Tone", ["Professional", "Casual", "Humorous", "Inspirational", "Technical"])
audience = st.text_input("👥 Audience", placeholder="e.g., Students, Developers, Beginners")
creativity = st.slider("✨ Creativity Level", 1, 10, 5)
length = st.selectbox("✍️ Blog Length (words)", ["300", "500", "700", "1000", "1500", "2000"])

col1, col2 = st.columns(2)


# ---------------------------------------
# IDEA GENERATOR
# ---------------------------------------
with col1:
    if st.button("💡 Generate Blog Idea"):
        if not api_key or not topic:
            st.error("Please enter your API key and topic!")
        else:
            prompt = f"""
            Generate a creative blog idea based on:
            Topic: {topic}
            Tone: {tone}
            Audience: {audience}
            Creativity: {creativity}/10
            
            Give:
            - Title
            - One-paragraph summary
            - Suggested unique angle
            """
            idea = generate_text(prompt, api_key)
            st.success("🎉 Blog Idea Generated!")
            st.write(idea)


# ---------------------------------------
# FULL BLOG GENERATOR
# ---------------------------------------
with col2:
    if st.button("📝 Generate Full Blog"):
        if not api_key or not topic:
            st.error("Please enter your API key and topic!")
        else:
            prompt = f"""
            Write a full blog article.
            Requirements:
            - Topic: {topic}
            - Tone: {tone}
            - Audience: {audience}
            - Creativity: {creativity}/10
            - Length: {length} words
            - SEO-friendly headings
            - Human-like writing
            - Clear structure
            
            Write the blog now.
            """
            blog = generate_text(prompt, api_key)
            st.success("📄 Full Blog Generated!")
            st.write(blog)
