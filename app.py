import streamlit as st
from transformers import pipeline
import torch

# Use a cache to load the model only once
@st.cache_resource
def load_model():
    """Loads the text generation model."""
    return pipeline('text-generation', model='distilgpt2')

generator = load_model()

# --- App Title and Description ---
st.title("🤖 AI Social Media Post Generator")
st.markdown("This app uses the `distilgpt2` model to generate social media posts based on your inputs. Fill in the details below to get started!")

# --- User Inputs ---
with st.form("post_form"):
    topic = st.text_input(
        "**Topic or Idea**", 
        placeholder="e.g., launching a new line of eco-friendly sneakers"
    )
    
    platform = st.selectbox(
        "**Platform**",
        ('Instagram', 'Twitter', 'Facebook', 'LinkedIn')
    )
    
    tone = st.selectbox(
        "**Tone**",
        ('Excited', 'Professional', 'Casual', 'Funny', 'Inspirational')
    )
    
    submitted = st.form_submit_button("✨ Generate Post")

# --- Generation Logic ---
if submitted:
    if not topic:
        st.error("Please enter a topic before generating.")
    else:
        with st.spinner("🤖 AI is thinking... Please wait."):
            # The one-shot prompt from your notebook code
            prompt = f"""
Generate a social media post by following the example format.

---
*EXAMPLE*
*Platform:* Instagram
*Topic:* A new bookstore cafe is opening.
*Tone:* Cozy and inviting

*Generated Post:*
*Caption:* The day has finally come! ☕📚 We're so excited to announce the grand opening of 'The Reading Nook Cafe' this Saturday. Come find your next favorite book and enjoy a warm cup of coffee with us. We can't wait to welcome you to our cozy corner of the world!
*Hashtags:* #BookstoreCafe #GrandOpening #CoffeeAndBooks #NewBeginnings #CozyVibes
---

*YOUR TASK*
*Platform:* {platform}
*Topic:* {topic}
*Tone:* {tone}

*Generated Post:*
*Caption:*"""
            
            try:
                generated_outputs = generator(
                    prompt,
                    max_length=300,
                    num_return_sequences=1,
                    pad_token_id=generator.tokenizer.eos_token_id
                )
                
                generated_text = generated_outputs[0]['generated_text']
                final_post = generated_text.split("Generated Post:")[2].strip()

                st.subheader("✅ Here's Your Generated Post:")
                st.markdown(f"> {final_post}")

            except Exception as e:
                st.error(f"An error occurred: {e}")