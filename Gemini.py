import streamlit as st 
import google.generativeai as genai 
from dotenv import load_dotenv
from PIL import Image
import os 
import io 

# Load environment variables from .env file
load_dotenv()

# Function to convert image to byte array
def image_to_byte_array(image: Image) -> bytes:
    imgByteArr = io.BytesIO()
    image.save(imgByteArr, format=image.format)
    imgByteArr = imgByteArr.getvalue()
    return imgByteArr

# Get API Key from environment variables
API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=API_KEY)

# Display logo image in Streamlit
st.image("./LOGO.png", width=250)
st.write("")

# Create tabs in Streamlit
tabs = st.tabs(["Chatbot"])

# Main function for the chatbot interface
def main():
    with tabs[0]:  # Access the first (and only) tab
        st.header("Interact with Chatbot")
        st.write("")

        # Text area for prompt input
        prompt = st.text_area("Prompt", placeholder="Enter your prompt here...", height=150, label_visibility="visible")

        if st.button("SEND", use_container_width=True):
            # Initialize the model and generate content
            model = genai.GenerativeModel("gemini-pro")  # Check model compatibility if errors persist

            response = model.generate_content(prompt)

            # Display response
            st.write("")
            st.header(":blue[Response]")
            st.write("")
            st.markdown(response.text)

# Run the main function when the script is executed
if __name__ == "__main__":
    main()
