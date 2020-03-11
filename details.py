#format of the inputs
#title, description, list[[title, description, img location]]
def mylist(listitems):
    final = "<ul>"
    for i in listitems:
        final = final +"<li>" + str(i) + "</li>"
    final = final + "</ul>"
    return(final)

def stripquotes(mylist):
    finallist = []
    for i in mylist:
        if type(i) == type(""):
            finallist.append(i.strip("/'" + '/"'))
        elif type(i) == type([]):
            finallist.append(stripquotes(i))
    return(finallist)

fencing = ["Stuyvesant Fencing", "Fencing is one of passions in my life. Joining in as a freshamn it was the one thing in life that I had complete control over. How much that I improved was directly proportional on how much work i put in. I was hooked, after a ton of work I made it , head of Foil for the boys fencing team, manager of the girls fencing team, woooo stuy fencing on 3 <br/><br/>However I didnt get to where i am without help.<br/> This is my thank you to everyone who has push me to become the person that I am now.<br/>", [[],[] ] ]


myTeam = ["My Team", "This is my hacktahon team that I code with, over time members have come and go but we will always remember the memories of last minute smashing keyboards and chugging coffee to stay up all night in LI (Shapin, Christ, Amanda yall know what im talking about >wO ) but, here im giving a shout out to the OG's, yall have been with me since day one in twain. <br/><center><b> Math Talent Represent :P </b></center> ", [["Esteak Shapin", "You already know whats good, you my bro and there is no one else that I would rather have coding by my side", "./static/imgs/shapinchris.jpg"],
["Christopher Dou","ayyy this one is for the CSS king. You a baller all the way. I still in awe of that one time you jumped the battery park fence sheesh. But fr I appreciate u, ur always fun to be around and we always come up with great projects together!! ...and u the only one that understands me when that free food come by", "./static/imgs/chris.jpg"],

]]
#Need to cite:
citation = stripquotes([
    "Citations",
  "This are the citations for what used to build this website",
    [
      ["Webhosting service", "repl.it, I used this service to host my python code + static documents", "./static/imgs/repl.png"],
      ["HTML + CSS reference", "Devdocs, I used this service to learn about a few specific attributes + functions that I used to make my website pretty + build the js walkthrough", "./static/imgs/DevDocs.jpeg"],
      ["jninja reference", "I used <a href='https://jinja.palletsprojects.com/en/2.11.x/'> this website </a> as my main jinja refrence", "./static/imgs/jinja.png"
      ],
      ["Stackoverflow", str("I used stack overflow to trouble shoot and solve various problems<br> including: " + mylist(["how to preload and cashe images - index.html(12)", "How to make git save an empty directory - userimgs/.gitignore", "The theory how you would be able to coding in js"]) ) ],

      ["What did I learn", "Here i'm going to talk about some of the achievements that i am proud to have done in this project. I learn how to: " + mylist(["use js to cycle through images and edit css attributes", "build a review mechinism that can take in imgs and text and ratings via a post method", "use python file minipulation + storages modules like os, shutil, werkzeug, and of course pickle!!!", "Just how diffrent js is to other languages like python and java with its single thread async design builtin and how that was a pain in the ...","Ofc this came alongside practicing using breakpoints (woo those saved me countless times)", "use flask in new ways examples: " + mylist(["cap file upload size", "get GET request args(see what i did there)", "create a route to handle user request for the static pics themselfs", "use jninja templating to get the file path inside the html"]), "Overall an absolute blast to make, little sleep deprived but it all worked out in the end. "
      ])
      ]
    ]
])

projects = [
  "My Projects",
  "These are the projects that I'm working or have worked on",
  [
    [],[]
  ]
]


contactme = [
    "Contact Me",
    "Leave a message about the site or contact my email <br> just make sure its clean",
  [
    ["Email:", "be a good sport and not spam me :) <br/> <a href='mailto:jjiang20@stuy.edu?subject=About%20Me%20Website'> jjiang20@stuy.edu</a>"],

  ]

]
