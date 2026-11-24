# Gen AI Program 2 – Multi-Provider LLM Client

##  About the Project

This project is a simple Generative AI application built using Python. It allows users to work with **Google Gemini** or a **local Ollama model** through the same client.

The main idea is to make it easy to switch between different LLM providers without changing the main application.

##  What This Project Does

- Connects to Google Gemini using its API
- Supports Ollama for running an LLM locally
- Lets the user choose which provider to use
- Handles temporary Gemini server issues with retries and fallback models
- Keeps the Gemini API key in a `.env` file
- Includes basic unit testing

##  Project Files

```text
Gen-AI-Program-2/
├── main.py
├── llm_client.py
├── test_client.py
├── requirements.txt
├── .gitignore
└── .env
```

- **`main.py`** – Starts the application and lets the user select Gemini or Ollama.
- **`llm_client.py`** – Contains the Gemini, Ollama, and common LLM client classes.
- **`test_client.py`** – Contains tests for the LLM client.
- **`requirements.txt`** – Contains the required Python packages.
- **`.gitignore`** – Prevents files such as `.env`, cache files, and virtual environments from being uploaded.
- **`.env`** – Used to store the Gemini API key.

## 🛠️ Technologies Used

- Python
- Google Gemini
- Ollama
- `google-genai`
- `requests`
- `python-dotenv`
- `unittest`

## ⚙️ Setup

First, clone the repository and move into the project folder:

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd Gen-AI-Program-2
```

Create and activate a virtual environment:

```bash
python -m venv .venv
```

**Windows:**
```bash
.venv\Scripts\activate
```

**Linux/macOS:**
```bash
source .venv/bin/activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

##  Gemini Setup

Create a `.env` file and add your Gemini API key:

```env
GEMINI_API_KEY=your_api_key_here
```

Make sure you **do not upload your API key or `.env` file to GitHub**.

##  Ollama Setup

If you want to use Ollama, install it and download the required model:

```bash
ollama pull llama3.2
```

Make sure Ollama is running before selecting the Ollama option.

##  Run the Project

Start the application using:

```bash
python main.py
```

You will be asked to choose a provider:

```text
Choose provider (gemini/ollama):
```

Enter either `gemini` or `ollama`, then type your question.

The application will generate and display the response from the selected LLM.

##  Testing

To run the unit tests:

```bash
python -m unittest test_client.py
```

The test checks whether the common `LLMClient` correctly handles a response from an LLM provider.

##  How It Works

```text
             main.py
                │
        Choose LLM Provider
          /             \
      Gemini           Ollama
         \               /
          \             /
           LLMClient
              │
              ▼
        AI Response
```

##  What I Learned

Through this project, I learned how to:

- Connect Python applications to Generative AI models
- Work with both cloud-based and local LLMs
- Use a common interface for different AI providers
- Handle API/server errors using retries and fallback models
- Manage API keys using environment variables
- Write basic unit tests

##  Author

**Varshini Bolla**

*Gen AI Program 2*
