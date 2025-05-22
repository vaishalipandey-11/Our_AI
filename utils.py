import streamlit as st

def about():
    about_text = """
    This application provides access to powerful Large Language Models (LLMs) for a variety of tasks.
    You can:
    -   Chat with an AI assistant.
    -   Use AI agents to perform specific tasks.
    -   Summarize documents and web pages.
    -   Interact with the AI using text, images, audio, and documents.
    -   Customize voice responses.
    -   Create by [ 🤖 Hir Patel 🤖 ](https://github.com/HIRU1920/)')
    """
    return about_text


def set_safety_settings():
    safety_settings = [
        {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE" 
        },
        {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
    ]
    return safety_settings
