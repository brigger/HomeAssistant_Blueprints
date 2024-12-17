import requests

# Replace these variables with your actual Home Assistant details
HA_URL = 'http://your.homeassistant.ip:8123'  # Use HTTPS if your HA instance is secured
API_TOKEN = 'your_long_lived_access_token_here'

headers = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json",
}

def reboot_home_assistant():
    try:
        response = requests.post(f"{HA_URL}/api/services/homeassistant/restart", headers=headers)
        if response.status_code == 200:
            return "Home Assistant is rebooting..."
        else:
            return f"Failed to reboot Home Assistant. Status code: {response.status_code}"
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    message = reboot_home_assistant()
    print(message)
