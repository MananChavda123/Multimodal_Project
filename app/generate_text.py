from transformers import pipeline

gen = pipeline("text-generation", model="EleutherAI/gpt-neo-1.3B")

def generate_product_text(prompt):
    title = f"Stylish {prompt.title()}"
    description = gen(f"Write a product description for: {prompt}", max_length=60)[0]['generated_text']
    return title, description
