import unittest
from phone_book import my_def, user1, user4, keys, phone_book

class TestPhoneBookPy(unittest.TestCase):
    def setUp(self):
        pass

    def test_add_remove_single_user(self):
        self.assertEqual(my_def(user1), user1)
        self.assertEqual(my_def(user1, 'del'), {})

    def test_add_remove_multiple_users(self):
        self.assertDictContainsSubset(my_def(user4), user4)
        self.assertDictContainsSubset(my_def(user4, 'del'), user4)


if __name__=='__main__':
    unittest.main()
