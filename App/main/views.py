from flask import Blueprint, render_template

from App.main import main


@main.route('/')
def hello_world():
    return 'Hello World!'