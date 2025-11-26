import typer
import requests
import httpx

app = typer.Typer(help="Simple HTTP client implemented with Typer.")


# def parse_headers(raw_headers: List[str]) -> Dict[str, str]:
#     """Parse ``KEY:VALUE`` header strings into a dict.

#     Same behaviour as the argparse version, but kept as a plain function
#     so it can be unit-tested independently.
#     """
#     headers: Dict[str, str] = {}
#     for item in raw_headers:
#         if ":" not in item:
#             raise typer.BadParameter(
#                 f"Invalid header {item!r}, expected KEY:VALUE"
#             )
#         key, value = item.split(":", 1)
#         headers[key.strip()] = value.strip()
#     return headers


@app.command()
def request(
    url: str = typer.Argument(
        ...,
        help="URL to request (e.g. https://httpbin.org/get)",
    ),
    # method: str = typer.Option(
    #     "GET",
    #     "-X",
    #     "--method",
    #     help="HTTP method to use.",
    #     case_sensitive=False,
    # ),
    # header: List[str] = typer.Option(
    #     [],
    #     "-H",
    #     "--header",
    #     help="Custom header in KEY:VALUE format. Can be passed multiple times.",
    # ),
    quiet: bool = typer.Option(
        False,
        "-q",
        "--quiet",
        help="Only print the response body, no metadata.",
    ),
) -> None:
    """Perform a simple HTTP request.

    This command is intentionally very similar to the argparse version so
    you can compare the developer experience between the two approaches.
    """
    # headers = parse_headers(header)

    # try:
    #     response = requests.request(method.upper(), url, headers=headers)
    # except requests.RequestException as exc:
    #     typer.secho(f"Request failed: {exc}", err=True)
    #     raise typer.Exit(code=1)

    # if not quiet:
    #     typer.echo(f"Status: {response.status_code}")
    #     typer.echo(f"URL: {response.url}")
    #     typer.echo(f"Headers: {len(response.headers)} header(s)")
    #     typer.echo("-" * 40)

    # typer.echo(response.text)

    pass


def make_request(method: str, url: str, debug: bool = False):
    response = requests.get(url)

    if method == "httpx":
        response = httpx.get(url)
    print(f"Response Status Code: {response.status_code}")

    if debug:
        print("Debug mode is enabled.")
        print(f"Response Headers: {response.headers}")


if __name__ == "__main__":
    # app()
    typer.run(make_request)
