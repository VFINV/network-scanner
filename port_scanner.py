import socket

target = input("Enter target IP: ")
print(f"\n Scanning target {target}...\n")

for port in range(20, 102): 
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)

    result = sock.connect_ex((target, port))
    if result == 0:
        print(f"Port {port} is open")
    sock.close()

print("Scan complete")
#test