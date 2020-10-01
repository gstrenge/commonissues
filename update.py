from Markdown.Site import Site
from functools import reduce
import os

pages_path = ["docs", "pages", "*"]
main_path = ["docs"]


site = Site("Common Issues", ["docs", "pages", "*"])
index_file_name = "index.md"

print(site)

with open(os.path.join(reduce(os.path.join, main_path), index_file_name), 'w') as file:
    file.write(f"{site}")

os.system('git add .')
os.system('git commit -m "Site Rebuilt"')
os.system('git push')
