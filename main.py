#the diffrent indent length are because i used too diffrent text editors for this project
from flask import Flask, render_template, session, request, send_from_directory

import details
from werkzeug.utils import secure_filename
import shutil
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
app.config['MAX_CONTENT_LENGTH'] = 20 * 1024 #max upload of 20 MB, soft stop, > 16

@app.route('/', methods=['GET'])
def home():
  if request.args.get('walkthrough') == 'True':
    print('starting walkthrough')
    sequence = request.args.get('sequence')
    print(sequence)
    return render_template(
    'index.html', walkthrough=1, sequence=int(sequence)
    )
  return render_template(
    'index.html', walkthrough=0
  )

@app.route('/myteam', methods=['GET'])
def team():
  return render_template(
    'teampage.html'
  )

##check if the file type is one of the allowed, if none type it returns false
def allowed_extension(extension):
    return extension.lower() in ALLOWED_EXTENSIONS

def myImgpaths(): #done
  print('getting img paths')
  filepaths = []
  finalpaths = []
  countup = 1
  for entry in os.scandir(app.config['UPLOAD_FOLDER']):
    if entry.is_file() and not entry.name.startswith(".") :
      filepaths.append(entry.name)
  for i in range(len(filepaths)): #check that its in order
    for u in filepaths:
        #print(str(u.split(".", 1)[0]) + "equals" + str(i + 1))
        if str(u.split(".", 1)[0]) == str(i + 1):
          print(os.path.join(app.config['UPLOAD_FOLDER'], u))
          finalpaths.append(os.path.join(app.config['UPLOAD_FOLDER'], u))
  return(finalpaths) #list of img names, 1- 10 in order


#on startup
  #save the old ratings in case a revert is needed
def onStartup():
  shutil.copy("rating.p", "ratingcp.p")
  reviews = []
  pickle.dump(reviews, open("rating.p", "wb"))
  shutil.copy("averagescore.p", "averagescorecp.p")
  overallrating = [0, 0]
  pickle.dump(overallrating, open("averagescore.p", "wb"))
  #remove all img files
  for entry in os.scandir(app.config['UPLOAD_FOLDER']):
      if entry.is_file() and not entry.name.startswith("."):
        os.remove(os.path.join(app.config['UPLOAD_FOLDER'], entry.name))

onStartup()
##

def addReview(name, rating, comment):
  if comment:
     myComment = comment
  else:
    myComment = "No comment, Jason Jiang's website was too perfect ^w^"

  averagescore = pickle.load( open("averagescore.p", "rb"))
  newaveragescore = [float(averagescore[0]) + float(rating), float(averagescore[1]) + float(1)]
  pickle.dump( newaveragescore, open("averagescore.p", "wb")) #save new( total scores + number of reviews)

  reviews = pickle.load( open("rating.p", "rb") )
  reviews.insert( 0, [name, rating, myComment] )
  pickle.dump( reviews, open("rating.p", "wb") ) #saves new( all reviews)
#thx to https://wiki.python.org/moin/UsingPickle

def getReviews(): #returns most recent 10 reviews(list) , average score
    reviews = pickle.load( open("rating.p", "rb") )
    reviews = reviews[0:10]
    return(reviews)

def next_filename(): #returns in the next slot 1-10 // if all filled then it renames all files to filename+1 and returns 1
  numboffiles = 0
  for entry in os.scandir(app.config['UPLOAD_FOLDER']):
      if entry.is_file() and not entry.name.startswith(".") :
         print(entry.name)
         numboffiles += 1
         print(numboffiles)
  moveover = (numboffiles >= 10)

  print("shift-over") #start shift-over code
  myFiles = []
  for i in range(numboffiles): #order the directory// extremely bad sort im sorry mr brooks, ill improve it in a future update
  #print(str(i + 1))
    for entry in os.scandir(app.config['UPLOAD_FOLDER']):
      if not entry.name.startswith(".") and entry.name.rsplit(".", 1)[0] == str(i + 1):
          # start at file 10
          #print(entry.name.rsplit(".", 1)[0])
        extension = entry.name.rsplit(".", 1)[1] #problem
          #print(extension)
        if allowed_extension(extension):
          myFiles.append(entry)
            #print(myFiles)

    #remove 10
  if moveover:
      print('path for 10: ', (os.path.join(app.config['UPLOAD_FOLDER'], myFiles[len(myFiles) - 1].name)))
      os.remove(os.path.join(app.config['UPLOAD_FOLDER'], myFiles[len(myFiles) - 1].name)) #get rid of 10
      myFiles.pop(len(myFiles) - 1)
      print("myfiles with deleted 10")
      print(myFiles)

    #overwrites from 10-1 , 10 del, 9 renamed to 10... etc
  myFiles.reverse()
  print(myFiles)

  countdown = len(myFiles) + 1 #9 -> 10

  for i in myFiles: ###
    start = os.path.join(app.config['UPLOAD_FOLDER'], i.name)##get exentsion
    end = os.path.join(app.config['UPLOAD_FOLDER'],str(countdown) + "." + i.name.rsplit(".", 1)[1])
    countdown = countdown - 1
    print("moving")
    print("start: " + str(start))
    print("end: " + str(end))
    os.rename(start , end) #move 9-> 10

  return("1")
  # else:
  #   print("numboffiles:" + str(numboffiles)) #1 is most recent, 10 least recent
  #   for i in range
  #   return(str(numboffiles + 1)) #return the next number


#print(next_filename())

def buildReviewLayout(): #in progress
  paths = myImgpaths()
  reviews = getReviews()
  print("number of reviews: " + str(len(reviews)))
  print("number of imgs: " + str(len(paths)))
  if len(reviews) != len(paths):
    raise(ValueError, "number of imgs and reviews dont coordinate")
  for i in range(len(reviews)): #append the img path to the reviews
    reviews[i].append(paths[i])

  default = details.contactme

  #getting average score
  averagescore = pickle.load( open("averagescore.p", "rb") )
  try:
    finalaveragescore = (averagescore[0] / averagescore[1])
  except: #if there are no reviews/ division by zero
    finalaveragescore = "N/A"
  return(default, finalaveragescore, reviews)

@app.route('/uploads/<filename>')
def serve(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/contactme', methods=['GET', 'POST'])
def contact():
  if request.method == 'POST':
    print('postrequestmade')
    name = request.form.get('name')
    rating = request.form.get('rating')
    if not name and rating: #ask if anything was returned for those needed values
      default, average, reviews = buildReviewLayout()
      return render_template(
        'contactme.html', i=default, averagescore=average, u=reviews, contactme=True, submit=False
      )
    comment = request.form.get('comment')
    print(name, rating, comment)
    addReview(name, rating, comment)
    print(request.files['img'])
    if 'img' in request.files and request.files['img'].filename != '': #ask if a img was sent // img is not none type
      print('second level made')
      myFile = request.files['img'] #get image
      #check if img is less than 360kb , 360,000
      #thx to https://codippa.com/how-to-check-file-size-in-python-3-ways-to-find-out-size-of-file-in-python/
      fileextension = myFile.filename.rsplit('.', 1)[1]
      if myFile.filename != '' and allowed_extension(fileextension):
        fileextension = "." + fileextension
        filename = next_filename() + fileextension
        filename = secure_filename(filename)
        print(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        myFile.save(os.path.join(app.config['UPLOAD_FOLDER'], filename)) #file, coruptted
        print('file saved')
      else:
          default, average, reviews = buildReviewLayout()
          return render_template(
            'contactme.html', i=default, averagescore=average, u=reviews, contactme=True, submit=False
          )
    else: #no image was sent, save a cp of the default img in its place
      filename = next_filename() + ".jpeg"
      filename = secure_filename(filename)
      print(os.path.join(app.config['UPLOAD_FOLDER'], filename))
      shutil.copy("default.jpeg", os.path.join(app.config['UPLOAD_FOLDER'], filename))
      print('default file saved')

    # img = request.form.get('img')
    # img.save(static/userimgs)
    #thank you to: https://flask.palletsprojects.com/en/1.1.x/patterns/fileuploads/ for showing me the os modules specialized function used to save the a file

    #getting the reviews
    #review line
    #getting the img paths
    #the two elements combine in the jninja
    default, average, reviews = buildReviewLayout()
    return render_template(
      'contactme.html', i=default, averagescore=average, u=reviews, contactme=True, submit=True
    )

  default, average, reviews = buildReviewLayout()
  return render_template(
    'contactme.html', i=default, averagescore=average, u=reviews, contactme=True
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
