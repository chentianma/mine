# -*- coding: utf8 -*-


from flask import render_template, flash, request, current_app, redirect, jsonify
from flask_login import login_required
from . import main
from config import basedir
from werkzeug.utils import secure_filename
from blog import db
from ..models import User, Role, Article, Category
from flask_uploads import *
from datetime import datetime


pic_format_list = ['.png', '.PNG', '.jpg', '.jpeg', '.JPG', '.JPEG']
uploadedFile = {'img': os.path.join(basedir, 'uploadFile/image'),
                'file': os.path.join(basedir, 'uploadFile/file')}

@main.route('/upload', methods=['GET', 'POST'])
@login_required
def upload():
    is_upload_file_exited()
    if request.method == 'POST':
        if request.files['file']:
            file = request.files['file']
            extend_name = os.path.splitext(file.filename)[1]
            if extend_name in pic_format_list:
                # print('上传格式为%s' % extend_name)
                save_path = uploadedFile['img']
            else:
                # print('----上传格式为%s' % extend_name)
                save_path = uploadedFile['file']
            filename1 = secure_filename(file.filename)
            filename2 = '%s_%s' % (datetime.utcnow().strftime("%Y%m%dT%H%M%SZ"), filename1)
            new_filename = os.path.join(save_path, filename2)
            file.save(new_filename)
            msg = '文件上传成功！文件地址为 /file/uploadFile%s' % new_filename.split('/uploadFile')[1]
            return render_template('main/upload.html', msg=msg)
    else:
        return render_template('main/upload.html')


def is_upload_file_exited():
    for i in uploadedFile.values():
        if os.path.exists(i):
            continue
        else:
            os.makedirs(i)
    return