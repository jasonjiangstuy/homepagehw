from flask import Flask, render_template, session, request
import details
app = Flask(__name__, static_folder='./static', template_folder='./templates')
#print(details.citation)
#setting cache to null
app.config['CACHE_TYPE'] = 'null'

app.config.update(TEMPLATES_AUTO_RELOAD=True)

@app.route('/', methods=['GET'])
def home():
  if request.args.get('walkthrough') == 'True':
    print('starting walkthrough')
    return render_template(
    'index.html', walkthrough=True
    )
  return render_template(
    'index.html'
  )

@app.route('/myteam', methods=['GET'])
def team():
  return render_template(
    'teampage.html'
  )

@app.route('/contactme', methods=['GET'])
def contact():
  return render_template(
    'standard.html', i=details.contactme
  )

@app.route('/citations', methods=['GET'])
def cite():
  return render_template(
    #global citation
    "standard.html", i=details.citation
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
