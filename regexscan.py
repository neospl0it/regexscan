import argparse
import requests
import re
from colorama import init, Fore, Style

def read_regex_patterns_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            patterns = file.readlines()
            patterns = [pattern.strip() for pattern in patterns if pattern.strip()]
        return patterns
    except FileNotFoundError:
        print(f"Regex patterns file '{file_path}' not found.")
        return []
    except Exception as e:
        print(f"Error occurred while reading regex patterns: {e}")
        return []

def search_leaked_credentials(url, regex_patterns):
    try:
        # Make a request to the target URL
        response = requests.get(url)
        
        # Check if the request was successful
        if response.status_code != 200:
            print(f"Failed to retrieve content from {url}. Status code: {response.status_code}")
            return
        
        # Extract content from the response
        content = response.text
        
        # Search for leaked credentials using each regex pattern
        for regex_pattern in regex_patterns:
            matches = re.findall(regex_pattern, content, re.IGNORECASE)
            if matches:
                print(Fore.RED + f"Potential leaked credentials found using pattern '{regex_pattern}':")
                for match in matches:
                    # Print each match in red color
                    print(Fore.RED + f"  {match}")
                print(Style.RESET_ALL)  # Reset colorama styles
            else:
                print(f"No leaked credentials found using pattern '{regex_pattern}'.")
    except requests.exceptions.RequestException as e:
        print(f"Error occurred during request: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    # Initialize colorama to enable ANSI escape sequence support on Windows
    init(autoreset=True)

    # Define the path to the regex patterns file
    regex_patterns_file = 'regex_patterns.txt'

    # Read regex patterns from the specified file
    regex_patterns = read_regex_patterns_from_file(regex_patterns_file)
    
    if regex_patterns:
        # Parse command-line arguments (for URL)
        parser = argparse.ArgumentParser(description="Search for potential leaked credentials in a webpage.")
        parser.add_argument("--url", type=str, help="Target URL to search for leaked credentials", required=True)
        args = parser.parse_args()

        # Call the function with the provided target URL and regex patterns
        search_leaked_credentials(args.url, regex_patterns)
    else:
        print("No regex patterns loaded. Exiting.")

if __name__ == "__main__":
    main()
