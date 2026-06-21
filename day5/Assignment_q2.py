class book:
    def __init__ (self, title, author):
        self.title= title
        self.author = author
        self.reviews= []
    def add_review(self, review):
        self.reviews.append(review)
    def count_reviews(self):
        return len(self.reviews)

    def display_reviews(self):
        if not self.reviews:
            print("No reviews yet.")
        else:
            print(f"Reviews for '{self.title}' by {self.author}:")
            for i in self.reviews:
                print(i)
book1 = book("The Girl in The Glasscase", "Devashish Sardana")
book1.add_review("good book")
book1.add_review("nice book")
book1.display_reviews()
print(book1.count_reviews())
