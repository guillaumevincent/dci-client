import click


def execute(context):
    print(context)


@click.command()
@click.option('--dci-login', envvar='DCI_LOGIN',
              help="DCI login or 'DCI_LOGIN' environment variable.")
@click.option('--dci-password', envvar='DCI_PASSWORD',
              help="DCI password or 'DCI_PASSWORD' environment variable.")
def cli(*args, **kwargs):
    context = {
        'dci_login': kwargs['dci_login'],
        'dci_password': kwargs['dci_password']
    }
    execute(context)
