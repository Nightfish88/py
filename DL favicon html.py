import requests
from bs4 import BeautifulSoup
import os

def download_favicon(url, save_directory):
    try:
        # Send a GET request to the website
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the HTML content
            soup = BeautifulSoup(response.content, 'html.parser')

            # Find the <link> tag with rel='icon' or 'shortcut icon'
            favicon_link = soup.find('link', rel=lambda value: value and any(x in value.lower() for x in ['icon', 'shortcut icon']))

            if favicon_link is not None:
                # Get the href attribute value of the <link> tag
                favicon_url = favicon_link['href']

                # Construct the absolute URL for the favicon
                absolute_url = urljoin(url, favicon_url)

                # Download the favicon
                response = requests.get(absolute_url)
                if response.status_code == 200:
                    # Extract the filename from the URL
                    filename = os.path.basename(absolute_url)

                    # Save the favicon to the specified directory
                    save_path = os.path.join(save_directory, filename)
                    with open(save_path, 'wb') as file:
                        file.write(response.content)
                    print("Favicon downloaded successfully!")
                else:
                    print("Failed to download favicon.")
            else:
                print("No favicon found.")
        else:
            print("Failed to fetch website content.")
    except requests.exceptions.RequestException as e:
        print("Error:", e)

# Example usage
url = "https://apps.moonbeam.network/moonbeam"
save_directory = r"C:\Users\Efim\Desktop\favicons"
download_favicon(url, save_directory)
