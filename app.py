import streamlit as st
import requests

st.set_page_config(page_title="Blog Idea & Blog Generator", page_icon="📝", layout="wide")

# ---------------------------------------
# GET API KEY FROM SECRETS
# ---------------------------------------
api_key = st.secrets["openrouter_api_key"]

def generate_text(prompt):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "HTTP-Referer": "http://localhost",
        "Content-Type": "application/json",
    }

    payload = {
        "model": "arcee-ai/trinity-mini:free",

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
st.title("📝 Blog Idea + Blog Generator (Grok 4.1 Fast • Free • OpenRouter)")
st.write("Generate blog ideas or full blogs using automatic API key from Streamlit Secrets.")

topic = st.text_input("🧠 Blog Topic", placeholder="e.g., Benefits of AI in Healthcare")
tone = st.selectbox("🎨 Tone", ["Professional", "Casual", "Humorous", "Inspirational", "Technical"])
audience = st.text_input("👥 Audience", placeholder="e.g., Students, Developers, Bloggers")
creativity = st.slider("✨ Creativity Level", 1, 10, 5)
length = st.selectbox("✍️ Blog Length (words)", ["300", "500", "700", "1000", "1500", "2000"])

col1, col2 = st.columns(2)

# ---------------------------------------
# IDEA GENERATOR
# ---------------------------------------
with col1:
    if st.button("💡 Generate Blog Idea"):
        if not topic:
            st.error("Please enter a topic!")
        else:
            prompt = f"""
            Generate a creative blog idea based on:
            - Topic: {topic}
            - Tone: {tone}
            - Audience: {audience}
            - Creativity: {creativity}/10

            Provide:
            - Catchy title
            - Summary paragraph
            - Unique angle
            """
            idea = generate_text(prompt)
            st.success("🎉 Blog Idea Generated!")
            st.write(idea)

# ---------------------------------------
# FULL BLOG GENERATOR
# ---------------------------------------
with col2:
    if st.button("📝 Generate Full Blog"):
        if not topic:
            st.error("Please enter a topic!")
        else:
            prompt = f"""
            Write a complete blog article with:

            Topic: {topic}
            Tone: {tone}
            Audience: {audience}
            Creativity Level: {creativity}/10
            Target Length: {length} words

            Additional requirements:
            - SEO-friendly headings
            - Human-like writing
            - Engaging intro & conclusion
            - Proper structure with H2/H3
            """

            blog = generate_text(prompt)
            st.success("📄 Full Blog Generated!")
            st.write(blog)
