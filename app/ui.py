import streamlit as st
from PIL import Image
from app.generate_image import generate_product_image
from app.generate_text import generate_product_text
from app.caption_image import generate_caption
# from app.text_to_speech import speak_text

def run_ui():
    st.set_page_config(page_title="🛍️ Retail GenAI Suite", layout="wide")
    st.title("🧠 Retail GenAI: Product Image + Text + Audio")

    prompt = st.text_input("Enter product description (e.g., 'red leather handbag with gold chains')")

    uploaded_image = st.file_uploader("Or upload a reference image", type=["jpg", "jpeg", "png"])

    if st.button("Generate Image"):
        image = generate_product_image(prompt)
        st.image(image, caption="Generated Product Image")
        image.save("outputs/generated_images/product.png")

    if uploaded_image and st.button("Caption Uploaded Image"):
        img = Image.open(uploaded_image).convert("RGB")
        caption = generate_caption(img)
        st.write(f"**📝 Caption:** {caption}")

