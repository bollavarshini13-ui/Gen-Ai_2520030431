# Tokenizer Comparison: BPE vs WordPiece vs SentencePiece

A small Python project that compares how three popular tokenization algorithms split the **same sentence in English, Telugu, and Hindi**. It shows the tokens, token IDs, and token count for each tokenizer, making it easy to see how tokenization behaves for different languages and scripts.

---

## Tokenizers Compared

| Algorithm | Model Used | Hugging Face ID |
|---|---|---|
| **BPE** (Byte-Pair Encoding) | GPT-2 | `gpt2` |
| **WordPiece** | Multilingual BERT | `bert-base-multilingual-cased` |
| **SentencePiece** | XLM-RoBERTa | `xlm-roberta-base` |

## Test Sentences

| Language | Text |
|---|---|
| English | Artificial intelligence is changing the world. |
| Telugu | కృత్రిమ మేధస్సు ప్రపంచాన్ని మారుస్తోంది. |
| Hindi | कृत्रिम बुद्धिमत्ता दुनिया को बदल रही है। |

---

## Why This Matters

Tokenization decides how text is broken into pieces before a language model sees it. The number of tokens affects:

- **Cost**: most LLM APIs charge per token.
- **Context length**: more tokens means less text fits in the context window.
- **Model quality**: how well a tokenizer handles a language can influence how well a model understands it.

Running the same meaning through different tokenizers and languages shows how much token counts can vary, especially for non-English scripts.

---

## Project Structure

```
.
├── tokenizer_comparison.py   # Main script
├── requirements.txt          # Dependencies
└── README.md
```

---

## Requirements

- Python 3.8+
- Internet connection on first run (tokenizer files are downloaded from Hugging Face and then cached locally)

Dependencies (`requirements.txt`):

```
transformers
sentencepiece
```

---

## Installation

```bash
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>

python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate

pip install -r requirements.txt
```

---

## Usage

```bash
python tokenizer_comparison.py
```

For each language, the script prints the following for every tokenizer:

1. **Tokens**: the readable token pieces
2. **Token IDs**: the numeric IDs the model receives
3. **Token Count**: the total number of tokens, including special tokens

### Output format

```
======================================================================
LANGUAGE: English
INPUT TEXT: Artificial intelligence is changing the world.
======================================================================

--- BPE - GPT-2 ---
Tokens:
[...]

Token IDs:
[...]

Token Count: ...
```

Run the script to see the actual tokens and counts on your machine.

---

## How It Works

1. `load_tokenizers()` loads each tokenizer using `AutoTokenizer.from_pretrained()`.
2. `compare_tokenizers()` encodes each sentence with `add_special_tokens=True`.
3. Token IDs are converted back to readable tokens with `convert_ids_to_tokens()`.
4. Tokens, IDs, and counts are printed for side-by-side comparison.

> **Note:** special tokens depend on the model. BERT adds `[CLS]` and `[SEP]`, XLM-R adds `<s>` and `</s>`, and GPT-2 does not add any by default. This slightly affects the token counts.

---

## Customizing

**Add your own text:** edit the `TEXTS` dictionary in `tokenizer_comparison.py`:

```python
TEXTS = {
    "English": "Artificial intelligence is changing the world.",
    "Tamil": "your text here"
}
```

**Add another tokenizer:** add an entry to the `TOKENIZERS` dictionary with any Hugging Face model ID:

```python
TOKENIZERS = {
    "BPE - GPT-2": "gpt2",
    "Unigram - T5": "t5-small"
}
```

---

## Tech Stack

- Python
- Hugging Face `transformers`
- `sentencepiece`

---

## License

This project is licensed under the [MIT License](LICENSE). Add a `LICENSE` file to your repository, or change this section to the license you prefer.
