#!/usr/bin/env python3

import requests

def is_url_alive(url):
        try:
            response = requests.get(url)
            # Consider any status code 200-299 to indicate success
            if 200 <= response.status_code < 300:
                return True
            else:
                return False
        except requests.exceptions.RequestException:
            return False


def main():

    # Example usage
    url_to_check = "http://192.168.31.13:8123"
    result = is_url_alive(url_to_check)
    print("HomeAssistant Luzern is up: "+str(result))  # This will print "true" if the URL is alive, otherwise "false"

    url_to_check = "http://192.168.32.5:8123"
    result = is_url_alive(url_to_check)
    print("HomeAssistant GrÃ¤chen is up: "+str(result))  # This will print "true" if the URL is alive, otherwise "false"


if __name__ == "__main__":
    main()