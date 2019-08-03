from flask import Flask, render_template, request, abort, redirect, url_for, session
import os,zipfile,random
from werkzeug.utils import secure_filename
from removebg import RemoveBg
import PIL.Image as Image
import shutil


APIKEY = "5dJL3SSoTauGqBqZP38npuef"
UPLOAD_FOLDER = '%s\\uploadFile' %os.getcwd()  # 上传路径
DOWNLOAD_FOLDER = '%s\\static\\downloadFile' %os.getcwd()  # 下载路径
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
        fileId = random.randint(100000, 999999);
        file = request.files['file']  # 获取上传的文件
        if file and allowed_file(file.filename):
            filename = str(fileId)+secure_filename(file.filename)  # 获取上传的文件名
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))  # 保存文件

            return '{"Code":0,"Message":"保存数据成功","Data":[{"fileId":"'+str(fileId)+'","filename":"'+filename+'"}]}'
        else:
            return '系统检测到非法的文件格式或操作！<a href="/">返回</a> '
    else:
        try:
            name = session['username']
            return render_template('index.html')
        except KeyError:
            abort(401)


@app.route('/drawing/<fileId>/<filename>')
def drawing(fileId,filename):
    rmbg = RemoveBg(APIKEY, "error.log")
    for pic in os.listdir(UPLOAD_FOLDER):
        if pic == filename:
            tempPic = pic.rsplit('.', 1)[0]
            url = "%s\%s" % (UPLOAD_FOLDER, filename)
            rmbg.remove_background_from_img_file(url)

            oldImg = url + "_no_bg.png"
            newImg = "%s\%s" % (DOWNLOAD_FOLDER, tempPic + ".png")
            try:
                shutil.move(oldImg, newImg)
                im = Image.open(newImg)
                x, y = im.size
                p = Image.new('RGBA', im.size, (255, 255, 255))
                p.paste(im, (0, 0, x, y), im)
                p.save("%s\%s" % (DOWNLOAD_FOLDER, tempPic + '_white.png'))

                im = Image.open(newImg)
                x, y = im.size
                p = Image.new('RGBA', im.size, (0, 0, 255))
                p.paste(im, (0, 0, x, y), im)
                p.save("%s\%s" % (DOWNLOAD_FOLDER, tempPic + '_blue.png'))

                im = Image.open(newImg)
                x, y = im.size
                p = Image.new('RGBA', im.size, (255, 0, 0))
                p.paste(im, (0, 0, x, y), im)
                p.save("%s\%s" % (DOWNLOAD_FOLDER, tempPic + '_red.png'))

                with zipfile.ZipFile("%s\%s" % (ZIP_FOLDER, tempPic + '.zip'), mode="w") as f:
                    for userfile in os.listdir(DOWNLOAD_FOLDER):
                        if userfile.rsplit('.', 1)[1] == 'png':
                            f.write("%s\%s" % (DOWNLOAD_FOLDER, userfile), userfile)

                #             os.remove("%s\%s" % (DOWNLOAD_FOLDER, userfile))

                # return redirect(url_for('static', filename="zipFile/{}".format(tempPic + ".zip")))

                return redirect(url_for('complete_file', filename=filename, fileId=fileId))
            except FileNotFoundError:
                return '你的图片好像没有前景哦~AI没办法识别出来你图片突出的主体呢~用其他的照片试试吧~'
        else:
            continue
        return '系统检测到非法的文件格式或操作！<a href="/">返回</a>'


@app.route('/complete/<fileId>')
def complete_json(fileId):
    # os.remove("%s\%s" % (UPLOAD_FOLDER, filename))
    rejson = '{"status":200,"Message":"获取数据成功","Data":['
    i = 0
    DataNum = 0
    length = os.listdir(DOWNLOAD_FOLDER).__len__()
    for pic in os.listdir(DOWNLOAD_FOLDER):
        i += 1
        if str(fileId) == pic[0:6]:
            DataNum += 1
            temp = ("%s\%s" % (DOWNLOAD_FOLDER, pic)).split('\\')
            imgPath = '/'+temp[-3]+'/'+temp[-2]+'/'+temp[-1]
            if length == i:
                rejson += '{"filename":"'+pic[6:]+'","filepath":"'+imgPath+'"}'
            else:
                rejson += '{"filename":"' + pic[6:] + '","filepath":"' + imgPath + '"},'
    rejson += ']}'
    if DataNum != 0:
        return rejson
    else:
        return '{"status":400,"Message":"获取数据失败"}'


@app.route('/complete/<fileId>/<filename>')
def complete_file(fileId,filename):
    return render_template('complete.html',fileId=fileId,filename=filename)


@app.errorhandler(401)
def page_not_found(error):
    return render_template('page_not_found.html'),404