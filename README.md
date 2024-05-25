# Regexscan

Regexscan is a simple bash script designed to search for leaked credentials in the content of a given URL. It uses regex patterns to identify common credential formats that might be exposed.

## Features

- Fetches content from a specified URL.
- Searches for a wide range of potential leaked credentials using regex.
- Supports a variety of credential formats including API keys, access tokens, passwords, and more.

## Requirements

- `curl`: Used to fetch the content from the URL.
- `grep`: Utilized to search the content using regex patterns.

## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/f141ne0/regexscan.git
    cd regexscan
    ```

2. Make the script executable:

    ```bash
    chmod +x regexscan.sh
    ```

3. Run the script with the `--url` parameter:

    ```bash
    ./regexscan.sh --url <url>
    ```

    Replace `<url>` with the URL you want to scan for leaked credentials.

## Example

```bash
./regexscan.sh --url https://example.com
```

Output will display any found credentials along with their context in the fetched content.

```bash
┌──(f141㉿neo)-[~/regexscan]
└─$ ./regexscan.sh --url https://ope******.gov.*n/
Searching for leaked credentials in https://ope******.gov.*n/...
apiKey: "A***SyCGXNhyQ_*************Q7VoZrVAw3GM"
```


## Regex Patterns

The script searches for a wide variety of credential formats including, but not limited to:

- API keys
- Access tokens
- Secret keys
- Passwords
- AWS keys
- Docker passwords

For a full list of patterns, see the `grep` command inside the script.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Disclaimer

This tool is intended for educational purposes and ethical testing only. Unauthorized scanning of systems without permission is illegal and unethical.

Feel free to customize the repository URL, add more sections if needed, or adjust the example commands and descriptions to better fit your project.
