import argparse
import requests
import re
from colorama import init, Fore, Style

def search_leaked_credentials(url, regex_pattern):
    try:
        # Make a request to the target URL
        response = requests.get(url)
        
        # Check if the request was successful
        if response.status_code != 200:
            print(f"Failed to retrieve content from {url}. Status code: {response.status_code}")
            return
        
        # Extract content from the response
        content = response.text
        
        # Search for leaked credentials using regex pattern
        matches = re.findall(regex_pattern, content, re.IGNORECASE)
        
        if matches:
            print(Fore.RED + "Potential leaked credentials found:")
            for match in matches:
                # Print each match in red color
                print(Fore.RED + f"  {match}")
            print(Style.RESET_ALL)  # Reset colorama styles
        else:
            print("No leaked credentials found.")
    except requests.exceptions.RequestException as e:
        print(f"Error occurred during request: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Search for potential leaked credentials in a webpage.")
    parser.add_argument("--url", type=str, help="Target URL to search for leaked credentials", required=True)
    args = parser.parse_args()

    # Initialize colorama to enable ANSI escape sequence support on Windows
    init(autoreset=True)

    # Define your regex pattern for searching leaked credentials
    regex_pattern = r'(access_key|access_token|admin_pass|admin_user|algolia_admin_key|algolia_api_key).*?[\'\"]([0-9a-zA-Z\-_=]{8,64})[\'\"]'

    # Call the function with the provided target URL and regex pattern
    search_leaked_credentials(args.url, regex_pattern)

if __name__ == "__main__":
    main()
