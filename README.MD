# QA Automation – Selenium & Pytest

## Project Overview

This project is a simple **demo login web application** created for QA automation practice.

The application is not a real production system. It provides a login page, and after a successful login, the user is redirected to a dashboard containing static, fictional data.

The project includes:

* A **System Requirements Document** describing how the application should work.
* Automated **positive and negative test cases** written in Python using Selenium.
* Black-box testing designed to validate the application against the defined requirements.
* Test execution and reporting using **pytest**.

---

## Project Structure

```text
.
├
│
├── tests/
│   ├── positive_test.py
│   └── negative_test.py
|   ├── conftest.py
|   └── values.py
├── test site/
│   ├── requirements/
│       ├── Software_Requirements.md
│   ├── app/
│       ├── app.js
│       ├── dashboard.html
│       ├── aindex.html
|       └── style.css

```

---

## Python & Pytest

The tests are executed using **pytest**.

Pytest works somewhat differently from running a regular Python script. It automatically discovers test files and test functions based on naming conventions.

For example:

* Test files can be named `test_*.py` or `*_test.py`
* Test functions can be named `test_*`

This allows pytest to automatically discover and execute the tests.

### `conftest.py`

This file contains reusable **fixtures and setup functions**.

Instead of defining the same setup logic inside every test function, it can be defined once in `conftest.py` and reused across the test suite.

### `values.py`

This file contains shared **configuration values and test data**.

Keeping these values in one place makes the test code easier to maintain and avoids duplicating the same data across multiple test files.

---

## Tests

The test suite is divided into two main categories according to the system requirements:

### `positive_test.py`

Contains positive test cases that verify that the application behaves correctly when valid input is provided.

### `negative_test.py`

Contains negative test cases that verify that the application correctly handles invalid input and unexpected scenarios.

The test functions use different sets of input values, allowing the same test logic to be executed multiple times with different test data.

---

## Results

### STD

The **System Test Document (STD)** describes:

* What is being tested
* Test objectives
* Test steps
* Test environment
* Expected results
* Actual results

It serves as the basis for validating the application against its requirements.

STD: https://docs.google.com/spreadsheets/d/1P_9KhZFZuKIEkA3hC6gEskjQlyBUuG7la9QmSw2AZWY/edit?usp=sharing

### `report.html`

An HTML test report generated after running the automated test suite.

The report contains information about:

* Executed tests
* Passed tests
* Failed tests
* Test execution results

---

## Testing Approach

The project uses a **black-box testing approach**.

The tests focus on the application's externally observable behavior rather than its internal implementation.

The goal is to verify that the application meets the defined requirements by covering both:

* ✅ Valid scenarios
* ❌ Invalid scenarios

---

## Running the Tests

Install the required dependencies and run the test suite with:

```bash
pytest
```

TO run the test with realtime logs:

```bash
pytest -v
```

To generate an HTML report:

```bash
pytest --html=results/report.html
```

The generated report can then be opened in a web browser.

---

## Technologies

* **Python**
* **Selenium WebDriver**
* **Pytest**
* **HTML**
* **Black-box testing**

---

## Project Goal

The main goal of this project is to demonstrate practical experience with:

* Test case design
* Positive and negative testing
* Requirements-based testing
* Selenium WebDriver
* Pytest
* Test fixtures
* Test data management
* Automated test execution
* HTML test reporting
* Black-box testing
