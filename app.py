# import os
# import json
# import requests
# from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
# from flask_json import FlaskJSON, JsonError, json_response, as_json
# from flask import jsonify
#
#
# app = Flask(__name__)
# from app import views
# app.config.from_object(os.environ['APP_SETTINGS'])
# FlaskJSON(app)


# @app.route('/')
# def hello():
#     return "Hello World!"
#
# @app.route('/member/<member_id>')
# def dms(member_id):
#     url = "http://192.168.200.130:8080/api/v1/lookupByRfid"
#     payload = "rfid=" + member_id
#     headers = {
#         'content-type': "application/x-www-form-urlencoded",
#         }
#     response = requests.request("POST", url, data=payload, headers=headers)
#     return response.json()
#
#
#
# @app.route('/<name>')
# def hello_name(name):
#     return "Hello {}!".format(name)

# if __name__ == '__main__':
#     app.run()
