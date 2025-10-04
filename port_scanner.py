import socket

def scan_ports(target, ports=[21,22,23,25,53,80,110,143,443,3389]):
    print(f"\nScanning {target}...\n")
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            result = sock.connect_ex((target, port))
            if result == 0:
                print(f"Port {port} is OPEN ✅")
            else:
                print(f"Port {port} is closed ❌")
            sock.close()
        except Exception as e:
            print(f"Error scanning port {port}: {e}")

if __name__ == "__main__":
    target_ip = input("Enter target IP address: ")
    scan_ports(target_ip)