from flask import Flask, render_template, request
from github_utils import fetch_repo_metadata, fetch_contributors, fetch_commits, analyze_commit_activity
import re
from datetime import datetime

app = Flask(__name__)

@app.template_filter('format_date')
def format_date(value, fmt='%Y-%m-%d %H:%M'):
    if isinstance(value, str):
        try:
            value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%SZ')
        except ValueError:
            return value
    return value.strftime(fmt)

def validate_repo_url(url):
    patterns = [
        r'github\.com/([^/]+)/([^/]+)',
        r'^([^/]+)/([^/]+)$'
    ]
    for pattern in patterns:
        match = re.search(pattern, url.strip('/'))
        if match:
            return match.group(1), match.group(2)
    return None, None

@app.route('/', methods=['GET', 'POST'])
def analyze_repo():
    if request.method == 'POST':
        owner, repo = validate_repo_url(request.form['repo_url'])
        if not owner or not repo:
            return render_template('index.html', error='Invalid GitHub URL format')
        data = {'repo_url': f"https://github.com/{owner}/{repo}"}
        metadata = fetch_repo_metadata(owner, repo)
        if 'error' in metadata:
            return render_template('index.html', error=metadata['error'])
        data.update(metadata)
        contributors = fetch_contributors(owner, repo)
        if isinstance(contributors, list):
            data['contributors'] = contributors[:10]
        commits = fetch_commits(owner, repo)
        if isinstance(commits, list):
            data['commits'] = commits[:10]
            data['commit_activity'] = analyze_commit_activity(commits)
        return render_template('index.html', data=data)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)