Gemini API
This project shows how to utilise the Gemini AI within a Python application through its API. A prompt can then be given to the AI and the result shown within the console.

Currently, the AI is prompted to describe Artificial Intelligence in an easily understood manner.
Features
Access to Google's Gemini API

Environment variable storage for API key
Python
Easy to install dependencies
Prompt driven text output from the AI
Tech Stack
Python 3.12
Google Gemini API
google-genai
python-dotenv
Project Structure
```text
.
├── main.py
├── requirements.txt
├── .env
├── .gitignore
└── .venv/
```
Requirements
Python 3.10 or newer
VS Code
Gemini API Key.
Your Gemini API key can be obtained via Google AI Studio:
https://aistudio.google.com/apikey
Setting up
1. Clone the project
```bash
git clone
cd
```
2. Set up a virtual environment
```bash
python -m venv .venv
```
3. Activate virtual environment
For Windows (PowerShell):
```powershell
.\.venv\Scripts\Activate.ps1
```
For macOS/Linux:
```bash
source .venv/bin/activate
```
4. Install dependencies
```bash
pip install -r requirements.txt
```
5. Enter in your API key
Make a new file in the projects root directory called .env.
```env
GEMINI_API_KEY=your_gemini_api_key_here
```
Enter your Gemini API key in place of your_gemini_api_key_here.
Ensure that you never commit or disclose your .env file and API key.
6. Execute the application
```bash
python main.py
```
How It Works
Reads in environment variables from the .env file.
Initialises the Gemini API with the entered API key.
Provides the AI with a prompt.
Obtains the resulting text.
Displays the text in the console.
Example Prompt
```text
What is Artificial Intelligence? Explain in simple words.
```
Example Output
```text
LLM Response:
Artificial Intelligence (AI) is the ability of computers to perform
tasks that usually require human intelligence, such as learning,
problem-solving, understanding language, and making decisions.
```
Note: The output can differ with each invocation of the AI.
Dependencies
The required libraries can be found in the requirements.txt document.
google-genai
requests
python-dotenv
pymongo
pytest
All dependencies can be installed by executing:
```bash
pip install -r requirements.txt
```
Security
Environment variables are used to store API keys.
.gitignore prevents the .env file from being uploaded to Git.
Never disclose API keys, database login details or any other sensitive information.
Potential Enhancements
Enable dynamic user prompting.
Incorporate error checking for API issues.
Allow for more than one Gemini AI model.
Include a chatbot.
Implement MongoDB to log chats.
Include automated testing functionality.

Author

This was produced as part of a Generative AI learning project.

If you find this project of value then please consider investigating it further and/or contributing. ⭐
