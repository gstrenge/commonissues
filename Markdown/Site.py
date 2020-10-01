import glob
import os
from functools import reduce
from Markdown.Page import Page
from Markdown.Markdown import Markdown

class Site(Markdown):

    def __init__(self, page_title, pages_path):
        pages_path = reduce(os.path.join, pages_path)
        pages_urls = glob.glob(pages_path)

        self.title = page_title
        self.pages = []

        for page in pages_urls:
            page_name = os.path.basename(page)

            page_title_lowercase = page_name.split(".")[0]
            page_title = ""
            for word in page_title_lowercase.split(" "):
                page_title += word[0].upper() + word[1:] + " "
            page_title = page_title[:-1]
            page_url = os.path.join("pages", page_name)

            self.pages.append(Page(page_title, page_url))
    
    def generate_markdown(self):
        markdown_text = f"#{self.title}\n"
        self.pages.sort(key= lambda element : element.title)
        for page in self.pages:
            markdown_text += f"- {page}\n"
        return markdown_text
