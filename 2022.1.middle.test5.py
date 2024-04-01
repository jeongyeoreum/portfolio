class Book:
    def __init__(self, chapters,pages):
        self.chapters = chapters
        self.pages = pages

    def __str__(self):
        return f' Chapters :{self.chapters},Pages:{self.pages}'

class EBook(Book):
    def __init__(self, chapters, pages, format):
        super().__init__(chapters, pages)
        self.format = format
    def __str__(self):
        return super().__str__() + f'format: {self.format}'

if __name__ == '__main__':
    python = EBook(8,500,"pdf")
    print(python)
