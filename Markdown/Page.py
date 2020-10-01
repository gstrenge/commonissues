from Markdown.Markdown import Markdown

class Page(Markdown):

    def __init__(self, title, url):
        self.title = title
        self.url = url

    def generate_markdown(self):
        url_without_md = self.url.split(".")[0]
        return f"[{self.title}]({url_without_md})"

    