from modules.scanner import scan_target
from modules.dns_lookup import dns_lookup
from modules.whois_lookup import whois_lookup
from modules.report import generate_report
from modules.subdomains import get_subdomains
import json
from modules.http_info import get_http_headers


def banner():
    print("=" * 50)
    print("      ReconForge")
    print(" Recon & Vulnerability Scanner")
    print("=" * 50)


banner()

target = input("Enter Target IP or Domain: ")

# Collect Recon Data
dns_data = dns_lookup(target)
whois_data = whois_lookup(target)
subdomains = get_subdomains(target)
headers = get_http_headers(target)
print("\nHTTP HEADERS DEBUG")
print(headers)
# Main Data Storage
scan_data = {
    "target": target,
    "dns": {},
    "whois": {},
    "subdomains": [],
    "headers": {},
    "ports": [],
    "os": ""
}

# Store DNS Data
if dns_data:
    scan_data["dns"] = dns_data

# Store WHOIS Data
if whois_data:
    scan_data["whois"] = whois_data

# Store Subdomains
scan_data["subdomains"] = subdomains
scan_data["headers"] = headers
# Run Nmap Scan
results = scan_target(target)

# Store Nmap Results
for host in results.all_hosts():

    # OS Detection
    if 'osmatch' in results[host]:

        osmatches = results[host]['osmatch']

        if osmatches:
            scan_data["os"] = osmatches[0]['name']

    # Port Information
    for proto in results[host].all_protocols():

        ports = results[host][proto].keys()

        for port in sorted(ports):

            service = results[host][proto][port]

            port_info = {
                "port": port,
                "protocol": proto,
                "service": service.get("name", ""),
                "product": service.get("product", ""),
                "version": service.get("version", "")
            }

            scan_data["ports"].append(port_info)

# Display Results
for host in results.all_hosts():

    print(f"\nHost: {host}")

    if 'osmatch' in results[host]:

        osmatches = results[host]['osmatch']

        if osmatches:
            print(f"Detected OS: {osmatches[0]['name']}")

    for proto in results[host].all_protocols():

        ports = results[host][proto].keys()

        print("\nPORT\tSERVICE\tVERSION")
        print("-" * 50)

        for port in sorted(ports):

            service = results[host][proto][port]

            service_name = service.get("name", "unknown")
            product = service.get("product", "")
            version = service.get("version", "")

            print(
                f"{port}\t"
                f"{service_name}\t"
                f"{product} {version}"
            )

# Show Subdomains
print("\nSUBDOMAINS")
print("=" * 50)

for subdomain in scan_data["subdomains"][:20]:
    print(subdomain)

# Generate Reports
generate_report(scan_data)

with open(f"reports/{target}.json", "w") as json_file:
    json.dump(scan_data, json_file, indent=4)

print(f"\n[+] JSON Report Saved: reports/{target}.json")
