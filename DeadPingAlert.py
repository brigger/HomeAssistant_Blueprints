#!/usr/bin/env python3

# Import the required functions from the modules
from PingURL import is_url_alive
from SendEmail2 import sendEmail

# Dictionary of IP addresses to check with their names
ip_addresses = {
    "HomeAssistant LUZERN": "http://192.168.31.13:8123",
    "HomeAssistant GRAECHEN": "http://100.89.26.117:8123"
}

# Initialize an empty message string for the detailed report
detailed_report = "Ping Status Report:\n"

# Initialize a list to hold unresponsive IPs with their names
unresponsive_ips = []

# Check each IP address, append the result to the detailed report, and track unresponsive IPs
for name, ip in ip_addresses.items():
    result = is_url_alive(ip)
    if result == True:
        #print(f"{name}  ({ip}) responded successfully.\n")
        detailed_report += f"{name} responded successfully.\n"
    else:
        #print(f"{name}  ({ip}) did not respond successfully.\n")
        detailed_report += f"{name} did not respond.\n"
        unresponsive_ips.append(f"{name}")

# Send the detailed report email
sendEmail(detailed_report, "Detailed report HomeAssistant Pings")

# Check if there are any unresponsive IPs and send a second email listing them
if unresponsive_ips:
    unresponsive_report = "The following server(s) did not respond: " + ", ".join(unresponsive_ips)
    sendEmail(unresponsive_report, "HomeAssistant unresponsive Pings")

print("DONE")
