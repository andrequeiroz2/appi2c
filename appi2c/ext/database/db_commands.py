import click
from appi2c.ext.database import db
from appi2c.ext.auth.auth_models import User # noqa


def init_app(app):

    @app.cli.command()
    def create_db():
        """Starting Data Base"""
        db.create_all()
        click.echo(click.style("Success", fg="green")+": Started Data Base")
