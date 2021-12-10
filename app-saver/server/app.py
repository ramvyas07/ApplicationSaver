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
            # return redirect('/')
            return {"status":"200 OK"}
        except:
            return 'Error while Adding application'
    else:
        applications = ApplicationSaverModel.query.order_by(ApplicationSaverModel.date_created).all()
        return render_template('index.html' , applications=applications)

@app.route('/delete/<int:id>')
def delete(id):
    delete_app = ApplicationSaverModel.query.get_or_404(id)
    try:
        db.session.delete(delete_app)
        db.session.commit()
        return redirect('/')
    except:
        return "There was an error in deletion of that application. Contact admin at @ramvyas_"

@app.route('/update/<int:id>' , methods=['POST','GET'])
def update(id):
    app = ApplicationSaverModel.query.get_or_404(id)
    if request.method == 'POST':
        app.application_name = request.form['application_name']
        app.application_link = request.form['application_link']
        app.application_status = request.form['application_status']

        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'Error'
    else:
        return render_template('update.html', app = app)

@app.route('/api', methods=['POST','GET'])
def api():
    try:
        result_json = cj.search({
                            'location'    : 'torronto',
                            'keywords'    : request.form['jobs'],
                            'affid'       : '213e213hd12344552',
                            'user_ip'     : '108.35.75.46',
                            'url'         : 'http://127.0.0.1:5000/api?q='+request.form['jobs']+'&l=torronto',
                            'user_agent'  : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
                        });
    except:
        return render_template('api.html')

if __name__=='__main__':
    app.run(debug=True)
