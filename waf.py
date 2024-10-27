from flask import Flask, request, abort

app = Flask(__name__)

# Define simple rules for detecting malicious patterns
BLOCKED_PATTERNS = [
    "SELECT * FROM",  # SQL Injection attempt
    "DROP TABLE",      # SQL Injection attempt
    "<script>",        # XSS attempt
    "eval(",           # Potential command execution attempt
]

def is_malicious(data):
    """Check if the request data contains malicious patterns."""
    for pattern in BLOCKED_PATTERNS:
        if pattern.lower() in data.lower():
            return True
    return False

@app.before_request
def filter_requests():
    """Filter incoming requests for malicious content."""
    # Check request method and data
    if request.method == 'POST':
        if is_malicious(request.form.to_json()):
            abort(403, description="Access Denied: Malicious content detected.")
    elif request.method == 'GET':
        if is_malicious(request.args.to_json()):
            abort(403, description="Access Denied: Malicious content detected.")

@app.route('/')
def index():
    return "Welcome to the Secure Web Application!"

@app.route('/submit', methods=['POST'])
def submit():
    return "Data submitted successfully!"

if __name__ == '__main__':
    app.run(port=5000, debug=True)
