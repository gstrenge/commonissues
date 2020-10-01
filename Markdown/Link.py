class Link(Markdown):

    def __init__(self, title, address):
        self.title = title
        self.address = address

    def generate_markdown(self):
        return f"[{self.title}]({self.address})"