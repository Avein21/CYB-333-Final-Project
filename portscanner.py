# Import the nmap module for port scanning
import nmap  
# Import datetime for getting timestamps
from datetime import datetime  

# Create an instance of the PortScanner
scanner = nmap.PortScanner()

# Ask the user for the target IP or domain
target = input("Enter the target IP or domain: ")

# Ask the user for the port range to scan
ports = input("Enter port range to scan (e.g., '22-80' or '80,443'): ")

# Print a message with the target and ports that will be scanned
print(f"Scanning {target} for ports: {ports}")

try:
    # Perform the port scan on the target with the specified ports
    # The scan results are stored in the 'scanner' object
    scanner.scan(target, ports)

    # Loop through all the hosts that responded
    for host in scanner.all_hosts():
        print(f"Host: {host}")
        print(f"State: {scanner[host].state()}")  # Show if the host is up or down

        # Loop through all protocols (TCP, UDP)
        for protocol in scanner[host].all_protocols():
            print(f"Protocol: {protocol}")

            # Get the list of open ports
            open_ports = scanner[host][protocol].keys()
            for port in open_ports:
                state = scanner[host][protocol][port]['state']  # Show the port state (open/closed)
                print(f"Port {port}: {state}")

except Exception as e:
    # If an error happens, print it
    print(f"Error: {e}")

# Print a timestamp at the end when the scan is done
print(f"Scan completed at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
