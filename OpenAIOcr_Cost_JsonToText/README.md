# 📄 JSON to Text Extraction Utility
JSON to Text Extraction Utility is a specialized tool designed to convert complex nested JSON data structures into human-readable text files. With recursive parsing capabilities and hierarchical formatting, this utility makes it easy to extract and view structured data in a more accessible format.
# 🧠 Technologies Used
</br>

 🔄 Recursive JSON Parsing

Purpose: Traverses complex nested JSON structures to extract all textual content.
Why: Handles arbitrarily deep nesting levels while maintaining the hierarchical relationship of data.
Implementation:
pythonCopydef extract_all_text_from_json(data, depth=0):
    text_lines = []
    indent = "    " * depth  # For better readability in output
    if isinstance(data, dict):
        for key, value in data.items():
            text_lines.append(f"{indent}{key}:")
            text_lines.extend(extract_all_text_from_json(value, depth + 1))
    elif isinstance(data, list):
        for idx, item in enumerate(data):
            text_lines.append(f"{indent}- Item {idx + 1}:")
            text_lines.extend(extract_all_text_from_json(item, depth + 1))
    elif isinstance(data, str):
        text_lines.append(f"{indent}{data}")
    elif isinstance(data, (int, float)):
        text_lines.append(f"{indent}{data}")
    return text_lines


 📂 Batch Processing

Purpose: Processes multiple JSON files in a single operation.
Why: Increases efficiency when working with collections of JSON documents.
Implementation:
pythonCopydef process_all_json_files(input_dir, output_dir):
    for file_name in os.listdir(input_dir):
        if file_name.lower().endswith('.json'):
            json_path = os.path.join(input_dir, file_name)
            extract_text_from_json(json_path, output_dir)


 📋 Formatted Output

Purpose: Generates well-formatted, indented text for readability.
Why: Preserves hierarchical structure of the original JSON data in the text output.
Feature: Automatic indentation based on nesting depth for improved readability.

 📁 Intelligent File Organization

Purpose: Creates a logical directory structure for output files.
Why: Keeps related outputs organized and easily accessible.
Implementation:
pythonCopybase_name = os.path.splitext(os.path.basename(json_path))[0]
output_subdir = os.path.join(output_dir, base_name)
output_path = os.path.join(output_subdir, f"{base_name}.txt")
os.makedirs(output_subdir, exist_ok=True)


 ⚠️ Error Handling

Purpose: Provides robust error detection and reporting.
Why: Ensures the script continues operation even when individual files fail processing.
Implementation: Specific exception handling for common file operations and data parsing errors.

 🌐 Summary
This utility demonstrates effective techniques for:

Structured data transformation from JSON to readable text
Hierarchical data preservation through intelligent formatting
Batch processing of multiple files
Clean file organization with automatic directory creation
Robust error handling for production-ready operation
<br/>

# <b> ⚠️ Notes
This project uses OpenAI's Vision model (gpt-4o) to extract structured data from images (e.g., scanned handwriting or printed documents) and calculate the estimated cost of the API usage.

Add your OpenAI API Key: Replace the empty string in the following line in main() with your actual key:

<pre>
    client = OpenAI(api_key="your-api-key-here")
</pre> </b>
