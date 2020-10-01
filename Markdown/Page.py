from Markdown.Markdown import Markdown

class Page(Markdown):

    def __init__(self, title, url):
        self.title = title
        self.url = url

    def generate_markdown(self):
        return f"[{self.title}]({self.url})"

    