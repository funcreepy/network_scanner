import nmap

def is_printer(port_list):
    printer_ports = [515, 631, 9100]
    for port in port_list:
        if port in printer_ports:
            return True
    return False

def is_ups(port_list):
    ups_ports = [80, 443, 161, 162]
    for port in port_list:
        if port in ups_ports:
            return True
    return False

def is_web_server(port_list):
    web_ports = [80, 443, 8080, 8443]
    for port in port_list:
        if port in web_ports:
            return True
    return False

def is_database_server(port_list):
    database_ports = [1433, 3306, 5432, 1521]
    for port in port_list:
        if port in database_ports:
            return True
    return False

def is_sub_database_server(port_list):
    sub_database_ports = [1433, 3306, 5432, 1521, 27017, 27018, 27019]
    for port in port_list:
        if port in sub_database_ports:
            return True
    return False

def is_docker(port_list):
    docker_ports = [2375, 2376, 2377, 5000, 5001]
    for port in port_list:
        if port in docker_ports:
            return True
    return False

def is_api(port_list):
    api_ports = [80, 443, 8080, 8443, 5000, 5001, 8000, 8081]
    for port in port_list:
        if port in api_ports:
            return True
    return False

def main():
    nm = nmap.PortScanner()
    target = input("Enter target IP address or range: ")
    nm.scan(hosts=target, arguments='-p- -sV --version-all --hostname')
    for host in nm.all_hosts():
        hostname = nm[host].hostname()
        ports = list(nm[host]['tcp'].keys())
        if is_printer(ports):
            print(f"[!] {hostname} ({host}) is probably a printer")
        elif is_ups(ports):
            print(f"[!] {hostname} ({host}) is probably an UPS")
        elif is_web_server(ports):
            print(f"[+] {hostname} ({host}) is a potential web server")
        elif is_database_server(ports):
            print(f"[+] {hostname} ({host}) is a potential database server")
        elif is_sub_database_server(ports):
            print(f"[+] {hostname} ({host}) is a potential sub-database server")
        elif is_docker(ports):
            print(f"[+] {hostname} ({host}) is a potential Docker container")
        elif is_api(ports):
            print(f"[+] {hostname} ({host}) is a potential API")
        else:
            print(f"[+] {hostname} ({host}) is a potential service")

if __name__ == '__main__':
    main()
