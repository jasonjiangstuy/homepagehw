from flask import Flask, render_template, session
from flask_debug import Debug
app = Flask(__name__, static_folder='./static', template_folder='./templates')

#setting cache to null
app.config['CACHE_TYPE'] = 'null'

app.config.update(TEMPLATES_AUTO_RELOAD=True)

@app.route('/', methods=['GET'])
def home():
  return render_template(
    'index.html'
  )

@app.route('/ourteam', methods=['GET'])
def team():
  return render_template(
    'teampage.html'
  )

@app.route('/wheremyenergy', methods=['GET'])
def energy():
  return render_template(
    'wheresmyenergy.html'
  )

@app.route('/contactus', methods=['GET'])
def contact():
  return render_template(
    'contactus.html'
  )

#adding header to disable caching -- REMOVE WHEN DEPLOYING SITE
@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

if __name__ == '__main__':
    #app.run(host='0.0.0.0', port='3000', debug=True) #do NOT use in production
    app.run(host='0.0.0.0', port='3000')

#useful modules
#picking -> method of database storage: can preserve classes
#www.MYURL/showcase.com#isFake?=True