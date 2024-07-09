import os
import time
import json
import re
from greptile_utils import submit_repo_for_indexing, check_indexing_status, query_codebase

def load_rules():
    with open('compliance_rules.json') as f:
        rules = json.load(f)
    return rules

def analyze_code(file_content, rules):
    violations = []
    lines = file_content.split('\n')
    for line_no, line in enumerate(lines, start=1):
        for rule in rules['rules']:
            if re.search(rule['pattern'], line):
                violations.append({
                    'line': line_no,
                    'rule_id': rule['id'],
                    'description': rule['description'],
                    'severity': rule['severity']
                })
    return violations

def load_remediation_suggestions():
    with open('remediation_suggestions.json') as f:
        suggestions = json.load(f)
    return suggestions

def provide_remediation(violations, suggestions):
    for v in violations:
        suggestion = suggestions.get(v['rule_id'])
        if suggestion:
            v['remediation'] = suggestion['suggestion']
            v['example'] = suggestion['example']
    return violations

def main():
    rules = load_rules()
    suggestions = load_remediation_suggestions()

    # Fetch codebase details using the Greptile API
    remote = 'github'
    repository = 'pallets/flask'
    branch = 'main'

    # Submit the repository for indexing
    indexing_response = submit_repo_for_indexing(remote, repository, branch)
    print('Indexing response:', indexing_response)

    repository_id = f'{remote}:{branch}:{repository}'

    # Wait for indexing to complete
    print("Waiting for indexing to complete...")
    while True:
        status_response = check_indexing_status(repository_id)
        print('Indexing status:', status_response)
        if status_response.get('status') == 'completed':
            print("Indexing completed.")
            break
        time.sleep(60)  # Check status every 60 seconds

    # Query the codebase to fetch file contents (example query)
    query_response = query_codebase("Fetch all files", repository_id)
    print(query_response)

    # Analyze the codebase for compliance
    all_violations = []
    for file in query_response.get('files', []):
        file_content = file['content']
        violations = analyze_code(file_content, rules)
        for v in violations:
            v['file'] = file['path']
        all_violations.extend(violations)

    # Provide remediation suggestions for the violations
    violations_with_remediation = provide_remediation(all_violations, suggestions)

    for v in violations_with_remediation:
        print(v)

if __name__ == "__main__":
    main()
