# AI Social Media Post Generator 🤖

This is a web application built with Streamlit that leverages the powerful Google Gemini API to generate high-quality, creative social media posts. You can specify a topic, a target platform, and a desired tone, and the AI will create a compelling post complete with a caption and relevant hashtags.

***

## 🚀 Live Demo

You can access the live, deployed version of the app here:

**[https://phhyzultzf785btglvxuu9.streamlit.app/](https://phhyzultzf785btglvxuu9.streamlit.app/)**
***

## ✨ Features

* **High-Quality Content:** Uses the Google Gemini API for creative and context-aware text generation.
* **Customizable:** Generate posts for multiple platforms (Instagram, Twitter, Facebook, LinkedIn).
* **Tone Selection:** Choose from various tones (Excited, Professional, Casual, Funny, Inspirational).
* **Simple Interface:** Clean and interactive user interface built with Streamlit.

***

## 🛠️ Technologies Used

* **Frontend:** Streamlit
* **AI/ML:** Google Gemini API (`gemini-1.5-flash`)
* **Core Language:** Python

***

## 📦 Local Setup and Installation

To run this project on your own machine, follow these steps:

### 1. Configuration: Add Your API Key

This application requires a Google Gemini API key to function.

1.  **Get an API Key:** Obtain a free API key from **[Google AI Studio](https://aistudio.google.com/app/apikey)**.
2.  **Create a Secrets File:** In your project folder, create a new folder named `.streamlit` and inside it, create a file named `secrets.toml`.
3.  **Add Your Key:** Add the following line to your `secrets.toml` file, replacing `YOUR_API_KEY_HERE` with the key you just copied:
    ```toml
    GEMINI_API_KEY = "YOUR_API_KEY_HERE"
    ```
    *Note: When deploying to Streamlit Community Cloud, you will add this same line to the app's online "Secrets" manager instead of using a file.*

### 2. Installation Steps

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/your-repository-name.git](https://github.com/your-username/your-repository-name.git)
    cd your-repository-name
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # For Windows
    python -m venv venv
    .\venv\Scripts\activate

    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Streamlit app:**
    ```bash
    streamlit run app.py
    ```
    The application will now be running on your local machine.

***

## Usage

1.  Open the app in your browser.
2.  Enter the topic or idea for your post.
3.  Select the social media platform.
4.  Choose the desired tone.
5.  Click the **"✨ Generate Post"** button and wait for the AI to generate the content.

