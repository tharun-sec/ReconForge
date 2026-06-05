import dns.resolver

def dns_lookup(domain):

    print("\nDNS INFORMATION")
    print("-" * 50)

    dns_data = {}

    records = ["A", "MX", "NS", "TXT"]

    for record in records:

        try:
            answers = dns.resolver.resolve(domain, record)

            values = [str(answer) for answer in answers]

            dns_data[record] = values

            print(f"\n{record} Records:")

            for value in values:
                print(value)

        except:
            dns_data[record] = []

            print(f"\n{record} Records: None")

    return dns_data
