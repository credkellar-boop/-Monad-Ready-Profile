from flask import Flask, render_template_string
import json
import os

app = Flask(__name__)

TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>MonadReady Dashboard</title>
</head>
<body>
    <h1>🔐 MonadReady Scan Report</h1>
    <p>Total Files Flagged: {{ total }}</p>

    {% for item in findings %}
        <div style="margin-bottom:20px;">
            <strong>{{ item.file }}</strong>
            <ul>
            {% for issue in item.issues %}
                <li>{{ issue.type }} ({{ issue.count }})</li>
            {% endfor %}
            </ul>
        </div>
    {% endfor %}
</body>
</html>
"""

@app.route("/")
def index():
    if not os.path.exists("../scan_report.json"):
        return "No report found. Run scanner first."

    with open("../scan_report.json") as f:
        data = json.load(f)

    return render_template_string(
        TEMPLATE,
        total=data["files_flagged"],
        findings=data["findings"]
    )

if __name__ == "__main__":
    app.run(debug=True)
