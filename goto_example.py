import requests
import logging

# Set up logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

# URL and payload
url = "http://localhost:3000/goto"
payload = {
    "url": "https://browserleaks.com/javascript",
    "navigationOptions": {
        "timeout": 60000,
    },
    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
    "viewportOptions": {
        "width": 1920,
        "height": 1080,
        "deviceScaleFactor": 1,
    },
    "timezoneId": "America/New_York",
}

try:
    # Perform the POST request
    response = requests.post(url, json=payload)

    # Log the response code
    logging.info(f"Response Code: {response.status_code}")

    # Log the response output
    logging.info(f"Response Output: {response.json()}")

except requests.exceptions.RequestException as e:
    logging.error(f"Request failed: {e}")
