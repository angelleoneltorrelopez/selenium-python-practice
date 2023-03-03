<p align="center">
  <a href="https://www.selenium.dev/documentation/"><img src="https://upload.wikimedia.org/wikipedia/commons/d/d5/Selenium_Logo.png" width="150" height="150"/>
</a>
<a href="https://www.ingenieriazeros.com/">
<img src="https://1.bp.blogspot.com/-Q_GalsLLP0A/YYoUh73-MuI/AAAAAAAAMNc/OB4AIcWjB-UWJDKgH3c-kd0Syqt92lI-ACNcBGAsYHQ/s320/IMG_1169.PNG" 
width="150" height="150"></a>
</p>

# Description
This project is an automation test designed to demonstrate the use of the Selenium tool to perform automated tests on 
web applications and APIs. In this project, we use Pytest as a framework and Selenium WebDriver to automate interaction 
with a test web application.

# Requirements
* Python ^3.11.0

## Dependencies used
* **Selenium:** Selenium libraries.
* **webdriver_manager** Automatic driver download
* **Pytest:** Python unitTest framework.
* **Pytest-html:** Pytest HTML reports.
* **Pytest-xdist:** Run tests parallel.
* **Openpyxl:** MS Excel support.
* **Allure-pytest:** To generate allure reports.
* **requests:** For API testing

## Supported browsers
| Browser | OS                    |
|---------|-----------------------|
| Chrome  | Windows, Linux, MacOS |
| Firefox | Windows, Linux, MacOS |
| Edge    | Windows, Linux, MacOS |
| Safari  | MacOS                 |


## Create virtual environments
```bash
py -m venv "env" 
```

## Environmental settings
### Windows
```bash
env\Scripts\activate
```

## Installation
To install, follow the steps below:

1. Clone the repository from GitHub:
    ```bash
    git clone git@github.com:angelleoneltorrelopez/selenium-python-practice.git
    ```
2. Install the project dependencies using the package manager:
    ```bash
    pip install -r requirements.txt  
    ```

## PyCharm settings
https://www.jetbrains.com/help/pycharm/creating-virtual-environment.html#existing-environment

# Use
To use the software, follow the steps below:


## Run all test
```bash
pytest
```

## Run test
```bash
pytest -v -s
```

# Report
### Generate html report
```bash
pytest --html=report.html
```

### Generate html report with log
```bash
pytest --html=report.html --capture sys
```
