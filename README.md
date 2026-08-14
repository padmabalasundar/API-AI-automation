# AI API Automation Suite (Python, Pytest, OpenAI)

An AI API test automation framework built with Python, Pytest, and the OpenAI API. This repository demonstrates functional API testing, error handling, structured JSON schema validation, HTML reporting, and automated CI/CD execution using GitHub Actions.

---

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Setup and Installation](#setup-and-installation)
- [Environment Configuration](#environment-configuration)
- [Running Tests](#running-tests)
- [Generating HTML Reports](#generating-html-reports)
- [CI/CD Integration](#cicd-integration)
- [Security Information](#security-information)

---

## Problem Statement
Testing AI APIs is different from testing standard REST APIs. Modern AI integrations face five common challenges:

1.Unpredictable Answers: AI outputs change with every call, making exact-text checks unreliable.
2. Unstructured Responses: Applications need clean, strictly typed JSON data, not long prose.
3. Security & Cost Risks: Leaked API keys can cause major security breaches and unexpected costs.
4. Frequent API Failures: Endpoints can fail due to rate limits, invalid keys, or deprecated models.
5. Poor Pipeline Visibility: Teams need instant visual reports in their CI/CD pipelines to catch breaking changes early.

## How This Project Solves It
This framework uses Pytest, Pydantic, and GitHub Actions to solve these issues:

- Pydantic Data Schemas: Forces AI outputs into exact JSON types (strings, numbers, lists).
- Automated Exception Handling: Tests failure states (like 401 or 404 errors) without crashing the suite.
- Secure Secret Management: Keeps API keys safe locally and in GitHub Actions.
- Visual HTML Reports: Generates easy-to-read execution reports automatically on every code push.
---

## Project Structure

```text
AI-API-Automation/
│
├── .github/
│   └── workflows/
│       └── api-tests.yml        # GitHub Actions workflow configuration
│
├── .env                         # Local environment variables (DO NOT COMMIT)
├── .gitignore                   # Version control ignore rules
├── api-ai-automation.py         # Pytest test suite implementation
├── README.md                    # Repository documentation
└── requirements.txt             # Python dependency list
```

## Prerequisites
Before running this project, ensure you have the following installed:

Python 3.10 or higher
Git
An active OpenAI API Key

## Quick Start: Clone and Run
Follow these step-by-step instructions to get the test suite running locally.

### Step 1: Clone the Repository
```
git clone https://github.com/padmabalasundar/API-AI-automation.git
cd API-AI-automation
```

### Step 2: Set Up Virtual Environment
On Windows (PowerShell):
```
python -m venv venv
.\venv\Scripts\activate
```
On macOS or Linux:

```
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```
pip install -r requirements.txt
```
(If requirements.txt is not yet created in your local environment, install directly:)

```
pip install openai python-dotenv pytest pytest-html pydantic
```
### Step 4: Configure Environment Variables
Create a .env file in the root directory of the project:

```
touch .env
```
Open the .env file and add your OpenAI API Key:

```
OPENAI_API_KEY=sk-proj-your-actual-openai-api-key-here
```

### Step 5: Execute the Test Suite
Run all tests in verbose mode:

```
pytest api-ai-automation.py -v
```
### Run tests with console output logging enabled:

```
pytest api-ai-automation.py -v -s
```
### Generating HTML Reports
To generate a standalone visual report after test execution, run:

```
pytest api-ai-automation.py --html=report.html --self-contained-html
```
After execution finishes, open report.html in your web browser to review overall execution status, execution duration per test, and error tracebacks.

## CI/CD Integration
This project includes a GitHub Actions workflow located at .github/workflows/api-tests.yml.

### Configuring GitHub Secrets
Navigate to your repository on GitHub.
Go to Settings > Secrets and variables > Actions.
Select New repository secret.
Set Name to OPENAI_API_KEY.
Set Value to your secret OpenAI API key.

### Accessing Test Reports in CI/CD
Open the Actions tab in GitHub.
Select the relevant workflow run.
Scroll to the Artifacts section at the bottom of the page.
Download pytest-html-report to view results locally.

## Security Information
Credentials Management: API keys are loaded locally using python-dotenv and injected into CI/CD environments using GitHub Secrets.

Version Control Hygiene: Local configuration files (.env), Python virtual environments (venv/), and Pytest caches (.pytest_cache/) are excluded from repository tracking via .gitignore

## Author Information

**PadmaBalasundar** - Developed as a comprehensive reference implementation and portfolio project demonstrating end-to-end automation, structured validation, and CI/CD integration for generative AI endpoints.

---