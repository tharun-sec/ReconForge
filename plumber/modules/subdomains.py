import subprocess

def get_subdomains(domain):

    try:

        result = subprocess.run(
            ["subfinder", "-d", domain, "-silent"],
            capture_output=True,
            text=True
        )

        cleaned = []

        for sub in result.stdout.splitlines():

            sub = sub.strip()

            if (
                domain in sub
                and "u003e" not in sub
            ):
                cleaned.append(sub)

        return sorted(
            list(
                set(cleaned)
            )
        )

    except Exception as e:

        print(f"Subfinder Error: {e}")
        return []
