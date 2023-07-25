import socket

def get_local_ip():
    hostname=socket.gethostname()
    ip=socket.gethostbyname(hostname)
    print("Current Server IP: "+ip)


def test_port(hostname, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        sock.settimeout(2)
        
        result = sock.connect_ex((hostname, port))
        
        if result == 0:
            print(f"Test Remote IP {hostname} Port {port} Success")
        else:
            print(f"Test Remote IP {hostname} Port {port} Failed")
        
        sock.close()
    
    except socket.error as e:
        print(f"Connection Error：{str(e)}")



get_local_ip()
for ip in ["172.25.200.71","172.25.200.72","172.25.200.143"]:
    for Port in [32230, 32231, 32227, 32228]:
       test_port(ip, Port)



