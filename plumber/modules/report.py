from datetime import datetime


def generate_report(scan_data):

    filename = f"reports/{scan_data['target']}.txt"

    with open(filename, "w") as report:

        report.write("RECONFORGE REPORT\n")
        report.write("=" * 50 + "\n\n")

        report.write(
            f"Generated: {datetime.now()}\n\n"
        )

        report.write(f"Target: {scan_data['target']}\n")
        report.write(f"OS: {scan_data['os']}\n\n")

        # WHOIS
        report.write("WHOIS INFORMATION\n")
        report.write("-" * 50 + "\n")

        for key, value in scan_data.get("whois", {}).items():
            report.write(f"{key}: {value}\n")

        # SUBDOMAINS
        report.write("\nSUBDOMAINS\n")
        report.write("-" * 50 + "\n")

        for subdomain in scan_data.get("subdomains", []):
            report.write(f"{subdomain}\n")

        # DNS
        report.write("\nDNS INFORMATION\n")
        report.write("-" * 50 + "\n")

        for record_type, values in scan_data.get("dns", {}).items():

            report.write(f"\n{record_type} Records:\n")

            for value in values:
                report.write(f"  {value}\n")

        # HTTP HEADERS
        report.write("\nHTTP HEADERS\n")
        report.write("-" * 50 + "\n")

        for key, value in scan_data.get("headers", {}).items():
            report.write(f"{key}: {value}\n")

        # OPEN PORTS
        report.write("\nOPEN PORTS\n")
        report.write("-" * 50 + "\n")

        for port in scan_data.get("ports", []):

            report.write(
                f"{port['port']}/{port['protocol']} "
                f"{port['service']} "
                f"{port['product']} "
                f"{port['version']}\n"
            )

    print(f"\n[+] Report Saved: {filename}")
