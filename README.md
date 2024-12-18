# CYB-333-Final-Project
This Python-based script is for scanning networks and web applications for vulnerabilities using Nmap. It detects open ports, services, and common security risks.

Requirements
 
    Python 3.x
  
    Nmap (installed on your system)
 
    python-nmap library (Python wrapper for Nmap)

Install Dependencies


    Before running the script, make sure to install the necessary libraries. You can install the required Python library using pip:

        pip install python-nmap

Also, ensure that Nmap is installed on your system. You can download it from here or install it via a package manager:

For macOS:
  
    brew install nmap

For Ubuntu/Debian:
  
    sudo apt-get install nmap

For Windows:
  
    Download the installer from the official Nmap website.

Usage

    Running the Script

      To run the script, simply execute it in your terminal or command prompt: python port_scanner.py

The script will prompt you for two inputs:
  
  Target IP or Domain: Enter the IP address or domain name you want to scan (e.g., 192.168.1.1 or example.com).
  
  Port Range: Enter the range of ports you want to scan (e.g., 22-80, 80,443).
  The script will then perform the scan and display the open ports for the given target, along with the status of each port and the host.

    Example
          Enter the target IP or domain: example.com
          Enter port range to scan (e.g., '22-80' or '80,443'): 22-80
          Scanning example.com for ports: 22-80
          Host: example.com
          State: up
          Protocol: tcp
          Port 22: open
          Port 80: open
          ...
          Scan completed at 2024-12-17 15:30:45

    Output
    The script will output the following information:
        Host: The IP or domain of the target.
        State: Whether the host is up or down.
        Protocol: The network protocol (e.g., TCP, UDP).
        Port: The open port numbers and their state (open or closed).

    Example Output
        Host: 192.168.1.1
        State: up
        Protocol: tcp
        Port 22: open
        Port 80: open
        Port 443: closed

Error Handling
If any error occurs during the scanning process (e.g., invalid target or incorrect port range), the script will catch it and print an error message.
  
  Error: nmap.nmap.NmapException: No such host is known
