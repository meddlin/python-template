# python-template

Template repo for Python projects using module architecture


## How to use this

- `main.py`: code goes here
- `tests/`: put tests in here

GitHub Actions for PyPi Distribution

- `.github/workflows/python-publish.yml`: Update with project name

*Optional*

- `FUNDING.yml`: Update this to your own, or delete the file completely

## Useful Commands

### Make a virtual environment (venv)

`python3 -m venv venv`

`source venv/bin/activate`

### Update `requirements.txt`

`pip freeze > requirements.txt`

### Install modules in development mode

`pip install -e .`

## Repo Protections

Consider the following features for hygiene and basic application security:

- branch protection
- Dependency Graph (Settings > Security | Advanced Security > Dependency Graph)
- Dependabot Alerts (Settings > Security | Advanced Security > Dependabot | Dependabot Alerts)

- Automatically delete head branches