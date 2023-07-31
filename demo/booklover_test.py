import unittest
import pandas as pd
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self): 
        # add a book and test if it is in `book_list`.
        booklover = BookLover('Taryn', 'hsh5rs@virginia.edu', 'Horror')
        
        booklover.add_book('Insomnia', 4)
        booklover.add_book('The Girl Who Loved Tom Gordon', 4)
        
        value = 'Insomnia' in booklover.book_list['book_name'].values
        expected = True
        
        self.assertEqual(value, expected)
        
    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        booklover = BookLover('Taryn', 'hsh5rs@virginia.edu', 'Horror')
        
        booklover.add_book('Insomnia', 4)
        booklover.add_book('Insomnia', 4)
        
        value = sum(1 for value in booklover.book_list['book_name'].values if value == 'Insomnia')
        expected = 1
        
        self.assertEqual(value, expected)
        
    def test_3_has_read(self): 
        booklover = BookLover('Taryn', 'hsh5rs@virginia.edu', 'Horror')
        
        booklover.add_book('Insomnia', 4)
        
        booklover.has_read('Insomnia')
        
        value = booklover.has_read('Insomnia')
        self.assertTrue(value)
        
    def test_4_has_read(self): 
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        booklover = BookLover('Taryn', 'hsh5rs@virginia.edu', 'Horror')
        booklover.has_read('Alice in Wonderland')
        
        value = booklover.has_read('Alice in Wonderland')
        
        self.assertFalse(value)
        
    def test_5_num_books_read(self):
        # add some books to the list, and test num_books matches expected.
        booklover = BookLover('Taryn', 'hsh5rs@virginia.edu', 'Horror')
        
        booklover.add_book('The Night Shift', 4)
        booklover.add_book('The Stand', 4)
        booklover.add_book('It', 5)
        booklover.add_book('The Girl Who Loved Tom Gordon', 4)
        
        value = booklover.num_book_read()
        expected = 4
        
        self.assertEqual(value, expected)

    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating  > 3
        booklover = BookLover('Taryn', 'hsh5rs@virginia.edu', 'Horror')
        
        booklover.add_book('Insomnia', 4)
        booklover.add_book('The Night Shift', 2)
        booklover.add_book('The Stand', 2)
        booklover.add_book('It', 5)
        booklover.add_book('The Girl Who Loved Tom Gordon', 4)
        
        value = sum(1 for value in booklover.book_list['book_rating'].values if value > 3)
        expected = 3
        
        self.assertEqual(value, expected)
        
if __name__ == '__main__':
    
    unittest.main(verbosity=3)
    
    
    