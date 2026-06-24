# Selenium Python POM Automation Framework

A scalable, production-grade test automation framework built on the **Page Object Model (POM)** architecture using Python, Pytest, and Selenium WebDriver.

## Features
- Page Object Model (POM) design pattern for maintainability and reusability
- Data-driven testing with parameterized fixtures
- Allure HTML reporting with screenshots on failure
- Cross-browser support (Chrome, Firefox, Edge)
- GitHub Actions CI/CD integration
- Environment-based configuration via `.env`

## Tech Stack
| Layer | Technology |
|---|---|
| Language | Python 3.10+ |
| Framework | Pytest |
| Browser Automation | Selenium WebDriver |
| Driver Management | WebDriver Manager |
| Reporting | pytest-html + Allure |
| CI/CD | GitHub Actions |

## Project Structure
```
selenium-pom-framework/
├── pages/              # Page Object classes
│   ├── base_page.py    # Base class with shared actions
│   ├── login_page.py   # Login page object
│   ├── inventory_page.py
│   └── cart_page.py
├── tests/              # Test cases
│   ├── conftest.py     # Fixtures & setup
│   ├── test_login.py
│   └── test_inventory.py
├── utils/              # Utilities
│   ├── config.py       # Config loader
│   └── driver_factory.py
├── reports/            # Generated reports (gitignored)
├── .github/workflows/  # CI/CD pipeline
├── .env.example        # Environment variable template
├── pytest.ini
└── requirements.txt
```

## Setup & Run
```bash
# Clone and install
git clone https://github.com/hemanth361/selenium-pom-framework
cd selenium-pom-framework
pip install -r requirements.txt

# Copy env file
cp .env.example .env

# Run all tests
pytest

# Run with Allure
pytest --alluredir=allure-results
allure serve allure-results

# Run specific suite
pytest tests/test_login.py -v
pytest -m smoke
```

## Test Site
Tests run against [SauceDemo](https://www.saucedemo.com/) — an e-commerce demo site built for automation practice.
