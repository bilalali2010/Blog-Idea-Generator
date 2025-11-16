import streamlit as st
from transformers import T5Tokenizer, T5ForConditionalGeneration

@st.cache_resource
def load_model():
    model_name = "t5-small"
    tokenizer = T5Tokenizer.from_pretrained(model_name)
    model = T5ForConditionalGeneration.from_pretrained(model_name)
    return tokenizer, model

tokenizer, model = load_model()

st.title("📝 Blog Idea Generator (FREE, No API Key)")
st.write("Generate blog ideas with adjustable parameters using a free local model.")

topic = st.text_input("Enter your topic (e.g., AI tools, fitness, cooking):")

tone = st.selectbox(
    "Select tone:",
    ["Professional", "Casual", "Funny", "Serious", "Motivational"]
)

audience = st.text_input("Target audience (e.g., students, developers, beginners):")

num_ideas = st.slider("How many ideas?", 1, 10, 5)

creativity = st.slider("Creativity Level (Temperature)", 0.1, 1.5, 0.9)

def generate_blog_idea(topic, tone, audience, creativity):
    prompt = (
        f"Generate a {tone} blog idea for the topic '{topic}' "
        f"targeted at {audience}. Make it creative."
    )
    
    input_text = "generate: " + prompt
    inputs = tokenizer.encode(input_text, return_tensors="pt", max_length=128, truncation=True)

    outputs = model.generate(
        inputs,
        max_length=80,
        do_sample=True,
        top_p=0.95,
        temperature=creativity,
        num_return_sequences=1
    )

    return tokenizer.decode(outputs[0], skip_special_tokens=True)

if st.button("Generate Ideas"):
    if topic.strip():
        st.subheader("Generated Blog Ideas:")
        for i in range(num_ideas):
            idea = generate_blog_idea(topic, tone, audience, creativity)
            st.write(f"**{i+1}. {idea}**")
            st.write("---")
    else:
        st.warning("Please enter a topic.")
