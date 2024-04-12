import requests
import re

def search_leaked_credentials(url, regex_pattern):
    try:
        # Make a request to the target URL
        response = requests.get(url)
        if response.status_code == 200:
            # Extract content from the response
            content = response.text
            
            # Search for leaked credentials using regex pattern
            matches = re.findall(regex_pattern, content, re.IGNORECASE)
            
            if matches:
                print("Potential leaked credentials found:")
                for match in matches:
                    print(match)
            else:
                print("No leaked credentials found.")
        else:
            print(f"Failed to retrieve content from {url}. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error occurred during request: {e}")

if __name__ == "__main__":
    # Prompt user to enter the target URL
    target_url = input("Enter the target URL: ")

    # Define your regex pattern for searching leaked credentials
    regex_pattern = r'((access_key|access_token|admin_pass|admin_user|algolia_admin_key|algolia_api_key|...)(=|>|:=|\|\|:|<=|=>|:).{0,5}[\'\"]([0-9a-zA-Z\-_=]{8,64})[\'\"])'

    # Call the function with the provided target URL and regex pattern
    search_leaked_credentials(target_url, regex_pattern)
