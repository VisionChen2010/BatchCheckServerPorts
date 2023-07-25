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
for ip in ["172.1.1.21","172.1.1.22","172.1.1.23"]:
    for Port in [220, 221, 222, 223，224，225]:
       test_port(ip, Port)



