# Contributing to Ultima Client Art Tools

Thank you for your interest in contributing! Here's how you can help.

---

## 🛠️ How to Contribute

### 1. Fork the Repository
Click the **Fork** button at the top of this page.

### 2. Clone Your Fork
```bash
git clone https://github.com/YOUR_USERNAME/Ultima-Client-Art-Tools.git
cd Ultima-Client-Art-Tools
```

### 3. Create a Feature Branch
```bash
git checkout -b feat/your-feature-name
```

Use conventional naming:
- `feat/` — New feature
- `fix/` — Bug fix
- `docs/` — Documentation update
- `refactor/` — Code restructure

### 4. Make Your Changes
- Follow PEP 8 style guidelines
- Add docstrings to new functions
- Test your changes locally

### 5. Commit Your Changes
```bash
git add .
git commit -m "feat: add texmaps extractor"
```

Use clear, descriptive commit messages.

### 6. Push to Your Fork
```bash
git push origin feat/your-feature-name
```

### 7. Open a Pull Request
Go to the original repository and click **New Pull Request**.

---

## 📝 Code Style

- **Python 3.8+ type hints** where appropriate
- **Docstrings** for all public functions
- **PEP 8** formatting
- **tqdm progress bars** for long-running operations
- **Try/except** with proper error handling

---

## 🧪 Testing

Before submitting:

```bash
# Test extraction tools
python main.py art
python main.py land

# Check for import errors
python -m py_compile core/*.py tools/*.py
```

---

## 🐛 Reporting Bugs

Open an issue with:
- Python version
- OS and version
- ultimapy version
- Full error traceback
- Steps to reproduce

---

## 💡 Suggesting Features

Open an issue with:
- Clear description of the feature
- Use case / motivation
- Example usage (if applicable)

---

## ✅ Pull Request Checklist

Before submitting:

- [ ] Code follows PEP 8 style
- [ ] All functions have docstrings
- [ ] Changes tested locally
- [ ] No breaking changes (or documented if necessary)
- [ ] Updated README.md if needed
- [ ] Commit messages are clear

---

## 📧 Questions?

Open an issue with the **question** label or reach out to the maintainers.

Thank you for contributing! 🎉
