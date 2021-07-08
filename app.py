from flask import Flask, render_template, url_for, request , redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from werkzeug.utils import redirect

app = Flask(__name__)
# DB Config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

#Database Model
class  ApplicationSaverModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    application_name = db.Column(db.String(955), nullable=False)
    application_link = db.Column(db.String(955), nullable=False)
    status = db.Column(db.String(955), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id

@app.route("/",methods=['POST','GET'])
def index():
    if request.method == 'POST':
        application_name = request.form['application_name']
        application_link = request.form['application_link']
        application_status = request.form['application_status']
        new_entry = ApplicationSaverModel(application_name=application_name,application_link=application_link,status=application_status)

        try:
            db.session.add(new_entry)
            db.session.commit()
            return redirect('/')
        except:
            return 'Error while Adding application'
    else:
        applications = ApplicationSaverModel.query.order_by(ApplicationSaverModel.date_created).all()
        return render_template('index.html' , applications=applications)

if __name__=='__main__':
    app.run(debug=True)
