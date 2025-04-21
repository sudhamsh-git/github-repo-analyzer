# GitHub Repo Analyzer

A modern web application to visualize commit activity, contributors, and trends for any public GitHub repository. Built with Flask, Chart.js, and Docker for portability and reproducibility.

---

## 🚀 Features
- **Instant GitHub Insights:** Enter a public repo URL to view commit activity, top contributors, and trends.
- **Charts & Visuals:** Interactive graphs for commits by day, hour, weekday, and month (Chart.js).
- **Contributor Analysis:** See the most active contributors and recent commit messages.
- **Robust Error Handling:** Handles GitHub API rate limits and invalid URLs gracefully.
- **Fully Containerized:** Runs anywhere with Docker—no dependencies or setup headaches.
- **Windsurf-Accelerated:** Built and iterated rapidly using Windsurf AI coding tools.

---

## 🐳 Quickstart: Run with Docker

1. **Clone the repository:**
   ```sh
   git clone https://github.com/YOUR_USERNAME/github-repo-analyzer.git
   cd github-repo-analyzer
   ```
2. **Build the Docker image:**
   ```sh
   docker build -t github-repo-analyzer .
   ```
3. **Run the container:**
   ```sh
   docker run -p 5000:5000 github-repo-analyzer
   ```
4. **Open your browser:**
   Go to [http://localhost:5000](http://localhost:5000)

---

## 🧩 Codebase Structure
- **`app.py`** — Flask entry point; handles routing, user input, and result rendering.
- **`github_utils.py`** — All GitHub API logic and commit analysis (fetches repo info, contributors, and commits; computes activity stats).
- **`templates/index.html`** — Main HTML UI (Bootstrap + Chart.js for interactive charts).
- **`static/styles.css`** — Custom CSS for styling.
- **`requirements.txt`** — Python dependencies for the app.
- **`Dockerfile` / `.dockerignore`** — Containerization setup for reproducible builds.
- **`test_github_utils.py`** — Unit tests for GitHub API and analysis logic.
- **`Loom Video/`** — Demo video walkthrough (see below).

---

## 📝 Usage Instructions
1. Enter a public GitHub repository URL (e.g., `https://github.com/pallets/flask`).
2. Click **Analyze** to view:
   - Repository metadata
   - Top contributors
   - Commit activity charts (by day, hour, weekday, month)
   - Recent commits table
3. Invalid URLs or API errors are handled and displayed in the UI.

---

## ⚡️ Windsurf Usage
- Windsurf AI tools were used to scaffold the Flask app, generate Docker configs, and iterate rapidly.
- Automated code edits, bug fixes, and Dockerization for faster delivery.
- See the Loom video for a full walkthrough of Windsurf’s impact on the project.

---

## 📂 Loom Video
- Demo video included in the `Loom Video/` folder:
  - **GitHub Repository Analyzer Demo.mp4** — Walkthrough of the app’s features, codebase, Docker usage, and Windsurf workflow.

---

## 🛠️ Developer Notes
- For higher GitHub API rate limits, set a `GITHUB_TOKEN` environment variable (see code comments in `github_utils.py`).
- Project is fully open-source and ready for CI/CD or cloud deployment.
- Contributions and feedback welcome!

---

## 📜 License
MIT License — see `LICENSE` file (if present).
