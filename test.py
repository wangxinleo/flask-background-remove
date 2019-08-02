import os,zipfile



UPLOAD_FOLDER = '%s\\uploadFile' %os.getcwd()  # 上传路径
DOWNLOAD_FOLDER = '%s\\downloadFile' %os.getcwd()  # 下载路径
ZIP_FOLDER = '%s\\zipFile' %os.getcwd()  # 压缩路径
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])  # 允许上传的文件类型


def main():
    with zipfile.ZipFile("%s\%s" % (ZIP_FOLDER, 'test1.zip'), mode="w") as f:
        for userfile in os.listdir(DOWNLOAD_FOLDER):
            if userfile.rsplit('.', 1)[1] == 'png':
                f.write("%s\%s" % (DOWNLOAD_FOLDER, userfile), userfile)
                # os.remove("%s\%s" % (DOWNLOAD_FOLDER, userfile))


if __name__ == '__main__':
    main()