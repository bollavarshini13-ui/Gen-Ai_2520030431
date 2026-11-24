# LLM Feature Token Budget Calculator

A lightweight Python tool for **planning the token economics of a GenAI feature before you build it**. Enter your expected traffic, token usage, model pricing, and provider limits, and the tool estimates daily and monthly cost, peak request and token rates, and tells you whether the plan fits within your budget and rate limits.

---

## Features

- **Token estimates**: daily input, output, and total tokens.
- **Cost estimates**: daily and monthly cost in USD (monthly is calculated as daily cost x 30).
- **Safety margin**: adds a configurable buffer (default 20%) on top of your estimates.
- **Capacity checks**: compares peak requests per minute (RPM) and tokens per minute (TPM) against provider limits.
- **Budget checks**: compares estimated costs against your daily and monthly budgets.
- **Clear verdict**: prints `PASS` or `REVIEW` for each check, with an overall recommendation.
- **Input validation**: rejects negative usage assumptions and negative safety margins.
- **Unit tests**: included for cost, capacity, and budget logic.

---

## Project Structure

```
.
├── budget.py           # FeatureBudget class and CLI report
├── test_budget.py      # Unit tests
├── requirements.txt    # Dependencies
├── .env                # Your planning assumptions (not committed)
└── README.md
```

---

## Requirements

- Python 3.8+
- `python-dotenv`

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

Create a `.env` file in the project root with your assumptions:

```env
REQUESTS_PER_DAY=1000
AVG_INPUT_TOKENS=1000
AVG_OUTPUT_TOKENS=500
PEAK_REQUESTS_PER_MINUTE=10

INPUT_PRICE_PER_MILLION=1.0
OUTPUT_PRICE_PER_MILLION=2.0

RPM_LIMIT=100
TPM_LIMIT=50000

DAILY_BUDGET_USD=5
MONTHLY_BUDGET_USD=100

SAFETY_MARGIN_PERCENT=20
```

| Variable | Description |
|---|---|
| `REQUESTS_PER_DAY` | Expected number of LLM calls per day |
| `AVG_INPUT_TOKENS` | Average input (prompt) tokens per request |
| `AVG_OUTPUT_TOKENS` | Average output (response) tokens per request |
| `PEAK_REQUESTS_PER_MINUTE` | Highest expected requests in a single minute |
| `INPUT_PRICE_PER_MILLION` | Model price (USD) per 1M input tokens |
| `OUTPUT_PRICE_PER_MILLION` | Model price (USD) per 1M output tokens |
| `RPM_LIMIT` | Provider's requests-per-minute limit |
| `TPM_LIMIT` | Provider's tokens-per-minute limit |
| `DAILY_BUDGET_USD` | Maximum daily spend you are willing to allow |
| `MONTHLY_BUDGET_USD` | Maximum monthly spend you are willing to allow |
| `SAFETY_MARGIN_PERCENT` | Extra buffer added to peak load and cost (default `20`) |

All values default to `0` if not set, except the safety margin, which defaults to `20`.

> **Tip:** use the current pricing and rate limits from your provider's documentation, since these change over time.

---

## Usage

```bash
python budget.py
```

### Example output (using the sample values above)

```
TOKEN ECONOMICS REPORT
-----------------------------------
Input tokens/day:  1,000,000
Output tokens/day: 500,000
Total tokens/day:  1,500,000
Estimated daily cost:   $2.0000
Estimated monthly cost: $60.00
Peak RPM with margin: 12.0
Peak TPM with margin: 18000

CHECKS
RPM capacity: PASS
TPM capacity: PASS
Daily budget: PASS
Monthly budget: PASS

Recommendation: WITHIN configured planning limits.
```

### Use it in your own code

```python
from budget import FeatureBudget

budget = FeatureBudget(
    requests_per_day=1000,
    avg_input_tokens=1000,
    avg_output_tokens=500,
    peak_requests_per_minute=10,
    input_price_per_million=1.0,
    output_price_per_million=2.0,
    rpm_limit=100,
    tpm_limit=50000,
    monthly_budget_usd=100,
    daily_budget_usd=5,
    safety_margin_percent=20,
)

print(budget.calculate())
```

---

## How the Calculations Work

```
input_tokens_day  = requests_per_day x avg_input_tokens
output_tokens_day = requests_per_day x avg_output_tokens

daily_cost   = (input_tokens_day x input_price + output_tokens_day x output_price) / 1,000,000
monthly_cost = daily_cost x 30

margin   = 1 + safety_margin_percent / 100
peak_rpm = peak_requests_per_minute x margin
peak_tpm = peak_requests_per_minute x (avg_input_tokens + avg_output_tokens) x margin
```

The checks compare:

- `peak_rpm` against `RPM_LIMIT`
- `peak_tpm` against `TPM_LIMIT`
- `daily_cost x margin` against `DAILY_BUDGET_USD`
- `monthly_cost x margin` against `MONTHLY_BUDGET_USD`

If any check fails, the tool recommends revising your assumptions, limits, or design before building.

---

## Running Tests

```bash
python -m unittest test_budget.py
```

The tests cover cost estimates, capacity checks, and failing RPM and monthly budget scenarios.

---

## Tech Stack

- Python
- `python-dotenv`
- `unittest`

---

## License

This project is licensed under the [MIT License](LICENSE). Add a `LICENSE` file to your repository, or change this section to the license you prefer.
