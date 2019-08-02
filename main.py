from flask import Flask, render_template, request, abort, redirect, url_for, session
import os,zipfile
from werkzeug.utils import secure_filename
from removebg import RemoveBg
import PIL.Image as Image
import shutil


APIKEY = ""
UPLOAD_FOLDER = '%s\\uploadFile' %os.getcwd()  # 上传路径
DOWNLOAD_FOLDER = '%s\\downloadFile' %os.getcwd()  # 下载路径
ZIP_FOLDER = '%s\\static\\zipFile' %os.getcwd()  # 压缩路径
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
            # flash('{} 上传成功'.format(filename))
            # return render_template('upload.html')  # 返回保存结果
            rmbg = RemoveBg(APIKEY, "error.log")
            for pic in os.listdir(UPLOAD_FOLDER):
                tempPic = pic.rsplit('.', 1)[0]
                url = "%s\%s" % (UPLOAD_FOLDER, pic)
                rmbg.remove_background_from_img_file(url)

                oldImg = url + "_no_bg.png"
                newImg = "%s\%s" % (DOWNLOAD_FOLDER, tempPic+".png")
                try:
                    shutil.move(oldImg, newImg)

                    im = Image.open(newImg)
                    x, y = im.size
                    p = Image.new('RGBA', im.size, (255,255,255))
                    p.paste(im, (0, 0, x, y), im)
                    p.save("%s\%s" % (DOWNLOAD_FOLDER, tempPic + '_white.png'))

                    im = Image.open(newImg)
                    x, y = im.size
                    p = Image.new('RGBA', im.size, (0,0,255))
                    p.paste(im, (0, 0, x, y), im)
                    p.save("%s\%s" % (DOWNLOAD_FOLDER, tempPic + '_blue.png'))

                    im = Image.open(newImg)
                    x, y = im.size
                    p = Image.new('RGBA', im.size, (255,0,0))
                    p.paste(im, (0, 0, x, y), im)
                    p.save("%s\%s" % (DOWNLOAD_FOLDER, tempPic + '_red.png'))

                    with zipfile.ZipFile("%s\%s" % (ZIP_FOLDER, tempPic + '.zip'), mode="w") as f:
                        for userfile in os.listdir(DOWNLOAD_FOLDER):
                            if userfile.rsplit('.', 1)[1] == 'png':
                                f.write("%s\%s" % (DOWNLOAD_FOLDER, userfile), userfile)
                                os.remove("%s\%s" % (DOWNLOAD_FOLDER, userfile))

                except FileNotFoundError:
                    return redirect(url_for('index'))
            os.remove("%s\%s" % (UPLOAD_FOLDER, pic))
            return redirect(url_for('static', filename="zipFile/{}".format(tempPic + ".zip")))
        else:
            return '非法的文件格式或操作！<a href="/upload">返回</a> '
    else:
        try:
            # name = session['username']
            return render_template('upload.html')
        except KeyError:
            abort(401)


@app.errorhandler(401)
def page_not_found(error):
    return render_template('page_not_found.html'),404