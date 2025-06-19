## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/Veltaliar/ing-zadanie-techniczne.git
   cd ing-zadanie-techniczne
   ```

2. Create virtual environment

   ```bash
   python -m venv .venv
   ```

3. Activate virtual environment
   ```bash
   cd .venv/Scripts
   ```

   ```bash
   activate
   ```

   ```bash
   cd ../..
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Install Playwright browsers:
   ```bash
   playwright install
   ```

## Running Test

You can run the test using the following command:
```bash
pytest --html=test_results/report.html --output=traces  --tracing=retain-on-failure --browser=chromium --browser=firefox --browser=webkit 
```

## Notes

Test fails in Github Actions due to captcha.