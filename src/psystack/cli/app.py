from __future__ import annotations

import typer

app = typer.Typer(name="psystack", help="Regression psystack harness for ML pipelines.")


@app.callback(invoke_without_command=True)
def main(ctx: typer.Context) -> None:
    """Launch TUI when no subcommand is given."""
    from psystack.cli.version_check import check_for_update

    check_for_update()

    if ctx.invoked_subcommand is None:
        from psystack.tui.app import PsyStackApp

        try:
            PsyStackApp().run()
        except (KeyboardInterrupt, SystemExit):
            pass
