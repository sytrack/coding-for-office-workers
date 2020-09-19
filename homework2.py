name = "sunyoung"
year = "1993"
address = "Seoul"
view_count1 = 0

class Article:
    name = "sunyoung"
    view_count = 0

    def __init__(self, name, year, address):
        self.name = name
        self.year = year
        self.address = address

    def read(self):
        self.view_count = self.view_count + 1

article = Article("sunyoung", "1993", "Seoul")
print(article.name)
print(article.year)
print(article.address)
print(article.view_count)
article.read()
