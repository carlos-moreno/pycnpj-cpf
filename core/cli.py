import pkg_resources
import rich_click as click
from rich.console import Console
from rich.table import Table

from .core import valida_cpf_cnpj

click.rich_click.USE_RICH_MARKUP = True
click.rich_click.USE_MARKDOWN = True
click.rich_click.SHOW_ARGUMENTS = True
click.rich_click.GROUP_ARGUMENTS_OPTIONS = True
click.rich_click.SHOW_METAVARS_COLUMN = True
click.rich_click.APPEND_METAVARS_HELP = True


@click.group()
@click.version_option(pkg_resources.get_distribution("pycpf-cnpj").version)
def main():
    """CPF and CNPJ validator.
    This cli application validates if the CPF/CNPJ entered is valid.
    """


@main.command()
@click.option("--value", help="Value to be validated.")
def validate(value: str) -> bool:
    table = Table(title="Value")
    headers = ["CPF/CNPJ", "Is Valid?"]
    for header in headers:
        table.add_column(header, style="magenta")

    result = valida_cpf_cnpj(value)
    table.add_row(f"{value}", str(result))
    console = Console()
    console.print(table)
