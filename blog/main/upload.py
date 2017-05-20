# -*- coding: utf8 -*-


from flask import render_template, flash, request, current_app, redirect
from flask_login import login_required
from . import main
from config import basedir
from blog import db
from ..models import User, Role, Article, Category
from flask_uploads import *


@main.route('/upload', methods=['GET', 'POST'])
@login_required
def upload():
    uploadedFiledir = os.path.join(basedir, 'uploadFile')
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = file.filename
            new_filename = os.path.join(uploadedFiledir, filename)
            file.save(new_filename)
            flash('文件上传成功！文件地址为/uploadFile/ %s' % filename)
            return '/uploadFile/ %s' % filename
    else:
        return '''
            <!doctype html>
            <title>Upload new File</title>
            <h1>Upload new File</h1>
            <form action="" method=post enctype=multipart/form-data>
              <p><input type=file name=file>
                 <input type=submit value=Upload>
            </form>
            '''
