import click

@click.command()
@click.option('--string',default = 'World', help = 'Enter name to say hello')
def cli(string):
	click.echo('Hello %s' %string)
