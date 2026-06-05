# ReconForge

ReconForge is a Python-based reconnaissance and vulnerability assessment tool designed to automate information gathering during security assessments and penetration testing.

## Features

* DNS Enumeration
* WHOIS Lookup
* Subdomain Discovery (Subfinder Integration)
* Port Scanning (Nmap Integration)
* Service Version Detection
* Operating System Detection
* HTTP Header Collection
* TXT Report Generation
* JSON Report Generation

## Technologies Used

* Python 3
* Nmap
* Subfinder
* Requests
* Python-Nmap
* Python-Whois
* DNSPython

## Project Structure

```text
ReconForge/
├── main.py
├── modules/
│   ├── scanner.py
│   ├── dns_lookup.py
│   ├── whois_lookup.py
│   ├── subdomains.py
│   ├── http_info.py
│   └── report.py
├── reports/
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/tharun-sec/ReconForge.git
cd ReconForge
```

Install Python dependencies:

```bash
pip install python-nmap requests python-whois dnspython
```

Install required tools:

```bash
sudo apt update
sudo apt install nmap subfinder
```

## Usage

Run ReconForge:

```bash
sudo python3 main.py
```

Enter a target domain or IP address when prompted.

Example:

```text
Enter Target IP or Domain: nmap.org
```

## Example Capabilities

* Discover subdomains
* Collect DNS records
* Gather WHOIS information
* Identify open ports
* Detect running services and versions
* Detect operating systems
* Collect HTTP response headers
* Generate structured reports

## Output

ReconForge generates:

* TXT Reports
* JSON Reports

Reports are stored inside the `reports/` directory.

## Disclaimer

This tool is intended for educational purposes and authorized security assessments only. Always obtain proper permission before scanning systems you do not own or manage.
