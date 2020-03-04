#format of the inputs
#title, description, list[[title, description, img location]]
def list(listitems):
    final = "<ul>"
    for i in listitems:
        final.append("<li>" + str(i) + "</li>")
    final.append("</ul>")
    return(final)
    
citation = [
    "Citations",
  "This are the citations for what used to build this website",
    [
      ["Webhosting service", "repl.it, I used this service to host my python code + static documents", "img."],
      ["HTML + CSS reference", "Devdocs, I used this service to learn about a few specific attributes + functions that I used to make my website pretty"],
      ["jninja reference", "I used <a href='https://jinja.palletsprojects.com/en/2.11.x/'> this website </a> to review a few jinja features that I forgot the format for", "img."
      ],
      ["Stackoverflow", "I used stack overflow to trouble shoot and solve various problems<br> including: " + list("how to preload and cashe images - index.html(12)")]

    ]
]

projects = [
  "My Projects",
  "These are the projects that I'm working or have worked on",
  [
    [],[]
  ]
]

contactme = [
  [

  ]

]
