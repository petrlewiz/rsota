from jinja2 import Environment, FileSystemLoader
import pandas as pd
import os

df = pd.read_csv("professor_data.csv")

env = Environment(loader=FileSystemLoader("templates"))
template = env.get_template("professor.html")


for _, row in df.iterrows():
     slug = row["Slug"]

     html = template.render(
          name = row["Name"],
          bio = row["Bio"]
     )
     os.makedirs("professors", exist_ok=True)

     with open(f'professors/{slug}.html', "w", encoding="utf-8") as file: 
          file.write(html)