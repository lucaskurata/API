from flask import Blueprint, jsonify, request


usuarios_app = Blueprint('usuarios_app',__name__,template_folder='templates')


@usuarios_app.route('/usr', methods=['POST'])
def cadastrar():
    