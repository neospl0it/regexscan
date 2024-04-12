# Regex Scan Tool

![Banner](config/banner.txt)

A command-line tool written in Go to scan webpages for potential leaked credentials using regex patterns.

## Features

- Detects common patterns indicative of leaked credentials within webpage content.
- Utilizes concurrency for faster scanning of multiple URLs.
- Displays results with colorized output for easy identification of potential issues.

## Installation

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/f141ne0/regexscan.git
   ```

2. Navigate to the project directory:
   ```bash
   cd regexscan
   ```

3. Ensure you have Go installed on your system.

## Usage

### 1. Prepare Configuration Files

Place the following files in the `config` directory relative to the project:

- `banner.txt`: Custom ASCII art banner to display at the beginning of the tool execution.
- `regex_patterns.txt`: Regex patterns used for detecting potential leaked credentials.

### 2. Run the Tool

Execute the tool by providing one or more URLs to scan:
```bash
go run main.go https://example.com 
```

The tool will scan each provided URL for potential leaked credentials based on the configured regex patterns.

## Customization

- **Regex Patterns**: Modify `regex_patterns.txt` to add, remove, or modify regex patterns based on specific credential formats to detect.
- **Banner**: Update `banner.txt` with a custom ASCII art banner to personalize the tool's output.

## Contributing

Contributions are welcome! If you have suggestions, feature requests, or want to report issues, please open an issue or pull request on GitHub.

## License

This project is licensed under the [MIT License](LICENSE).
