# Automated Code Compliance Checker

## Project Overview
This project is an Automated Code Compliance Checker that leverages the Greptile API to fetch and analyze codebase details, ensuring compliance with industry standards such as GDPR. It performs static code analysis to detect compliance violations and provides remediation suggestions.

## Setup Instructions
1. Clone the Flask repository:
    ```bash
    git clone https://github.com/aravindvengarai/flask.git
    cd flask
    ```

2. Create a new directory for the project and navigate into it:
    ```bash
    mkdir ../automated-code-compliance-checker
    cd ../automated-code-compliance-checker
    ```

3. Create the necessary files and directories as outlined in the project structure.

4. Add your Greptile API key and GitHub PAT to the `.env` file.

5. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

6. Run the main script:
    ```bash
    python main.py
    ```

## Usage
The main script (`main.py`) indexes the Flask repository using the Greptile API, fetches codebase details, analyzes the code for compliance violations, and provides remediation suggestions.

## Technical Details
- **compliance_rules.json**: Contains the compliance rules for analysis.
- **remediation_suggestions.json**: Provides remediation suggestions for detected violations.
- **greptile_utils.py**: Utility functions for interacting with the Greptile API.
- **main.py**: Main script to run the compliance checker.

## Feedback on Greptile API
The Greptile API provides a seamless way to fetch and analyze codebase details. The indexing and query endpoints are well-documented and easy to use.

## Ideas for Future Enhancements
- Integration with CI/CD pipelines for continuous compliance monitoring.
- Enhanced reporting and visualization of compliance status.
- Support for additional compliance standards.
