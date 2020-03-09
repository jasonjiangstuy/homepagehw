#format of the inputs
#title, description, list[[title, description, img location]]
def list(listitems):
    final = "<ul>"
    for i in listitems:
        final = final +"<li>" + str(i) + "</li>"
    final = final + "</ul>"
    return(final)

def stripquotes(list):
    finallist = []
    for i in list:
        if type(i) == type(""):
            finallist.append(i.strip("/'" + '/"'))
        elif type(i) == type([]):
            finallist.append(stripquotes(i))
    return(finallist)


#Need to cite:
citation = stripquotes([
    "Citations",
  "This are the citations for what used to build this website",
    [
      ["Webhosting service", "repl.it, I used this service to host my python code + static documents", "img."],
      ["HTML + CSS reference", "Devdocs, I used this service to learn about a few specific attributes + functions that I used to make my website pretty + build the js walkthrough"],
      ["jninja reference", "I used <a href='https://jinja.palletsprojects.com/en/2.11.x/'> this website </a> to review a few jinja features that I forgot the format for", "img."
      ],
      ["Stackoverflow", "I used stack overflow to trouble shoot and solve various problems<br> including: " + list(["how to preload and cashe images - index.html(12)", "How to make git save an empty directory - userimgs/.gitignore"])]

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
