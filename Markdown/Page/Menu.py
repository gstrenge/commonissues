import glob
import os
from functools import reduce
from Markdown.Page.Page import Page
from Markdown.Markdown import Markdown
from Markdown.Config import Config


class Menu(Page):

    def __init__(self, title, path):
        super().__init__(title, path + [Config.MENU_FILE_NAME])

        path_string = reduce(os.path.join, path)
        pages_urls = glob.glob(os.path.join(path_string, "*"))

        self.pages = []
        self.menus = []

        for page in pages_urls:
            page_name = os.path.basename(page)

            page_title_lowercase = page_name.split(".")[0]
            title = ""
            for word in page_title_lowercase.split(" "):
                title += word[0].upper() + word[1:] + " "
            title = title[:-1]
            page_url = os.path.join(path_string, page_name)

            if os.path.isdir(page_name):
                self.menus.append(Menu(title, path + [page_name]))
            else:
                self.pages.append(Page(title, page_url))

    
    def generate_markdown(self):
        markdown_text = f"# {self.title}\n"

        self.menus.sort(key=lambda element : element.title)
        self.pages.sort(key= lambda element : element.title)

        for menu in self.menus:
            markdown_text += f"- {menu}\n"

        markdown_text += "---"

        for page in self.pages:
            markdown_text += f"- {page}\n"

        return markdown_text
