# mihi-sickness

Repeating over and over the same shitty task at the same shitty platform is sick. The current code is as shitty as the automated shit, PRs are welcome.

## How to run

**First:** Configure your environment.

```
pip install pytest-playwright
playwright install
```

**Second:** Set your credentials at `config.json` file

**Third:** Run a test file

```
pytest [--headed] <test_filename>
```

### test_bulk_attendance.py

This test will just submit all the days of the current month as they are.

### test_bulk_approve.py

Not fully working yet. The idea is to just approve all the pending items.
