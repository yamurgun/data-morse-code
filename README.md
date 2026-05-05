# 🚀 Morse Code Encoder & Decoder

## 📌 Overview
This project implements a fully functional Morse Code Encoder and Decoder in Python. It converts human-readable text into Morse code and decodes it back into text using clean, modular, and test-driven development practices.

## 🧠 Key Highlights
- Built a bidirectional encoding system (text ↔ Morse)
- Used modular architecture (separate encoder and decoder modules)
- Achieved 100% passing test coverage using Pytest
- Implemented efficient dictionary-based mapping
- Wrote clean, readable, and maintainable Python code

## ⚙️ Features
- Encode plain text into Morse code
- Decode Morse code back into text
- Letters separated by spaces
- Words separated using `|`
- Case-insensitive processing
- Ignores unsupported characters

## 🛠️ Tech Stack
- Python
- Pytest (unit testing)
- Pylint (code quality)

## 🧪 Example Usage

### Encoding
```python
encode("Hello World")
# Output:
".... . .-.. .-.. ---|.-- --- .-. .-.. -.."
```

### Decoding
```python
decode(".... . .-.. .-.. ---|.-- --- .-. .-.. -..")
# Output:
"HELLO WORLD"
```

## 🧩 Project Structure
```
morse/
├── encoder.py     # text → Morse
├── decoder.py     # Morse → text
├── mapping.py     # dictionary mapping
```

## 🧪 Testing
Run all tests:
```bash
pytest -v
```

✔️ All tests pass  
✔️ Code quality rated 10/10 with Pylint  

## 📚 What I Learned
- Breaking complex problems into smaller functions
- Using dictionary mappings effectively
- Implementing encoding & decoding logic
- Writing modular and testable Python code
- Running targeted tests with Pytest

## 💡 Why This Project Matters
This project demonstrates strong fundamentals in problem-solving, clean code practices, and test-driven development. It reflects real-world data transformation scenarios such as communication protocols and data processing systems.

## 🔗 Author
Yağmur Güner
