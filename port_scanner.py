import socket  # Import the socket library for networking

# Ask the user to input the target IP address or hostname
target = input("Enter target IP: ")

# Print a message to indicate scanning is starting
print(f"\n Scanning target {target}...\n")

# Loop through a range of port numbers (from 20 to 101 inclusive)
for port in range(20, 102): 
    # Create a new socket object using IPv4 (AF_INET) and TCP (SOCK_STREAM)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Set a default timeout of 1 second for each connection attempt
    socket.setdefaulttimeout(1)

    # Try to connect to the target IP and current port
    # connect_ex() returns 0 if successful, or an error code otherwise
    result = sock.connect_ex((target, port))

    # If connection is successful (port is open), print the port number
    if result == 0:
        print(f"Port {port} is open")

    # Close the socket to free system resources
    sock.close()

# After scanning all ports, print a completion message
print("Scan complete")
