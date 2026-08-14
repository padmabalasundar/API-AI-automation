# AI API Automation Suite (Python, Pytest, OpenAI)

A test automation framework built with Python, Pytest, and the OpenAI API. This repository demonstrates functional API testing, error handling, structured JSON schema validation, HTML reporting, and automated CI/CD execution using GitHub Actions.

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

## Features

- Functional API Testing: Validates chat completions and HTTP 200 responses.
- Negative Testing and Error Handling: Validates error responses including NotFoundError (404) and AuthenticationError (401).
- Structured Schema Validation: Enforces data types and required fields using Pydantic models with OpenAI Structured Outputs.
- Test Fixtures: Uses Pytest fixtures for client instantiation and configuration reuse.
- HTML Reporting: Generates standalone HTML execution reports using pytest-html.
- Automated CI/CD: Executes tests automatically on code push or pull request via GitHub Actions.

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