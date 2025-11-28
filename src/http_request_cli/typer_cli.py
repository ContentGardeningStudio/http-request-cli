import typer
import requests
import httpx
from enum import Enum

app = typer.Typer(help="Simple HTTP client implemented with Typer.")


class HttpLib(str, Enum):
    requests = "requests"
    httpx = "httpx"


@app.command()
def request(
    url: str = typer.Argument(
        ...,
        help="URL to request (e.g. https://httpbin.org/get)",
    ),
    lib: str = typer.Argument(
            ...,
            help="Lib to use (requests or httpx)",
        ),
    debug: bool = typer.Option(
        False,
        "-d",
        "--debug",
        help="Only print the response body, no metadata.",
    ),
) -> None:
    """Perform a simple HTTP request.

    This command is intentionally very similar to the argparse version so
    you can compare the developer experience between the two approaches.
    """
    typer.secho(f"\n→ Sending request to {url}", fg="cyan")
    typer.secho(f"→ Using library: {lib}", fg="cyan")

    if lib == HttpLib.httpx:
        response = httpx.get(url)
    elif lib == HttpLib.requests:
        try:
            response = requests.get(url)
        except requests.RequestException as e:
            typer.secho(f"Request failed: {e}", err=True, fg="red")
            raise typer.Exit(code=1)
    else:
        raise typer.BadParameter("You need to provide something valid for the lib option: httpx or requests")
        response = None

    if response is not None:
        typer.echo(f"Response Status Code: {response.status_code}")


if __name__ == "__main__":
    app()
