# -*- coding: utf8 -*-


from flask import Flask
from blog import create_app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)