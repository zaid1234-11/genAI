import streamlit as st
from transformers import pipeline
import torch

# Use a cache to load the model only once
@st.cache_resource
def load_model():
    """Loads the text generation model."""
    # Switched to 'gpt2' for better instruction-following capabilities
    return pipeline('text-generation', model='gpt2')

generator = load_model()

# --- App Title and Description ---
st.title("🤖 AI Social Media Post Generator")
st.markdown("This app uses the `gpt2` model to generate social media posts based on your inputs. Fill in the details below to get started!")

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
            
            # --- SIMPLIFIED AND MORE DIRECT PROMPT ---
            # This prompt is easier for the model to understand and follow.
            prompt = f"""
You are an expert social media manager.
Write a social media post for the platform '{platform}' with a '{tone}' tone.
The post should be about: '{topic}'.
Include a creative caption and 3-5 relevant hashtags.

Post:
"""
            
            try:
                # This version tells the model to only return the new text it generates.
                generated_outputs = generator(
                    prompt,
                    max_new_tokens=150,      # Generate up to 150 new words
                    return_full_text=False,  # This is the key change!
                    pad_token_id=generator.tokenizer.eos_token_id,
                    num_beams=5,             # Helps generate more coherent text
                    no_repeat_ngram_size=2   # Prevents repetitive phrases
                )
                
                # The output is now much cleaner, no splitting needed.
                final_post = generated_outputs[0]['generated_text'].strip()

                st.subheader("✅ Here's Your Generated Post:")
                st.markdown(f"> {final_post}")

            except Exception as e:
                st.error(f"An error occurred: {e}")

