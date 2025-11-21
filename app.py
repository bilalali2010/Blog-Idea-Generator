import streamlit as st
import random

st.set_page_config(page_title="Blog Idea Generator", page_icon="📝")

def generate_blog_idea(topic, tone, audience, creativity, length):
    templates = [
        f"A {tone.lower()} blog post about **{topic}**, designed for {audience}.",
        f"A {creativity.lower()} exploration of **{topic}** written in a {tone.lower()} tone.",
        f"A blog idea focusing on **{topic}**, crafted for {audience} with a {tone.lower()} style.",
        f"A unique angle on **{topic}**, blending a {tone.lower()} tone with {creativity.lower()} creativity.",
    ]
    idea = random.choice(templates)
    return f"{idea}\n\nSuggested Length: {length} words"

st.title("📝 Blog Idea Generator")
st.write("Generate creative blog ideas with adjustable parameters.")

topic = st.text_input("🧠 Blog Topic", placeholder="e.g., AI in Healthcare")
tone = st.selectbox("🎨 Tone", ["Professional", "Casual", "Humorous", "Inspirational", "Technical"])
audience = st.text_input("👥 Audience", placeholder="e.g., Students, Developers, Beginners")
creativity = st.slider("✨ Creativity Level", 1, 10, 5)
length = st.selectbox("✍️ Blog Length", ["300", "500", "700", "1000", "1500"])

if st.button("Generate"):
    if not topic or not audience:
        st.error("Please complete all fields!")
    else:
        result = generate_blog_idea(topic, tone, audience, str(creativity), length)
        st.success("🎉 Idea Generated!")
        st.write(result)
