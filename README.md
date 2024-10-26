# Rule_engine
Objective:
Develop a simple 3-tier rule engine application(Simple UI, API and Backend, Data) to determine
user eligibility based on attributes like age, department, income, spend etc.The system can use
Abstract Syntax Tree (AST) to represent conditional rules and allow for dynamic
creation,combination, and modification of these rules.
Data Structure:
● Define a data structure to represent the AST.
● The data structure should allow rule changes
● E,g One data structure could be Node with following fields
○ type: String indicating the node type ("operator" for AND/OR, "operand" for
conditions)
○ left: Reference to another Node (left child)
○ right: Reference to another Node (right child for operators)
○ value: Optional value for operand nodes (e.g., number for comparisons)

**
Here's a list of software required for the Rule Engine with AST project:

Programming Languages

1. Python 3.9+

Database

1. PostgreSQL 13+

Database Client

1. pgAdmin 4

AST Parsing Library

1. pyparsing

Data Validation Library

1. jsonschema

Testing Framework

1. Pytest

Code Editor/IDE

1. Visual Studio Code


Operating System

1. Windows 10+


Additional Tools

1. Docker (for containerization)


Installation Steps

1. Install Python 3.9+
2. Install PostgreSQL 13+
3. Install pgAdmin 4
4. Install pyparsing
5. Install jsonschema
6. Install Pytest: pip install pytest
7. Install Visual Studio Code
8. Install Docker
Verify Installations

1. Python: python --version
2. PostgreSQL: psql --version
3. pgAdmin: Open pgAdmin and connect to database
4. pyparsing: pip show pyparsing
5. jsonschema: pip show jsonschema
6. Pytest: pytest --version
