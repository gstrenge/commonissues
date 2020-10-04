from Markdown.Page.Menu import Menu
from Markdown.Config import Config
from functools import reduce
import os


site = Menu("Common Issues", Config.SITE_TOP_DIRECTORY + Config.PAGES_TOP_DIRECTORY)
index_file_name = "index.md"

print(site)

with open(os.path.join(reduce(os.path.join, main_path), index_file_name), 'w') as file:
    file.write(f"{site}")

os.system('git add .')
os.system('git commit -m "Site Rebuilt"')
os.system('git push')
