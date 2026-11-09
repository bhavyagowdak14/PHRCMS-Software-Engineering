# PHRCMS-Software-Engineering

## Patient Health Record Consent Management System (PHRCMS)

**Student:** BHAVYA K  
**SRN:** PES1UG24AM066  
**Course:** Software Engineering Lab  
**Department:** CSE (AIML)

---

## Project Overview

The **Patient Health Record Consent Management System (PHRCMS)** is a patient-centric electronic health data gateway that allows patients to explicitly manage **granular and time-bound consent permissions** for verified healthcare stakeholders such as clinic doctors and diagnostic laboratories.

The system enables patients to:

- Grant access to specific health records.
- Define time-bound access permissions.
- Revoke previously granted consent.
- Receive notifications before consent expiry.
- View a complete audit trail of consent and record-access activities.
- Ensure secure access to sensitive patient health information.

---

## Software Engineering Labs

This repository contains practical assignments and deliverables completed as part of the Software Engineering Lab course.

| Lab | Title | Description |
|---|---|---|
| Lab 1 | Requirements Engineering & UML Use-Case Modelling | Requirements documentation, UML use-case diagrams and use-case flow modelling. |
| Lab 2 | Agile Backlog & Sprint Simulation | Agile project planning, backlog management and sprint simulation using Jira. |
| Lab 3 | Component Modelling & Architectural Pattern Selection | Component diagrams and architectural design justification. |
| Lab 4 | Target Shooting Game | Development of a Python-based target shooting game using modular components. |
| Lab 5 | Static Code Analysis | Python code analysis, issue identification and correction using Pylint, Bandit and Flake8. |
| Lab 6 | Code and Branch Coverage Analysis | Writing and executing pytest test cases to measure line coverage and branch coverage using Python Coverage.py. |
| Lab 7 | Fuzz Testing for Input Validation Bugs | Applying property-based fuzz testing using Hypothesis to identify input validation bugs and improve application robustness. |

---

## Repository Structure

```text
PHRCMS-Software-Engineering/
│
├── Lab-1_Requirements_Engineering_UML/
│   ├── 01_Requirements_Table.pdf
│   ├── 02_UML_Use_Case_Diagram.pdf
│   ├── 03_Use_Case_Flow_Request_Record_Access.pdf
│   └── 04_Complete_Lab1_Report.pdf
│
├── Lab-2_Agile_Backlog_Sprint_Simulation/
│   ├── 01_Lab2_Jira_Reflection.docx
│   └── 02_Lab2_Jira_Reflection.pdf
│
├── Lab-3_Component_Modeling_Architecture/
│   ├── 01_Lab3_Component_Diagram.png
│   ├── 02_Lab3_Architecture_Justification.pdf
│   └── README.md
│
├── Lab-4_Target_Shooting/
│   └── target-shooting/
│       ├── main.py
│       ├── requirements.txt
│       ├── README.md
│       └── game/
│           ├── game_engine.py
│           ├── target.py
│           ├── hit_detection.py
│           └── renderer.py
│
├── Lab-5_Static_Code_Analysis/
│   ├── gym_system.py
│   ├── issues.md
│   ├── pylint_before.txt
│   ├── pylint_after.txt
│   ├── bandit_before.txt
│   ├── bandit_after.txt
│   ├── flake8_before.txt
│   └── flake8_after.txt
│
├── Lab 6/
│   ├── README.md
│   ├── .gitignore
│   ├── shipping_quote.py
│   ├── test_shipping_quote.py
│   ├── CodeCoverageTest_shipping_quote.py
│   ├── BranchCoverageTest_shipping_quote.py
│   ├── Code_Coverage.png.png
│   └── Branch_Coverage.png.png
│
├── Lab 7/
│   ├── processor.py
│   ├── processor_buggy.py
│   ├── test_processor.py
│   ├── Buggy_Application.png
│   ├── Failing_Tests.png
│   ├── Fixed_Application.png
│   └── Passing_Tests.png
│
└── README.md
```

---

## Lab Descriptions

### Lab 1 – Requirements Engineering & UML Use-Case Modelling

- Identification and documentation of software requirements.
- Preparation of UML use-case diagrams.
- Modelling use-case flows for the PHRCMS project.

### Lab 2 – Agile Backlog & Sprint Simulation

- Agile project planning and sprint management.
- Creation and management of product backlogs.
- Sprint simulation using Jira.

### Lab 3 – Component Modelling & Architectural Pattern Selection

- Preparation of software component diagrams.
- Identification of system components and their interactions.
- Selection and justification of architectural patterns.

### Lab 4 – Target Shooting Game

- Development of a Python-based target shooting game.
- Implementation of modular game components.
- Separation of game engine, target management, hit detection and rendering.

### Lab 5 – Static Code Analysis

- Analysis of Python source code using static analysis tools.
- Identification and correction of code quality issues.
- Comparison of analysis reports before and after corrections.
- Tools used: Pylint, Bandit and Flake8.

### Lab 6 – Code and Branch Coverage Analysis

- Implementation of test cases using pytest.
- Measurement of line coverage and branch coverage using Coverage.py.
- Testing different execution paths, conditions and edge cases.
- Generation of coverage reports to evaluate test completeness.

**Coverage Results:**
- Code Coverage: 100%
- Branch Coverage: 100%

**Tools Used:** Python, pytest, Coverage.py.

### Lab 7 – Fuzz Testing for Input Validation Bugs

- Application of property-based fuzz testing using Hypothesis.
- Identification of input validation bugs in Python functions.
- Testing unexpected, malformed and invalid inputs.
- Improving application robustness through defensive programming.
- Comparison of buggy and fixed application behaviour.
- Verification of fixes using Hypothesis-based tests.

**Functions Tested:**
- `calculate_dimensional_weight()`
- `format_tracking_label()`
- `parse_package_manifest()`

**Tools Used:** Python, Hypothesis, pytest.

---

## Technologies and Tools

| Category | Technologies / Tools |
|---|---|
| Programming Languages | Python |
| Requirements & Modelling | UML |
| Agile Project Management | Jira |
| Architecture Modelling | Component Diagrams |
| Static Code Analysis | Pylint, Bandit, Flake8 |
| Test Automation | pytest |
| Code Coverage | Coverage.py |
| Fuzz Testing | Hypothesis |
| Version Control | Git, GitHub |

---

## Repository Purpose

This repository serves as a collection of Software Engineering Lab assignments, including source code, technical documentation, diagrams, reports, testing implementations and practical experiments completed throughout the course.
