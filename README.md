# Webpage Leaked Credentials Checker

This Python script allows you to search for potential leaked credentials (e.g., passwords, API keys, tokens) in the content of a webpage using regex patterns. It's a handy tool for security assessments and monitoring web pages for sensitive information exposure.

## Prerequisites

- Python 3.x installed on your system
- `requests` library (`pip install requests`)
- `colorama` library (`pip install colorama`)

## Installation

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/f141ne0/regexscan.git
   ```

2. Install the required Python libraries:
   ```bash
   pip install requests colorama
   ```

## Usage

1. Add your desired regex patterns to the `regex_patterns.txt` file. Each pattern should be on a separate line.

2. Run the script `leaked_credentials_checker.py` with the target URL:
   ```bash
   python leaked_credentials_checker.py --url "https://example.com"
   ```

   Replace `"https://example.com"` with the URL of the webpage you want to scan.

3. The script will fetch the webpage content and search for potential leaked credentials based on the regex patterns provided in `regex_patterns.txt`.

## Regex Patterns

You can customize the regex patterns in the `regex_patterns.txt` file to match specific formats or keywords associated with leaked credentials. Refer to the provided sample patterns for common credential-related terms.

## Contributing

Contributions are welcome! If you have suggestions, improvements, or new features to add, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

---

**Disclaimer**: Use this tool responsibly and only on web pages that you have permission to test. Do not use it for illegal or unauthorized purposes.

