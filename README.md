# MD LLM Optimizer

**MD LLM Optimizer** is a Python tool to convert Markdown files into a compact, LLM-friendly format.  
It reduces token usage by simplifying Markdown syntax, converting tables to JSON, and removing unnecessary formatting.

## Features

- Strip Markdown headers and lists
- Convert links `[text](url)` to `text: url`
- Convert Markdown tables into JSON objects
- Remove extra blank lines and spaces
- CLI-based interface with English messages
- Ready for integration with LLM workflows

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/md-llm-optimizer.git
cd md-llm-optimizer
```

2. Create a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows
```

3. Install dependencies (if any; currently uses only standard library):
```bash
pip install -r requirements.txt
```


## Usage
```
python optimize.py input.md output.txt
```

### License

MIT License

