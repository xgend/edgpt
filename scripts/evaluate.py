from transformers import pipeline

model_path = "models/edgpt"
generator = pipeline("text-generation", model=model_path)

def evaluate():
    prompt = "Explain Newton's first law of motion."
    response = generator(prompt, max_length=100)
    print("EdGPT Response:", response[0]["generated_text"])

if __name__ == "__main__":
    evaluate()
