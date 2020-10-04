from Markdown.Markdown import Markdown
from Markdown.Link import Link


class Page(Markdown):

    def __init__(self, title, path, content="", header=""):
        self.title = title
        self.path = path
        self.link = Link(title, path)

        self.content = content
        self.header = header

    def generate_markdown(self):

        markdown = f"{self.header}\n\n"
        markdown += self.content

        return markdown

