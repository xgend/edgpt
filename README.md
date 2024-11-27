
# **EdGPT: Educational demo Generative Pre-trained Transformer**

EdGPT is a fine-tuned generative AI model designed specifically for educational purposes. It leverages state-of-the-art transformer-based architectures to provide accurate, engaging, and tailored responses to educational queries.

## **Features**
- **Educational Focus**: Pretrained and fine-tuned on educational datasets to answer academic questions effectively.
- **Customizable**: Easily fine-tunable with new data to expand capabilities.
- **Lightweight Deployment**: Compatible with Ollama AI for efficient local deployment, even in CPU-only environments.

---

## **Project Structure**

```plaintext
edgpt/
│
├── data/                     # Training data
│   ├── training_data.json    # Raw training data
│   ├── validation_data.json  # Validation data
│
├── models/                   # Fine-tuned models
│   └── edgpt/                # Final model files
│
├── scripts/                  # Scripts for processing and training
│   ├── preprocess.py         # Preprocess training data
│   ├── train.py              # Fine-tuning script
│   ├── evaluate.py           # Model evaluation script
│
├── config/                   # Configuration files
│   ├── training_args.json    # Hyperparameters for training
│
├── notebooks/                # Jupyter Notebooks for experiments
│   └── edgpt_analysis.ipynb
│
├── README.md                 # Project documentation
├── requirements.txt          # Python dependencies
└── ollama_config.yaml        # Ollama server configuration
```

---

## **Getting Started**

### **Prerequisites**
1. Python 3.11+
2. Git
3. Ollama AI installed locally (`ollama-cli` for model deployment).

### **Install Dependencies**
Clone the repository and install the necessary Python packages:
```bash
git clone https://github.com/xgenfuture/edgpt.git
cd edgpt
pip install -r requirements.txt
```

---

## **Usage**

### **Step 1: Prepare the Data**
Ensure your training data is formatted correctly in `data/training_data.json`. Use the `scripts/preprocess.py` script to preprocess the data:
```bash
python scripts/preprocess.py
```

### **Step 2: Fine-Tune the Model**
Run the fine-tuning script:
```bash
python scripts/train.py
```

### **Step 3: Evaluate the Model**
Test the fine-tuned model using the evaluation script:
```bash
python scripts/evaluate.py
```

### **Step 4: Deploy with Ollama**
1. Configure Ollama with `ollama_config.yaml`:
   ```yaml
   models:
     - name: edgpt
       path: ./models/edgpt
   ```

2. Start the Ollama server:
   ```bash
   ollama start --config ollama_config.yaml
   ```

3. Query the model:
   ```bash
   ollama query edgpt "What is Newton's second law?"
   ```

---

## **Dataset**
The training data is designed for educational purposes and covers topics such as:
- Science (Physics, Chemistry, Biology)
- Mathematics
- History
- Literature

You can extend the dataset by adding more JSON entries in the `data/` folder.

---

## **Customization**
You can customize **EdGPT** by:
- Adding more data to `training_data.json`.
- Adjusting hyperparameters in `config/training_args.json`.
- Using transfer learning on a different base model.

---

## **Contributing**
Contributions are welcome! Feel free to:
- Submit pull requests.
- Report bugs or request features in the [issues section](https://github.com/yourusername/edgpt/issues).

---

## **License**
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## **Acknowledgments**
- [Meta AI's LLaMA](https://ai.facebook.com/blog/large-language-model-llama-meta-ai/)
- [Hugging Face Transformers](https://huggingface.co/transformers/)
- The open-source community for sharing valuable resources.

---

### **Contact**
For inquiries, reach out to **XGen Future** at mail.xgenfuture@gmail.com.
