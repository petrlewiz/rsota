from jinja2 import Environment, FileSystemLoader
import os

env = Environment(loader=FileSystemLoader("templates"))

template = env.get_template("professor.html")

professor = {
    "name" : "Dr. Smith",
    "title" : "Professor of Old Testament",
    "bio" : "Went to RSOTA and got a masters degree in theology"
}

html = template.render(
    name=professor["name"],
    title=professor["title"],
    bio=professor["bio"]
)

os.makedirs("professors", exist_ok=True)

with open("professors/dr-smith.html", "w", encoding="utf-8") as file: 
    file.write(html)