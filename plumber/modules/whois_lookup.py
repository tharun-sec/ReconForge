import whois

def whois_lookup(domain):

    print("\nWHOIS INFORMATION")
    print("-" * 50)

    try:

        info = whois.whois(domain)

        print(f"Domain      : {info.domain_name}")
        print(f"Registrar   : {info.registrar}")
        print(f"Created     : {info.creation_date}")
        print(f"Expires     : {info.expiration_date}")

        return {
            "domain": str(info.domain_name),
            "registrar": str(info.registrar),
            "created": str(info.creation_date),
            "expires": str(info.expiration_date)
        }

    except Exception as e:

        print(f"WHOIS Error: {e}")

        return {}
