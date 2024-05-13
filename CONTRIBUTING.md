# Contributing Guidelines

Welcome to EduConnect! We appreciate your interest in contributing to our project. Before you get started, please take a moment to review the following guidelines.

## Purpose

EduConnect is an open-source project. Contributions from the community help improve the project and make it better for everyone. We welcome contributions in the form of bug fixes, feature enhancements, documentation improvements, and more.

## Code of Conduct

Please note that this project adheres to a [Code of Conduct](link-to-code-of-conduct.md) to ensure a welcoming and inclusive environment for all contributors. By participating in this project, you agree to abide by its terms.

## Getting Started

To contribute to EduConnect, you'll need to set up your development environment. Follow these steps:


Clone the repository using the following command

```bash
git clone github.com/itskindastrange/educonnect
# After cloning, move into the directory having the project files using the change directory command
cd EduConnect
```
Create a virtual environment where all the required python packages will be installed

```bash
# Use this on Windows
python -m venv env
# Use this on Linux and Mac
python3 -m venv env
```
Activate the virtual environment

```bash
# Windows
.\env\Scripts\activate
# Linux and Mac
source env/bin/activate
```
Install all the project Requirements
```bash
pip install -r requirements.txt
```
-Apply migrations and create your superuser (follow the prompts)
```bash
# apply migrations and create your database
python manage.py migrate

# Create a user with manage.py
python manage.py createsuperuser
```

Run the development server

```bash
# run django development server
python manage.py runserver
```


## How to Contribute

### Issues

Before creating a new issue, please search for existing issues to avoid duplicates. If you find an existing issue that matches yours, you can comment or provide additional information.

When creating a new issue, include the following details:
- Description of the issue
- Steps to reproduce (if applicable)
- Expected behavior
- Actual behavior

### Pull Requests

1. Fork the repository and create a new branch for your changes.
2. Make your changes and ensure they adhere to our coding standards and guidelines.
3. Write tests for new features or bug fixes.
4. Submit a pull request, including a clear title and description that references related issues (if any).

## Code Style and Formatting

We follow [coding style and formatting guidelines](link-to-guidelines.md) to maintain code consistency and readability. Please ensure your contributions adhere to these guidelines.

## Testing Guidelines

We encourage writing tests for new features and bug fixes. Follow our [testing guidelines](link-to-testing-guidelines.md) to ensure proper testing of your changes.

## Documentation

Clear and concise documentation is crucial. Update or create documentation for new features or changes. Follow our [documentation guidelines](link-to-documentation-guidelines.md) when writing documentation.

## Review Process

All pull requests will undergo a review process by our team. We'll provide feedback and suggestions for improvement. Contributors are expected to address feedback promptly and revise their pull requests accordingly.

## License

By contributing to EduConnect, you agree that your contributions will be licensed under the [project's license](link-to-license.md). Please review the licensing terms before contributing.

## Acknowledgments

We acknowledge and appreciate all contributions to EduConnect. Special thanks to our contributors for their valuable input and efforts.

## Feedback and Questions

If you have any questions or need further clarification, please [contact us](link-to-contact-info.md) or join our [community chat](link-to-community-chat.md).

Thank you for contributing to EduConnect!

