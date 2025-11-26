import argparse
import requests
import httpx


# def parse_headers(raw_headers: List[str]) -> Dict[str, str]:
#     """Parse ``KEY:VALUE`` header strings into a dict.

#     This is kept deliberately simple for demo purposes.
#     """
#     headers: Dict[str, str] = {}
#     for item in raw_headers:
#         if ":" not in item:
#             raise ValueError(f"Invalid header {item!r}, expected KEY:VALUE")
#         key, value = item.split(":", 1)
#         headers[key.strip()] = value.strip()
#     return headers


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
        "method", type=str, help="Which method to use", choices=["requests", "httpx"]
    )
    parser.add_argument("--debug", action="store_true", help="Enable debug mode.")

    # parser.add_argument(
    #     "-X",
    #     "--method",
    #     default="GET",
    #     choices=["GET", "HEAD"],
    #     help="HTTP method to use (default: GET).",
    # )
    # parser.add_argument(
    #     "-H",
    #     "--header",
    #     action="append",
    #     default=[],
    #     help="Custom header in KEY:VALUE format. Can be passed multiple times.",
    # )
    parser.add_argument(
        "-q",
        "--quiet",
        action="store_true",
        help="Only print the response body, no metadata.",
    )

    args = parser.parse_args(argv)
    print(args)

    response = requests.get(args.url)
    if args.method == "httpx":
        response = httpx.get(args.url)

    print(f"Response Status Code: {response.status_code}")
    if args.debug:
        print("Debug mode is enabled.")
        print(f"Response Headers: {response.headers}")

    # try:
    #     headers = parse_headers(args.header)
    # except ValueError as exc:
    #     parser.error(str(exc))
    #     raise SystemExit(2)

    # try:
    #     response = requests.request(args.method, args.url, headers=headers)
    # except requests.RequestException as exc:
    #     print(f"Request failed: {exc}", file=sys.stderr)
    #     raise SystemExit(1)

    # if not args.quiet:
    #     print(f"Status: {response.status_code}")
    #     print(f"URL: {response.url}")
    #     print(f"Headers: {len(response.headers)} header(s)")
    #     print("-" * 40)

    # # For simplicity we always decode as text and ignore binary responses.
    # print(response.text)


if __name__ == "__main__":
    main()
