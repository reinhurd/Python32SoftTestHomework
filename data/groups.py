# -*- coding: utf-8 -*-
from model.group import Group
import random
import string


constant = [
    Group(name='111', header='222', footer="333"),
    Group(name='1111', header='2222', footer="3333")
]


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits  # + string.punctuation + " "*10 #Отключение небезопасных символов
    return prefix + ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [
    Group(name=random_string("name", 10), header=random_string("header", 20), footer=random_string("footer", 20))
    for i in range(3)
]