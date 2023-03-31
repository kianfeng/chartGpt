# YOUR_PROJECT_NAME

YOUR_PROJECT_DESCRIPTION

## Table of Contents

- [Installation](#installation)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Resources](#resources)
- [Contributing](#contributing)

## Installation

This project uses [Poetry](https://python-poetry.org/) for dependency management and packaging. To get started, make sure you have Python 3.7+ and Poetry installed on your system.

1. Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_PROJECT_NAME.git
cd YOUR_PROJECT_NAME
# Install the project dependencies:
poetry install
# Activate the virtual environment:
poetry shell

```

## Usage
After installing the dependencies and activating the virtual environment, you can run the project using:

```shell
aws configure   # configure your aws credentials
poetry run uvicorn src.main:app --reload # run the project
```
http://127.0.0.1:8000/docs

## Resources
1. [Poetry Documentation](https://python-poetry.org/docs/)
2. [fastapi best practices](https://fastapi.tiangolo.com/tutorial/best-practices/)

## Contributing
Contributions are welcome! Please open an issue or submit a pull request on the project's GitHub repository.
