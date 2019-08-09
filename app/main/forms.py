import os
from flask import current_app
from . import main


@main.route('/complete/<fileId>')
def complete_json(fileId):
    # os.remove("%s\%s" % (current_app.config.get('UPLOAD_FOLDER'), filename))
    DataNum = 0
    rejson = '{"status":200,"Message":"获取数据成功","Data":['
    for pic in os.listdir(current_app.config.get('DOWNLOAD_FOLDER')):
        if str(fileId) == pic[0:6]:
            DataNum += 1
            temp = ("%s\%s" % (current_app.config.get('DOWNLOAD_FOLDER'), pic)).split('\\')
            imgPath = '/'+temp[-3]+'/'+temp[-2]+'/'+temp[-1]
            rejson += '{"filename":"' + pic[6:] + '","filepath":"' + imgPath + '"},'
    for tempZip in os.listdir(current_app.config.get('ZIP_FOLDER')):
        if str(fileId) == tempZip[0:6]:
            DataNum += 1
            temp = ("%s\%s" % (current_app.config.get('ZIP_FOLDER'), tempZip)).split('\\')
            zipPath = '/'+temp[-3]+'/'+temp[-2]+'/'+temp[-1]
            rejson += '{"filename":"' + tempZip[6:] + '","filepath":"' + zipPath + '"}'
    rejson += ']}'
    if DataNum != 0:
        return rejson
    else:
        return '{"status":400,"Message":"获取数据失败"}'