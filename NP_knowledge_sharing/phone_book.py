# my_def(name, par=del)
# {name: phone}
# return {all names and phones}

user1 = {'Vanya': '0961112233'}
keys = user1.keys()
#print keys[0]
user2 = {'Daria': '0964354884'}
user3 = {'Daria': 'no cellphone'}
user4 = {'Daria': 'no cellphone','Vanya': '0961112233'}

phone_book = {}

# par=None means that parameter is optional
def my_def(name, par=None):
    if par == 'del':
        key = name.keys()
        for i in key:
            del phone_book[i]
    else:
        phone_book.update(name)

    return phone_book


# my_def(user1, 'del')
# print phone_book
my_def(user4)
print phone_book

my_def(user4, 'del')
print phone_book

# test adding people to phone_book
# assert 'Vanya' in phone_book
# assert phone_book['Vanya'] == '0961112233'
# assert 'Daria' in phone_book
# assert phone_book['Daria'] == '0964354884'
# assert len(phone_book) == 2

# test deleting people from phone_book
# TODO: add/delete several users at once


# test_update_user(user)

# http://pythontesting.net/framework/unittest/unittest-introduction/
