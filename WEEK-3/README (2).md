# LLM Client with Usage Monitoring

A small Python project that provides a **unified interface for multiple LLM providers** (Google Gemini and local Ollama), with **automatic model fallback, retry with backoff, and per-call usage logging to MongoDB**.

Every request records token counts, latency, estimated cost, and status, so you can monitor how your LLM calls behave over time.

---

## Features

- **Provider abstraction**: a common `LLMProvider` interface, with `GeminiProvider` and `OllamaProvider` implementations.
- **Automatic model fallback (Gemini)**: if a model is unavailable, rate limited, or times out, the client moves to the next backup model.
- **Retry with exponential backoff**: temporary errors (timeouts, 429, 5xx) are retried up to 3 attempts (2s, then 4s delay).
- **Usage tracking in MongoDB**: each call logs provider, model, input/output/total tokens, latency, estimated cost, status, and attempts.
- **Failure logging**: failed requests are logged too, including the error message.
- **Cost estimation**: configurable per-million-token pricing for hosted Gemini calls. Local Ollama inference is recorded as `0.0` with a note that local compute cost is not included.
- **Unit tests** using fake providers and loggers, so no API keys or database are needed.

---

## Project Structure

```
.
├── main.py             # CLI entry point
├── llm_client.py       # LLMResult, providers (Gemini, Ollama), LLMClient
├── usage_logger.py     # MongoDB usage logger
├── test_client.py      # Unit tests
├── requirements.txt    # Python dependencies
└── .env                # Your secrets and config (not committed)
```

---

## Requirements

- Python 3.9+
- A [MongoDB](https://www.mongodb.com/) instance (local or Atlas)
- A [Gemini API key](https://aistudio.google.com/app/apikey) (if using Gemini)
- [Ollama](https://ollama.com/) installed and running locally (if using Ollama)

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

## Configuration

Create a file named `.env` in the project root:

```env
GEMINI_API_KEY=your_gemini_api_key
MONGODB_URI=your_mongodb_connection_string

# Optional: used for cost estimation (USD per 1 million tokens)
GEMINI_INPUT_PRICE_PER_MILLION=0
GEMINI_OUTPUT_PRICE_PER_MILLION=0
```

| Variable | Required | Description |
|---|---|---|
| `GEMINI_API_KEY` | Only for Gemini | Your Google Gemini API key |
| `MONGODB_URI` | Yes | MongoDB connection string |
| `GEMINI_INPUT_PRICE_PER_MILLION` | No | Input token price per 1M tokens (default `0`) |
| `GEMINI_OUTPUT_PRICE_PER_MILLION` | No | Output token price per 1M tokens (default `0`) |

> **Security:** never commit your `.env` file. Add it to `.gitignore`:
>
> ```
> .env
> venv/
> __pycache__/
> ```

### Using Ollama

Make sure Ollama is running and the model is pulled:

```bash
ollama pull llama3.2
ollama serve
```

---

## Usage

```bash
python main.py
```

You will be prompted to choose a provider and enter a question:

```
Choose provider (gemini/ollama): gemini
Enter your question: Explain AI in simple words
```

Example output:

```
Trying Gemini model: gemini-3.8-flash
Gemini model selected: gemini-3.8-flash

Usage details saved to MongoDB.
Latency: 1234.56 ms
Input tokens: 6
Output tokens: 120
Estimated cost (USD): 0.0

LLM Response:
...
```

### Using it in your own code

```python
from llm_client import GeminiProvider, LLMClient
from usage_logger import UsageLogger

logger = UsageLogger()
client = LLMClient(GeminiProvider(api_key="YOUR_KEY"), logger)

print(client.generate("What is machine learning?"))

logger.close()
```

---

## How It Works

1. `main.py` picks a provider and wraps it in `LLMClient`.
2. `LLMClient.generate()` calls the provider and measures latency.
3. **Gemini fallback:** `GeminiProvider` tries each model in order (`gemini-3.8-flash`, `gemini-3.7-flash`, `gemini-3.5-flash-lite`) and moves on if one is unavailable.
4. **Retries:** if the whole call fails with a temporary error, `LLMClient` retries with exponential backoff (up to 3 attempts).
5. **Logging:** success or failure, the result is saved to the `api_usage` collection in the `llm_monitoring` database.

### Example MongoDB record

```json
{
  "provider": "Gemini",
  "model": "gemini-3.8-flash",
  "input_tokens": 6,
  "output_tokens": 120,
  "total_tokens": 126,
  "latency_ms": 1234.56,
  "estimated_cost_usd": 0.0,
  "cost_type": "estimated_hosted_api_cost",
  "status": "success",
  "attempts": 1,
  "timestamp": "2026-11-24T10:30:00Z"
}
```

---

## Running Tests

The tests use fake providers and loggers, so no API key or database is needed:

```bash
python -m unittest test_client.py
# or
pytest
```

---

## Extending the Project

To add a new provider (for example OpenAI or Anthropic):

1. Create a class that extends `LLMProvider`.
2. Set `provider_name` and `model`.
3. Implement `generate(prompt)` returning an `LLMResult`.
4. Pass it to `LLMClient`.

---

## Tech Stack

- Python
- Google Gen AI SDK (`google-genai`)
- Ollama (local inference)
- MongoDB (`pymongo`)
- `python-dotenv`, `requests`, `pytest`

---

## License

This project is licensed under the [MIT License](LICENSE). Add a `LICENSE` file to your repository, or change this section to the license you prefer.
