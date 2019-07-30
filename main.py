from flask import Flask, render_template, request, abort, redirect, url_for, escape, session, flash
import os
from werkzeug.utils import secure_filename


UPLOAD_FOLDER = '%s' %os.getcwd()  # 上传路径
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])  # 允许上传的文件类型


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = '1111111111'  # os.urandom(16)


def allowed_file(filename):  # 验证上传文件是否符合要求
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':

        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = '密钥无效！'
        else:
            session['username'] = request.form['username']
            return redirect(url_for('upload_file'))
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))


@app.route('/upload', methods=['POST', 'GET'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']  # 获取上传的文件
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)  # 获取上传的文件名
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))  # 保存文件
            flash('{} 上传成功'.format(filename))
            return render_template('upload.html')  # 返回保存结果
        else:
            return '非法的文件格式或操作！<a href="/upload">返回</a> '
    else:
        try:
            name = session['username']
            return render_template('upload.html', name=name)
        except KeyError:
            abort(401)


@app.errorhandler(401)
def page_not_found(error):
    return render_template('page_not_found.html'),404