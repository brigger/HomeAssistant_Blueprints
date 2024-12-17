#!/usr/bin/env python3

import requests

# Replace these variables with your information
HA_URL = "http://homeassistant.local:8123"  # URL to your Home Assistant instance
TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiIzYzRhMGQ2MTllMTA0NmM3OWI3MzYwZTJmZGViYWY0MCIsImlhdCI6MTcwNzkyNzYxMCwiZXhwIjoyMDIzMjg3NjEwfQ.I9pr1jEJL6NHqK_FNkZUr6JMjXMranl7aFaVzd644Ik"
ENTITY_ID = "light.office_light"

headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json",
}

data = {
    "entity_id": ENTITY_ID
}

response = requests.post(f"{HA_URL}/api/services/light/turn_on", json=data, headers=headers)

print("Light turned on successfully.")
else:
print(f"Failed to turn on light. Status code: {response.status_code}")
