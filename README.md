# Hinglish Cyberbullying Detection using BERT
Detect cyberbullying in Hinglish (Hindi-English code-mixed) tweets using a fine-tuned BERT model.
This project uses modern NLP techniques and is deployed as an interactive web app for public testing.

## Demo
Try the model live on Hugging Face Spaces:
https://huggingface.co/spaces/sakshambindal/hinglish-cyberbullying

## Dataset
- Source Dataset: [BullyExplain Dataset](https://github.com/MaityKrishanu/GenEx_Cybebullying), but this has some missing values and irrelevant enteries.
- Updated Dataset: [BullyExplain-updated.xlsx](BullyExplain-updated.xlsx)
- Language: Hinglish (Hindi-English code-mixed, Roman script)
- Samples: 6,084 tweets, balanced Bully/Non_bully classes
- Reference: Maity, Krishanu et al., "GenEx: A Commonsense-aware Unified Generative Framework for Explainable Cyberbullying Detection," EMNLP 2023.

## How to Run Locally
1. Download the full project files (including the trained model)

   Click the Link to download the file: [Download from Onedrive](https://bindal925-my.sharepoint.com/:u:/g/personal/saksham_bindal925_onmicrosoft_com/EQzgDkqVGTxLiW4htpcmzH8BG_CC6hc8teCQ6WPWj4GM_A?e=7qyqJL&download=1)
2. Install dependencies
   ```
   pip install -r requirements.txt
   ```

3.  Run the Gradio app
    ```
    python app.py
    ```
4. Click the Link: [http://localhost:7860](http://localhost:7860) to test the app.

## Example Usage
Try these sample tweets in the app:
```
Tu kitna bekaar aadmi hai, sabko pareshan karta hai.
```
```
Aaj mausam bahut accha hai, chalo ghumne chalte hain.
```

## Model
**Architecture:** BERT-base-multilingual-cased, fine-tuned for binary sequence classification
**Metrics:**
- Accuracy: 0.83
- Precision: 0.81
- Recall: 0.89
- F1-score: 0.85
*(Based on test set evaluation: 594 Non_bully, 693 Bully samples)*
