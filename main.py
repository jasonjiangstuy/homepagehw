from flask import Flask, render_template, session, request
import details
from werkzeug.utils import secure_filename
import os
import pickle #thx mr brooks for the suggestion
UPLOAD_FOLDER = './static/userimgs'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__, static_folder='./static', template_folder='./templates')
#print(details.citation)
#setting cache to null
app.config['CACHE_TYPE'] = 'null'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
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

##check if the file type is one of the allowed, if none type it returns false
def allowed_extension(extension): 
    return extension.lower() in ALLOWED_EXTENSIONS 

def myImgpaths():
  print('getting img paths')

#on startup
  #save the old ratings in case a revert is needed
import shutil
shutil.copy("rating.p", "ratingcp.p")

reviews = []
pickle.dump(reviews, open("rating.p", "wb"))

##

def addReview(name, rating, comment):    
  if comment:
     myComment = comment
  else:
    myComment = "No comment, Jason Jiang's website was too perfect ^w^"
  reviews = pickle.load( open("rating.p", "rb") ) 
  reviews.append((name, rating, myComment))
  pickle.dump()
#thx to https://wiki.python.org/moin/UsingPickle

def next_filename(): #returns in the next slot 1-10 // if all filled then it renames all files to filename+1 and returns 1
  numboffiles = 0
  for entry in os.scandir(app.config['UPLOAD_FOLDER']):
      if entry.is_file() :
         print(entry.name)
         numboffiles += 1
  moveover = (numboffiles >= 10)
  if moveover:
    print("shift-over") #start shift-over code
    myFiles = []
    for i in range(numboffiles): #order the directory// extremely bad sort im sorry mr brooks, ill improve it in a future update
      #print(str(i + 1))
      for entry in os.scandir(app.config['UPLOAD_FOLDER']):
        if entry.name.rsplit(".", 1)[0] == str(i + 1): 
          # start at file 10
          #print(entry.name.rsplit(".", 1)[0])
          extension = entry.name.rsplit(".", 1)[1] #problem
          #print(extension)
          if allowed_extension(extension):
            myFiles.append(entry)
            #print(myFiles)

    #remove 10
    print('path for 10: ', (os.path.join(app.config['UPLOAD_FOLDER'], myFiles[len(myFiles) - 1].name)))
    os.remove(os.path.join(app.config['UPLOAD_FOLDER'], myFiles[len(myFiles) - 1].name)) #get rid of 10
    myFiles.pop(len(myFiles) - 1)
    print("myfiles with deleted 10")
    print(myFiles)
       
    #overwrites from 10-1 , 10 del, 9 renamed to 10... etc
    myFiles.reverse()
    print(myFiles)
    
    countdown = 10
    
    for i in myFiles: ###
      start = os.path.join(app.config['UPLOAD_FOLDER'], i.name)##get exentsion
      end = os.path.join(app.config['UPLOAD_FOLDER'],str(countdown) + "." + i.name.rsplit(".", 1)[1])         
      countdown = countdown - 1
      print("moving")
      print("start: " + str(start))
      print("end: " + str(end))
      os.rename(start , end) #move 9-> 10

    return("1")
  else:
    print("numboffiles:" + str(numboffiles))
    return(str(numboffiles)) #return the next number
    

#print(next_filename())

@app.route('/contactme', methods=['GET', 'POST'])
def contact():
  if request.method == 'POST':
    print('postrequestmade')
    name = request.form.get('name')
    rating = request.form.get('rating')
    if not name and rating:
      return render_template(
      'standard.html', i=details.contactme, contactme=True, submit=False
    )
    comment = request.form.get('comment')
    img = request.form.get('img')
    print(name, rating, comment, img)
    addReview(name, rating, comment)
    print(request.files['img'])
    if 'img' in request.files: #ask if a img was sent #@
      print('second level made')
      myFile = request.files['img'] #@ 
      fileextension = myFile.filename.rsplit('.', 1)[1]
      if myFile.filename != '' and allowed_extension(fileextension):
        fileextension = "." + fileextension
        filename = next_filename() + fileextension
        filename = secure_filename(filename)
        print(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        myFile.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        print('file saved')
    # img = request.form.get('img')
    # img.save(static/userimgs)
    #thank you to: https://flask.palletsprojects.com/en/1.1.x/patterns/fileuploads/ for showing me the os modules specialized function used to save the a file 
    
    #getting the reviews
    #review line

    #getting the img paths
    #the two elements combine in the jninja
    return render_template(
      'standard.html', i=details.contactme, contactme=True, submit=True
    )
  return render_template(
    'standard.html', i=details.contactme, contactme=True
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
