# Lab 5 – Static Code Analysis

## Project: Fitness Club Class Booking Ledger

### Issues Identified and Fixed

| No. | Issue | Tool | Severity | Fix Applied |
|---|---|---|---|---|
| 1 | Mutable default argument | Pylint | Warning | Replaced [] with None |
| 2 | Bare exception handling | Pylint/Flake8 | Warning | Used specific exceptions |
| 3 | Unsafe shell command using os.system() | Bandit | High | Replaced with pathlib file operations |
| 4 | Missing file encoding | Pylint | Warning | Added UTF-8 encoding |
| 5 | File not properly closed | Pylint | Refactor | Used with open() |
| 6 | Incorrect class capacity condition | Manual inspection | Logic bug | Changed > to >= |
| 7 | Invalid function naming | Pylint | Convention | Changed addMembers() to add_members() |
| 8 | Missing docstrings | Pylint | Convention | Added module and function documentation |
| 9 | Incorrect dictionary iteration | Pylint | Convention | Used dictionary items() |
| 10 | Negative class capacity accepted | Manual inspection | Logic bug | Added capacity validation |
| 11 | Missing input validation | Manual inspection | Logic bug | Added guest count validation |

### Before and After Results

| Tool | Before | After |
|---|---|---|
| Pylint | 6.60/10 | 10.00/10 |
| Bandit | 1 High severity issue | 0 issues |
| Flake8 | 10 violations | 0 violations |

### Conclusion

Static code analysis helped identify code quality problems, insecure coding practices, formatting violations and logical errors. After applying the necessary corrections, the program achieved a Pylint score of 10/10, zero Bandit findings and zero Flake8 violations.