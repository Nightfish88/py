import requests
import urllib.parse

def download_favicon(url, size, save_path):
    domain = urllib.parse.urlparse(url).netloc
    favicon_url = f"https://www.google.com/s2/favicons?domain={domain}&sz={size}"
    response = requests.get(favicon_url)
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print(f"Favicon downloaded successfully and saved at {save_path}")
    else:
        print("Failed to download favicon")

# Example usage
# Put desired url below to download favicon
url = "https://apps.moonbeam.network/moonbeam"
size = 32
filename = urllib.parse.urlparse(url).netloc + ".ico"
save_path = fr"C:\Users\Efim\Desktop\favicons\{filename}"
download_favicon(url, size, save_path)