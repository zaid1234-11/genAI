import streamlit as st
from transformers import pipeline
import torch

# Use a cache to load the model only once
@st.cache_resource
def load_model():
    """Loads the text generation model."""
    # Using 'gpt2' for its instruction-following capabilities
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
            
            # --- FINAL, MORE STRUCTURED PROMPT ---
            # This format gives the model a very clear, structured instruction.
            prompt = f"""
[INST]
You are an expert social media manager. Your task is to write a post for the social media platform '{platform}'.
The post must have a '{tone}' tone.
The topic for the post is: '{topic}'.
Generate a creative caption and include 3-5 relevant hashtags.
[/INST]
"""
            
            try:
                # --- TUNED GENERATION PARAMETERS ---
                # These settings balance creativity and focus.
                generated_outputs = generator(
                    prompt,
                    max_new_tokens=150,
                    temperature=0.7,
                    top_k=50,
                    top_p=0.95,
                    do_sample=True,
                    pad_token_id=generator.tokenizer.eos_token_id,
                    no_repeat_ngram_size=3 # Prevents repeating longer phrases
                )
                
                final_post = generated_outputs[0]['generated_text'].split("[/INST]")[1].strip()

                st.subheader("✅ Here's Your Generated Post:")
                st.markdown(f"> {final_post}")

            except Exception as e:
                st.error(f"An error occurred: {e}")


