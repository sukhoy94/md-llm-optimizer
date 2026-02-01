import re
import json
import os

OUTPUT_DIR = "output"

def md_to_llm_optimized(md_content):
    # 1. Remove Markdown headers (convert to plain text)
    md_content = re.sub(r'^\s*#+\s*', '', md_content, flags=re.MULTILINE)

    # 2. Convert lists (-, *, +) to plain text
    md_content = re.sub(r'^\s*[-*+]\s+', '', md_content, flags=re.MULTILINE)

    # 3. Convert links [text](url) to "text: url"
    md_content = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'\1: \2', md_content)

    # 4. Convert Markdown tables to JSON
    tables = re.findall(r'(\|.+\|[\s\S]+?)(?=\n\n|$)', md_content)
    for table in tables:
        lines = [line.strip() for line in table.strip().split('\n') if line.strip()]
        if len(lines) < 2:
            continue
        headers = [h.strip() for h in lines[0].split('|')[1:-1]]
        data = []
        for row in lines[2:]:
            values = [v.strip() for v in row.split('|')[1:-1]]
            if len(values) == len(headers):
                data.append(dict(zip(headers, values)))
        md_content = md_content.replace(table, json.dumps(data, ensure_ascii=False))

    # 5. Remove extra blank lines
    md_content = re.sub(r'\n\s*\n', '\n', md_content)

    return md_content.strip()


def main():
    # Ensure output folder exists
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    # Ask user for input file
    while True:
        input_file = input("Enter the path to the Markdown file to optimize: ").strip()
        if not os.path.isfile(input_file):
            print("Error: File not found. Try again.")
            continue
        if not input_file.lower().endswith(".md"):
            print("Error: Only Markdown (.md) files are accepted.")
            continue
        break

    # Read input file
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            md_content = f.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    optimized_content = md_to_llm_optimized(md_content)

    # Determine output path
    filename = os.path.splitext(os.path.basename(input_file))[0] + "_optimized.txt"
    output_path = os.path.join(OUTPUT_DIR, filename)

    # Write optimized content
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(optimized_content)
        print(f"LLM-optimized content saved to: {output_path}")
    except Exception as e:
        print(f"Error writing file: {e}")


if __name__ == "__main__":
    main()
