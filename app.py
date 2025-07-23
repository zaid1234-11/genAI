import streamlit as st
import json
import requests # Make sure to add 'requests' to your requirements.txt

# --- App Title and Description ---
st.title("🤖 AI Social Media Post Generator")
st.markdown("This app uses the Gemini API to generate high-quality social media posts. Fill in the details below to get started!")

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
            # This prompt is designed for a powerful instruction-following model.
            prompt = f"""
As an expert social media manager, create a post for the platform '{platform}' with a '{tone}' tone.
The topic is: '{topic}'.
Your response must include a creative caption and 3-5 relevant hashtags.
"""

            # --- API CALL SETUP ---
            # This section calls the external Gemini API
            api_key = "" # This is handled automatically by the environment
            api_url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={api_key}"
            
            headers = {'Content-Type': 'application/json'}
            
            data = {
                "contents": [{
                    "parts": [{
                        "text": prompt
                    }]
                }]
            }

            try:
                # --- MAKING THE REQUEST ---
                response = requests.post(api_url, headers=headers, data=json.dumps(data))
                response.raise_for_status() # Raise an exception for bad status codes
                
                result = response.json()
                
                # --- EXTRACTING THE TEXT ---
                # The structure of the response is navigated to get the generated text.
                final_post = result['candidates'][0]['content']['parts'][0]['text'].strip()

                st.subheader("✅ Here's Your Generated Post:")
                st.markdown(f"> {final_post}")

            except requests.exceptions.RequestException as e:
                st.error(f"An API error occurred: {e}")
            except (KeyError, IndexError) as e:
                st.error(f"Could not parse the API response. Error: {e}")
                st.write("Raw API Response:")
                st.json(result) # Display the raw response for debugging

