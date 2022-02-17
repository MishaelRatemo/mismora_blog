from urllib import response
from flask import render_template, request,jsonify
from . import root

@root.route(404)
def four_Ow_four():
    title = '404 page'
    error_description =' The page you are looking we seem not to have found it'
    return render_template('404.html', title=title, error_description=error_description), 404

@root.app_errorhandler(500)
def internal_server_err(err):
    if request.accept_mimetypes.accept_json and not request.accept_mimetype.accept_html:
        response = jsonify({ 'error': 'internal server error'})
        response.status_code = 500
        return response
    return render_template('500.html'), 500