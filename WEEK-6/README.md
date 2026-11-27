# Week 6 – Generative AI Programming Practical

## LLM Baseline Evaluation using Ollama and Llama 3.2

This project evaluates the performance of a locally running Large Language Model (LLM), **Llama 3.2**, using a Golden Question Set. The program generates answers for predefined questions, compares them against expected keywords, calculates keyword coverage scores, and saves the evaluation results in a CSV file.

This experiment represents the first baseline evaluation, identified as **Release v0.1**.

---

## Project Overview

The project performs the following tasks:

- Loads a Golden Question Set containing 30 questions.
- Sends each question to Llama 3.2 using Ollama.
- Generates responses using the local LLM.
- Compares generated answers against expected keywords.
- Calculates keyword coverage percentages.
- Assigns PASS, REVIEW, or ERROR status to each question.
- Saves the evaluation results in a CSV file.
- Displays a baseline evaluation summary in the terminal.

---

## Technologies Used

- Python
- Ollama
- Llama 3.2
- Visual Studio Code
- Requests library
- JSON
- CSV

---

## Project Structure

```text
week6/
│
├── main.py
├── golden_set.json
├── requirements.txt
└── baseline_results.csv
```

| File | Description |
|---|---|
| `main.py` | Main Python program for LLM evaluation |
| `golden_set.json` | Contains 30 questions, expected answers, keywords, and sources |
| `requirements.txt` | Python dependencies |
| `baseline_results.csv` | Automatically generated evaluation results |

---

## Prerequisites

Make sure the following software is installed:

1. Python 3.x
2. Visual Studio Code
3. Ollama

Download links:

- [Python](https://www.python.org/downloads/)
- [Visual Studio Code](https://code.visualstudio.com/)
- [Ollama](https://ollama.com/download)

---

## Installation and Setup

### Step 1: Install Ollama

Download and install Ollama from:

https://ollama.com/download

Verify the installation:

```bash
ollama --version
```

### Step 2: Download Llama 3.2

Open the terminal and run:

```bash
ollama pull llama3.2
```

Verify that the model is installed:

```bash
ollama list
```

### Step 3: Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
```

Navigate into the project directory:

```bash
cd week6
```

### Step 4: Install Python dependencies

```bash
python -m pip install -r requirements.txt
```

The required dependency is:

```text
requests
```

---

## How to Run

Make sure Ollama is running and Llama 3.2 is installed.

Run the Python program:

```bash
python main.py
```

The program will start the baseline evaluation and process all questions in the Golden Question Set.

---

## Evaluation Methodology

### 1. Golden Question Set

Each question in `golden_set.json` contains:

- Question ID
- Question
- Expected answer
- Keywords
- Source URL

### 2. LLM Response Generation

The program sends each question to Ollama's local API endpoint:

```text
http://localhost:11434/api/generate
```

Model used:

```text
llama3.2
```

Temperature:

```text
0
```

Temperature is set to 0 to encourage more consistent and deterministic responses.

### 3. Keyword-Based Scoring

The generated answer is checked against the expected keywords.

The keyword coverage score is calculated using:

**Keyword Coverage (%) = (Matched Keywords / Total Expected Keywords) × 100**

### 4. Status Classification

| Score | Status |
|---|---|
| 60% or above | PASS |
| Below 60% | REVIEW |
| Request or execution failure | ERROR |

---

## Output

The program automatically generates:

```text
baseline_results.csv
```

The CSV file contains:

| Column | Description |
|---|---|
| Question_ID | Unique question identifier |
| Question | Original question |
| Expected_Answer | Expected answer |
| LLM_Answer | Generated answer from Llama 3.2 |
| Matched_Keywords | Keywords found in the response |
| Missing_Keywords | Keywords not found |
| Score | Keyword coverage percentage |
| Status | PASS, REVIEW, or ERROR |
| Source | Reference source URL |
| Model | Model used for evaluation |
| Release | Experiment release version |

The CSV file can be opened using Microsoft Excel for further analysis.

---

## Baseline Summary

After completing the evaluation, the program displays:

- Release Version
- Model Name
- Total Questions
- Successful Responses
- Passed Questions
- Questions for Review
- Failed Requests
- Average Keyword Coverage
- Evaluation Date

---

## Release Information

| Parameter | Value |
|---|---|
| Project | Generative AI Programming Practical |
| Week | 6 |
| Release | v0.1 |
| Model | Llama 3.2 |
| Evaluation | Keyword-Based Baseline |
| Dataset | Golden Question Set (30 Questions) |
| Execution | Local using Ollama |

---

## Conclusion

This project establishes the first baseline evaluation of Llama 3.2 using a predefined Golden Question Set. It measures the model's response quality through keyword coverage, records individual question results, and provides an overall evaluation summary.

The generated `baseline_results.csv` serves as the record of the first experiment, **Release v0.1**.

---

## Author

Created as part of the Week 6 Generative AI Programming Practical.
