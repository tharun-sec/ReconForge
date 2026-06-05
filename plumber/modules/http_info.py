import requests


def get_http_headers(target):

    try:

        url = f"http://{target}"

        response = requests.get(
            url,
            timeout=5,
            allow_redirects=True
        )

        return dict(response.headers)

    except Exception as e:

        print(f"HTTP Error: {e}")
        return {}
