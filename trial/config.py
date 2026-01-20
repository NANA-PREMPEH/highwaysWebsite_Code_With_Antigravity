import os


#Set the configurations
class Config:
    
    SECRET_KEY = os.environ.get('SECRET_KEY')
    # SQLALCHEMY_DATABASE_URI = os.environ.get('JAWSDB_URL') # for deployment on cpanel
    # SQLALCHEMY_DATABASE_URI = "mysql+pymysql://highwaysgov_desktopuser:@desktopuser@197.253.67.106/highways_ghadb" # for deployment on cpanel (old Db)
    # SQLALCHEMY_DATABASE_URI = "mysql+pymysql://highwaysgov_desktopuser:@desktopuser@197.253.67.106/highwaysgov_db_v1" # for deployment on cpanel (new Db)
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:root@localhost/for_antigravity" # for local development
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') 
    ADMIN_HIGHWAYS = os.environ.get('ADMIN_HIGHWAYS')
    
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    ACL = 'public-read'
    FLASKS3_BUCKET_NAME = os.environ.get('FLASKS3_BUCKET_NAME')
    FLASKS3_REGION = 'us-east-1'

    
    ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL') 
    POSTS_PER_PAGE = 3

    #Code for robot detection
    CAPTCHA_CONFIG = {'SECRET_CAPTCHA_KEY': 'wMmeltW4mhwidorQRli6Oijuhygtfgybunxx9VPXldz'}

