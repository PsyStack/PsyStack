from __future__ import annotations

import threading


def check_for_update() -> None:
    """Print a notice if a newer version of psystack is available on PyPI."""

    def _check() -> None:
        try:
            import json
            import urllib.request

            from psystack import __version__

            resp = urllib.request.urlopen(
                "https://pypi.org/pypi/psystack/json", timeout=3
            )
            data = json.loads(resp.read())
            latest = data["info"]["version"]

            if latest != __version__:
                import typer

                typer.echo(
                    f"\n  PsyStack {latest} available (you have {__version__}). "
                    f"Run: pip install --upgrade psystack\n"
                )
        except Exception:
            pass  # network down, PyPI unreachable, not published yet — all fine

    threading.Thread(target=_check, daemon=True).start()
