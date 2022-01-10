import json
import click
import logging
from flask.cli import FlaskGroup
from api.app import create_app

log = logging.getLevelName("bard")

@click.group(cls=FlaskGroup, create_app=create_app)
def cli():
    """Server-side command line for bard. """