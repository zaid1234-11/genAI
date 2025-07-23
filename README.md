# AI Social Media Post Generator 🤖

This is a simple web application built with Streamlit that uses a text-generation AI model (`distilgpt2`) to create social media posts. You can specify a topic, a target platform, and a desired tone to generate a creative caption and relevant hashtags.

***

## 🚀 Live Demo

You can access the live, deployed version of the app here:

**[https://your-app-name.streamlit.app/](https://your-app-name.streamlit.app/)**

*(Replace the link above with your actual Streamlit Community Cloud URL)*

***

## ✨ Features

* Generate posts for multiple platforms (Instagram, Twitter, Facebook, LinkedIn).
* Choose from various tones (Excited, Professional, Casual, Funny, Inspirational).
* Leverages a one-shot prompting technique for structured and relevant output.
* Simple, clean, and interactive user interface built with Streamlit.

***

## 🛠️ Technologies Used

* **Frontend:** Streamlit
* **AI/ML:** Hugging Face Transformers (`distilgpt2`)
* **Core Language:** Python

***

## 📦 Local Setup and Installation

To run this project on your own machine, follow these steps:

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

1.  Open the [Live Demo](#-live-demo) link or run the app locally.
2.  Enter the topic or idea for your post in the text box.
3.  Select the social media platform from the dropdown menu.
4.  Choose the desired tone for the post.
5.  Click the **"✨ Generate Post"** button and wait for the AI to generate the content.
