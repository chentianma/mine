# -*- coding: utf8 -*-


from flask import render_template, flash, request, current_app, redirect, jsonify
from flask_login import login_required
from . import main
from config import basedir
from werkzeug.utils import secure_filename
from blog import db
from ..models import User, Role, Article, Category
from flask_uploads import *


@main.route('/upload', methods=['GET', 'POST'])
@login_required
def upload():
    if request.method == 'POST':
        if request.files['file']:
            uploadedFile = os.path.join(basedir, 'uploadFile')
            file = request.files['file']
            filename = secure_filename(file.filename)
            new_filename = os.path.join(uploadedFile, filename)
            file.save(new_filename)
            msg = '文件上传成功！文件地址为/uploadFile/ %s' % filename
            # flash('文件上传成功！文件地址为/uploadFile/ %s' % filename)
            # return jsonify({'status': 200,
            #                 'url': '/uploadFile/ %s' % filename})
            return render_template('main/upload.html', msg=msg)
    else:
        return render_template('main/upload.html')
