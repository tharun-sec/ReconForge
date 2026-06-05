import nmap

def scan_target(target):

    scanner = nmap.PortScanner()

    print("\n[+] Starting Scan...\n")

    scanner.scan(target, arguments="-sV -p1-1023 -vv  -sC  -O")

    return scanner
