from flask import Flask, render_template, request, url_for, redirect
import difflib
import pandas as pd
from reccode import whiskey_rec

app = Flask(__name__, template_folder='templates')


# Set up the main route
@app.route('/', methods =['GET','POST'])    
def index():


    return render_template('index.html')

@app.route('/recommendations', methods=['GET','POST'])
def recommendations():
    w1 = request.form['whis1']
    w2 = request.form['whis2']
    w3 = request.form['whis3']
    w4 = request.form['whis4']
    w5 = request.form['whis5']
    user_type = request.form['whiskeys']
    user_budget = request.form['budget']
    result = whiskey_rec(w1,w2,w3,w4,w5,user_type,user_budget)
    #'{} {} {} {} {} {} {}'.format(w1,w2,w3,w4,w5,user_type,user_budget)
   
    return '''
            <!DOCTYPE html>
            <html>
            
            <center>
            <body  style = "background-image: url('https://images.footballfanatics.com/FFImage/thumb.aspx?i=/productimages/_3744000/altimages/ff_3744083-faf05331922e825509e1alt1_full.jpg&w=900">
                <h1>Here Is Your Flight!</h1>
                {0}</body></center>
            </html>
            '''.format(result)

   


 

if __name__ == '__main__':
    app.run(threaded=True,debug=False)
