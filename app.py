import streamlit as st
import google.generativeai as genai

# --- App Title and Description ---
st.title("🤖 AI Social Media Post Generator")
st.markdown("This app uses the Gemini API to generate high-quality social media posts. Fill in the details below to get started!")

# --- Configure the API ---
# The API key is stored in Streamlit's Secrets management.
try:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error(f"Error configuring the API. Have you set your GEMINI_API_KEY in Streamlit Secrets? Error: {e}")
    st.stop()


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
            
            # --- GEMINI API PROMPT ---
            prompt = f"""
As an expert social media manager, create a post for the platform '{platform}' with a '{tone}' tone.
The topic is: '{topic}'.
Your response must include a creative caption and 3-5 relevant hashtags.
"""

            try:
                # --- MAKING THE REQUEST ---
                response = model.generate_content(prompt)
                
                # --- EXTRACTING THE TEXT ---
                final_post = response.text.strip()

                st.subheader("✅ Here's Your Generated Post:")
                st.markdown(f"> {final_post}")

            except Exception as e:
                st.error(f"An API error occurred: {e}")

