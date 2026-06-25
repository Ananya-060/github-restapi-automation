# GitHub API Automation

A PyTest automation project that tests GitHub API endpoints for user profile, repository operations, and data-driven repo management.

## Features
- Retrieve GitHub user profile information
- List repositories associated with a user account
- Create a new GitHub repository
- Update repository details
- Delete a repository
- Generate HTML test execution report
- Execute automated test runs through Jenkins

## Tech Stack

- Python
- PyTest
- requests
- GitHub REST API
- Jenkins

## Project Structure

```text
project-root/
├── tests/
├── utils/
├── data/
├── reports/
├── requirements.txt
├── conftest.py
└── README.md
```

## Prerequisites

Before running the project, ensure you have:

- Python 3.x installed
- A GitHub personal access token with repo permissions
- Internet access to call the GitHub API

## Installation

1. Clone the repository

```bash
git clone <repository-url>
cd <repository-name>
```

2. Create and activate a virtual environment

```bash
python -m venv .venv
.venv\Scripts\activate
```
3. Install dependencies

```bash
pip install -r requirements.txt
```
## Test Data Setup

1. Copy test_data_example.json to data/test_data.json
2. Open data/test_data.json and fill in your values:
   - base_url: `https://api.github.com`
   - token: your GitHub personal access token
   - username: your GitHub username
   - new_repo.description: description for the new repo
   - new_repo.private: `false` or `true`
   - updated_repo.description: description for repo update

> data/test_data.json is ignored by .gitignore. Do not commit your token.


## Running Tests

Run all tests from the repository root:

```bash
pytest
```

Reports are generated automatically into the 'reports/' folder.

## Notes

- test_data_example.json is the sample data structure.
- data/test_data.json should contain your real credentials and test values.
- Keep your GitHub token private.
