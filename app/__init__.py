import os
from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
# from flask.ext.session import Session
# from flask_debugtoolbar import DebugToolbarExtension
from flask import jsonify
from flask_mail import Mail

# from flask_assets import Environment, Bundle


app = Flask(__name__)
# app.config.from_object('config')
app.config.from_object(os.environ['APP_SETTINGS'])
# print(app.config)
mail = Mail(app)
# toolbar = DebugToolbarExtension(app)

from app import views




# http://flask-assets.readthedocs.io/en/latest/
# assets = Environment(app)
# assets.url = app.static_url_path

# #Add the files that you want included - the pyscss is the sass compiler
# scss = Bundle('scss/app.scss', filters='pyscss', output='all.css')
# #This is the file that is included in the template
# assets.register('scss_all', scss)
#
# scss = Bundle('dog.scss', filters='pyscss', output='all.css')
# assets.register('scss_all', scss)
