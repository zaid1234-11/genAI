import streamlit as st
from transformers import pipeline
import torch

# Use a cache to load the model only once
@st.cache_resource
def load_model():
    """Loads the text generation model."""
    # --- UPGRADED MODEL ---
    # Using a more capable model for better results.
    return pipeline('text-generation', model='EleutherAI/gpt-neo-125M')

generator = load_model()

# --- App Title and Description ---
st.title("🤖 AI Social Media Post Generator")
st.markdown("This app uses the `GPT-Neo` model to generate social media posts based on your inputs. Fill in the details below to get started!")

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
            
            # --- SIMPLIFIED AND DIRECT PROMPT ---
            # This clear format works best with models like GPT-Neo.
            prompt = f"""
You are an expert social media manager.
Write a social media post for the platform '{platform}' with a '{tone}' tone.
The post should be about: '{topic}'.
Include a creative caption and 3-5 relevant hashtags.

Here is the post:
"""
            
            try:
                # --- TUNED GENERATION PARAMETERS ---
                generated_outputs = generator(
                    prompt,
                    max_new_tokens=150,
                    do_sample=True,
                    temperature=0.75,
                    top_k=50,
                    top_p=0.95,
                    no_repeat_ngram_size=2,
                    pad_token_id=generator.tokenizer.eos_token_id,
                    return_full_text=False # Ensures we only get the new text
                )
                
                final_post = generated_outputs[0]['generated_text'].strip()

                st.subheader("✅ Here's Your Generated Post:")
                st.markdown(f"> {final_post}")

            except Exception as e:
                st.error(f"An error occurred: {e}")
