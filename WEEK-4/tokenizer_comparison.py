from transformers import AutoTokenizer


# Tokenizers to compare
TOKENIZERS = {
    "BPE - GPT-2": "gpt2",
    "WordPiece - Multilingual BERT": "bert-base-multilingual-cased",
    "SentencePiece - XLM-R": "xlm-roberta-base"
}


# Same sentences will be tested with all three tokenizers
TEXTS = {
    "English": "Artificial intelligence is changing the world.",
    "Telugu": "కృత్రిమ మేధస్సు ప్రపంచాన్ని మారుస్తోంది.",
    "Hindi": "कृत्रिम बुद्धिमत्ता दुनिया को बदल रही है।"
}


def load_tokenizers():

    tokenizers = {}

    for name, model_name in TOKENIZERS.items():

        print(f"\nLoading {name}...")

        tokenizer = AutoTokenizer.from_pretrained(model_name)

        tokenizers[name] = tokenizer

    return tokenizers


def compare_tokenizers(tokenizers):

    for language, text in TEXTS.items():

        print("\n" + "=" * 70)
        print(f"LANGUAGE: {language}")
        print(f"INPUT TEXT: {text}")
        print("=" * 70)

        for tokenizer_name, tokenizer in tokenizers.items():

            # Convert text into token IDs
            encoded = tokenizer(
                text,
                add_special_tokens=True
            )

            token_ids = encoded["input_ids"]

            # Convert token IDs back to readable tokens
            tokens = tokenizer.convert_ids_to_tokens(token_ids)

            print(f"\n--- {tokenizer_name} ---")

            print("Tokens:")
            print(tokens)

            print("\nToken IDs:")
            print(token_ids)

            print(f"\nToken Count: {len(token_ids)}")


def main():

    print("\nBPE vs WordPiece vs SentencePiece")
    print("=" * 70)

    tokenizers = load_tokenizers()

    compare_tokenizers(tokenizers)


if __name__ == "__main__":
    main()