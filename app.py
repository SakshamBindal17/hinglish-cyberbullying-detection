import gradio as gr
from transformers import BertTokenizer, BertForSequenceClassification
import torch
import torch.nn.functional as F

MODEL_PATH = "best_model"
tokenizer = BertTokenizer.from_pretrained(MODEL_PATH)
model = BertForSequenceClassification.from_pretrained(MODEL_PATH)
model.eval()

def predict_tweet(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=128)
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
        probs = F.softmax(logits, dim=1).squeeze()
        pred = torch.argmax(logits, dim=1).item()
        label = "Bully" if pred == 1 else "Non_bully"
    return f"Prediction: {label}\n\nProbabilities:\nNon_bully: {probs[0]:.2f}\nBully: {probs[1]:.2f}"

demo = gr.Interface(
    fn=predict_tweet,
    inputs=gr.Textbox(lines=2, placeholder="Enter a tweet in Hinglish..."),
    outputs="text",
    title="Hinglish Cyberbullying Detector",
    description="Enter a Hinglish tweet to predict if it's Bully or Non_bully."
)

if __name__ == "__main__":
    demo.launch()
