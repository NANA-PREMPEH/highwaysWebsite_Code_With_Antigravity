from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate
from elasticsearch import Elasticsearch
from flask_mail import Mail
from trial.config import Config

from flask_s3 import FlaskS3
#for text editor
from flask_ckeditor import CKEditor

#FOR ROBOT DETECTION 
from flask_simple_captcha import CAPTCHA







#Create a database Instance 
mail = Mail()
db = SQLAlchemy()
bcrypt = Bcrypt()
migrate = Migrate() 
login_manager = LoginManager() 
login_manager.login_view = 'users.login' 
login_manager.login_message_category = 'info' 
s3 = FlaskS3()

#for text editor
ckeditor = CKEditor()

#FOR ROBOT DECTION
captcha = CAPTCHA(config=Config.CAPTCHA_CONFIG)

def create_app(config_class=Config):
    #Initialise flask
    app = Flask(__name__)
    app.config.from_object(Config)

    
    #Extensions Initialization
    mail.init_app(app) 
    db.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app, db) 
    login_manager.init_app(app)
    
    s3.init_app(app)

    #FOR ROBOT DETECTION
    app = captcha.init_app(app)
    ckeditor.init_app(app) #for text editor


    app.elasticsearch = Elasticsearch([app.config['ELASTICSEARCH_URL']]) \
        if app.config['ELASTICSEARCH_URL'] else None

    # Global Context Processor for Announcements and Dashboard counts
    from trial.models import Announcement, Leave
    @app.context_processor
    def inject_global_data():
        try:
            announcements = Announcement.query.filter_by(is_active=True).order_by(Announcement.date_posted.desc()).all()
            pending_no = Leave.query.filter_by(leave_status="Pending").count()
        except:
            announcements = []
            pending_no = 0
        return dict(announcements=announcements, pending_no=pending_no)

   
    #Import the blueprint objects and register with our routes
    from trial.users.routes import users
    from trial.blogs.routes import blogs
    from trial.generalforms.routes import generalforms 
    from trial.projects.routes import projects
    from trial.main.routes import main
    from trial.errors.handlers import errors
    from trial.admin.routes import admin
    from trial.leavemgt.routes import leavemgt
    from trial.ongoing_proj.routes import ongoing_proj 
    from trial.completed_proj.routes import completed_proj

    #Register the blueprint
    app.register_blueprint(users)
    app.register_blueprint(blogs)
    app.register_blueprint(generalforms)
    app.register_blueprint(projects)
    app.register_blueprint(main)
    app.register_blueprint(errors)
    app.register_blueprint(admin)
    app.register_blueprint(leavemgt)
    app.register_blueprint(ongoing_proj)
    app.register_blueprint(completed_proj)

    return app