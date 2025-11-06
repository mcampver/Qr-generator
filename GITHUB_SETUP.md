# GitHub Setup Instructions

## Initial Setup

### 1. Initialize Git Repository

```bash
# Initialize git repository (if not already done)
git init

# Add all files
git add .

# Create initial commit
git commit -m "Initial commit: QR Business Card Generator"
```

### 2. Create GitHub Repository

1. Go to https://github.com/new
2. Repository name: `qr-business-card-generator` (or your choice)
3. Description: "Generate QR codes for business cards with custom logo"
4. Choose Public or Private
5. **DO NOT** initialize with README, .gitignore, or license (we already have these)
6. Click "Create repository"

### 3. Connect and Push

```bash
# Add remote repository (replace with your URL)
git remote add origin https://github.com/yourusername/qr-business-card-generator.git

# Push to GitHub
git branch -M main
git push -u origin main
```

## Repository Settings

### Topics (Tags)
Add these topics to your repository for better discoverability:
- `qr-code`
- `qr-generator`
- `business-card`
- `vcard`
- `python`
- `pillow`
- `contact-sharing`

To add topics:
1. Go to your repository on GitHub
2. Click the gear icon ⚙️ next to "About"
3. Add the topics listed above

### Description
Use this as your repository description:
```
Generate professional QR codes for business cards with custom logo overlay. Supports vCard format for easy contact sharing on iPhone and Android.
```

### Website
If you have a demo or website, add it here.

## Optional: Add GitHub Actions

Create `.github/workflows/python-app.yml` for automated testing:

```yaml
name: Python Application

on: [push, pull_request]

jobs:
  build:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.x'
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    - name: Test import
      run: python -c "from qr import TarjetaPresentacionQR; print('Import successful')"
```

## Optional: Add Badges

Add these to the top of your README.md:

```markdown
![GitHub stars](https://img.shields.io/github/stars/yourusername/qr-business-card-generator)
![GitHub forks](https://img.shields.io/github/forks/yourusername/qr-business-card-generator)
![GitHub issues](https://img.shields.io/github/issues/yourusername/qr-business-card-generator)
```

## Maintaining Your Repository

### Regular Updates

```bash
# After making changes
git add .
git commit -m "Description of changes"
git push
```

### Versioning

Use semantic versioning tags:

```bash
# Create a version tag
git tag -a v1.0.0 -m "Version 1.0.0"
git push origin v1.0.0
```

### Creating Releases

1. Go to your repository on GitHub
2. Click "Releases" → "Create a new release"
3. Choose your tag (e.g., v1.0.0)
4. Add release notes
5. Attach binaries if needed (e.g., Windows .exe)
6. Publish release

## Tips

- Enable "Issues" in repository settings for bug reports
- Enable "Discussions" for community questions
- Add a CHANGELOG.md to track version history
- Consider adding screenshots or GIF demos to README
- Star your own repository 😄

## Need Help?

- [GitHub Docs](https://docs.github.com)
- [Git Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf)
