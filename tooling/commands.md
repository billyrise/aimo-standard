# Commands

## Local Setup
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -r requirements.txt
```

## Serve
```bash
mkdocs serve
```

## Lint
```bash
python tooling/checks/lint_i18n.py
python tooling/checks/lint_schema.py
pytest -q
```

## Versioned Deploy with mike (GitHub Pages branch deployment)

### Current (working) -> alias "latest"
```bash
mike deploy dev latest --update-aliases
mike set-default latest
mike list
```

### Release version snapshot (example: 0.1.0)
```bash
mike deploy 0.1.0 latest --update-aliases
mike set-default latest
mike list
```

**Note:**
- Actual pushing to gh-pages is handled by CI in workflows.

## GitHub Initial Push

### First-time repository setup

```bash
# Navigate to repository root
cd /path/to/aimo-standard

# Initialize git (if not already done)
git init

# Add all files
git add .

# Create initial commit
git commit -m "chore: bootstrap aimo standard docs-as-code pipeline"

# Rename branch to main
git branch -M main

# Add remote (replace <ORG> with your GitHub organization/username)
git remote add origin https://github.com/<ORG>/aimo-standard.git

# Push to GitHub
git push -u origin main
```

**Important:**
- Replace `<ORG>` with your actual GitHub organization or username
- Ensure you have write access to the repository
- After pushing, GitHub Actions will automatically build and deploy to `gh-pages` branch
