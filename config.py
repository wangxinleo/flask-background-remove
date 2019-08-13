# 程序的配置
import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:  # 通用配置
    API_KEY = ""
    KEYEXIST = 0
    UPGOREMOVE_COUNT = 0
    UPLOAD_FOLDER = '%s/app/static/uploadFile' % os.getcwd()  # 上传路径
    DOWNLOAD_FOLDER = '%s/app/static/downloadFile' % os.getcwd()  # 下载路径
    ZIP_FOLDER = '%s/app/static/zipFile' % os.getcwd()  # 压缩路径
    ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'jfif', 'pjpeg', 'pjp'])  # 允许上传的文件类型
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'I7\xcd\xadu_\xf2\x87\xe4\xca%)\xa5O)C'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True  # 设置是否在每次连接结束后自动提交数据库中的变动
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://upGoremove:xxxxxx@49.232.48.54:3306/upGoremove'
    FLASKY_MAIL_SUBJECT_PREFIX = '[UpGoRemove]'  # 集成邮件功能，这个类似于主题概要的意思，但不是主题，只是在主题前面加个修饰前缀
    FLASKY_MAIL_SENDER = 'UpGoRemove Admin <UpGoRemove@example.com>'  # 这个是发件人，而<>前面的内容，实际上就相当于昵称的作用
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN') or 'wangxinleo'

    @staticmethod  # 使类不需要实例化就可以被调用
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
    #                           'sqllite:///' + os.path.join(basedir, 'data-dev.sqlite')


class ProductionConfig(Config):
    DEBUG = True
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    #                           'sqlite:///' + os.path.join(basedir, 'data.sqlite')


class TestingConfig(Config):
    TESTING = True
    # SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
    #                           'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
