import argparse
import requests
import httpx


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(
        prog="http-argparse",
        description="Simple HTTP client implemented with argparse.",
    )
    parser.add_argument(
        "url",
        help="URL to request (e.g. https://httpbin.org/get)",
    )
    parser.add_argument(
        "lib", type=str, help="Which lib to use", choices=["requests", "httpx"]
    )
    parser.add_argument(
        "-q",
        "--quiet",
        action="store_true",
        help="Only print the response body, no metadata.",
    )

    args = parser.parse_args(argv)
    print(args)

    if args.lib == "httpx":
        response = httpx.get(args.url)
    elif args.lib == "requests":
        try:
            response = requests.get(args.url)
        except requests.RequestException as e:
            print(f"Request failed: {e}")
            response.raise_for_status()
    else:
        print("You need to provide something valid for the lib option: httpx or requests")
        response = None

    if response is not None:
        print(f"Response Status Code: {response.status_code}")


if __name__ == "__main__":
    main()
