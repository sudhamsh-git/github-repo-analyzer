# GitHub Repo Analyzer

A web application to visualize commit activity, contributors, and trends for any public GitHub repository.

## Features
- Upload a public GitHub repo URL and instantly visualize:
  - Commit frequency by hour and per day
  - Top contributors (pie chart)
  - Recent commits table
- Modern, responsive UI (Bootstrap + Chart.js)
- Handles GitHub API rate limits and errors gracefully

## Quickstart (Docker)

1. **Build the Docker image:**
   ```sh
   docker build -t github-repo-analyzer .
   ```
2. **Run the container:**
   ```sh
   docker run -p 5000:5000 github-repo-analyzer
   ```
3. **Open your browser:**
   Visit [http://localhost:5000](http://localhost:5000)

## Windsurf Usage
- Windsurf was used to optimize code edits, automate Dockerization, and streamline the build/test/deploy process.
- See the video demo for a walkthrough of how Windsurf accelerated development and improved reliability.

## Project Structure
- `app.py` - Flask backend
- `github_utils.py` - GitHub API logic and commit analysis
- `templates/index.html` - Main UI
- `static/styles.css` - Custom styles
- `requirements.txt` - Python dependencies
- `Dockerfile` / `.dockerignore` - Containerization

## Notes
- For higher GitHub API rate limits, set a `GITHUB_TOKEN` environment variable (see code comments).
- Demo video included for codebase walkthrough and Windsurf demonstration.
