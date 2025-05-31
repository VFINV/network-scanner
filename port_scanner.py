import socket

target = input("Enter target IP or hostname: ")

try:
    target_ip = socket.gethostbyname(target)
    print(f"\nScanning target {target_ip}...\n")
except socket.gaierror:
    print("Invalid hostname or IP")
    exit()

for port in range(20, 102):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        socket.setdefaulttimeout(1)
        result = sock.connect_ex((target_ip, port))
        if result == 0:
            print(f"Port {port} is open")

print("Scan complete")
