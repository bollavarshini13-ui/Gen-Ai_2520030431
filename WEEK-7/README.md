# Week 7 – Next Token Probability Analysis Using GPT-2

## 1. Project Title
**Next Token Probability Analysis Using GPT-2**

## 2. Objective
The objective of this project is to understand how a Generative AI language model predicts the next token in a sequence by calculating probabilities for possible next tokens.

## 3. Description
This project uses the pretrained GPT-2 model to analyze text prompts and predict the most probable next tokens.

The program takes four predefined prompts, processes them using the GPT-2 tokenizer and model, calculates the probability distribution of the next token using the Softmax function, and displays the top 5 most probable next-token candidates.

The generated results are also saved automatically into a CSV file for further analysis.

## 4. Technologies Used
- Python
- PyTorch
- Hugging Face Transformers
- GPT-2 Language Model
- CSV

## 5. Project Structure

Week7/
│
├── main.py
├── requirements.txt
├── README.md
└── week7_probability_results.csv

## 6. Input Prompts
The program uses the following four prompts:

1. The cat is
2. Artificial intelligence is
3. India is a
4. Machine learning helps

## 7. Methodology

### Step 1: Load the GPT-2 Model
The program loads the pretrained GPT-2 model and its tokenizer from Hugging Face.

### Step 2: Tokenization
Each input prompt is converted into token IDs using the GPT-2 tokenizer.

### Step 3: Generate Logits
The model processes the input tokens and produces logits for the next-token prediction.

### Step 4: Calculate Probabilities
The Softmax function is applied to the logits to convert them into probabilities.

### Step 5: Select Top 5 Predictions
The program selects the five tokens with the highest probabilities using Top-K selection.

### Step 6: Display Results
The predicted tokens, their ranks, token IDs, and probabilities are displayed in the terminal.

### Step 7: Save Results
The results are saved automatically in the following CSV file:

week7_probability_results.csv

## 8. Installation

Make sure Python is installed on your system.

Install the required libraries by running:

```bash
pip install -r requirements.txt
```

## 9. Execution

Run the following command in the terminal:

```bash
python main.py
```

The GPT-2 model will be downloaded automatically during the first run. An internet connection is required for the initial model download.

## 10. Output

The program generates the Top 5 next-token predictions for each of the four prompts.

The CSV file contains the following columns:

| Column Name | Description |
|---|---|
| Prompt | Original input text |
| Rank | Position of the prediction |
| Candidate Token | Predicted next token |
| Token ID | Numerical ID of the predicted token |
| Probability | Probability assigned to the predicted token |

A total of 20 predictions are generated (4 prompts × 5 predictions).

## 11. Key Concepts

- **Tokenization:** Breaking text into smaller units called tokens.
- **Logits:** Raw scores produced by the model for possible next tokens.
- **Softmax:** Converts logits into a probability distribution.
- **Top-K Prediction:** Selects the K most probable next tokens.
- **Language Model:** Predicts the next token based on the input context.

## 12. Conclusion

This experiment demonstrates how GPT-2 performs next-token prediction using probability distributions. It provides practical understanding of tokenization, logits, Softmax, and Top-K selection, which are fundamental concepts in Generative AI and Large Language Models.

The generated CSV file makes it easy to inspect and compare the predictions and their probabilities across different prompts.
