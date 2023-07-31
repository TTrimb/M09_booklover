import pandas as pd

class BookLover:
    def __init__ (self, name, email, fav_genre, num_book = 0, book_list = pd.DataFrame({'book_name':[], 'book_rating':[]})
):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_book = num_book
        self.book_list = book_list
    
    def add_book(self, book_name, book_rating):
        if book_name not in self.book_list['book_name'].values:
            new_book = pd.DataFrame({'book_name':[book_name],'book_rating':[book_rating]})
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
            print('Book is added to the list')
        else: 
            print('Book is already on the list')

    def has_read(self, book_name):
        if book_name in self.book_list['book_name'].values:
            return True
        else:
            return False
        
    def num_book_read(self):
        num = len(self.book_list)
        return num
    
    def fav_books(self):
        rating = self.book_list.query('book_rating > 3')
        return rating
             
    
        
        