# Requirements
* **Python:** Programming language.
* **Selenium:** Selenium libraries.
* **Pytest:** Python unitTest framework.
* **Pytest-html:** Pytest HTML reports.
* **Pytest-xdist:** Run tests parallel.
* **Openpyxl:** MS Excel support.
* **Allure-pytest:** To generate allure reports.

# Run test
###Run all test
```bash
pytest
```
### Run test
```bash
pytest -v -s
```

# Report
### Generate html report
```bash
pytest --html=report.html
```

###generate html report with log
```bash
pytest --html=report.html --capture sys
```