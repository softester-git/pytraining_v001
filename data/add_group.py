# -*- coding: utf-8 -*-
from model.group import Group
import random
import string


constant = [
    Group(group_name="name1", group_header="header1", group_footer="footer1"),
    Group(group_name="name2", group_header="header2", group_footer="footer2")
]


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


test_data = [
    Group(group_name=group_name if group_name!="" else None, group_header=group_header if group_header!="" else None, group_footer=group_footer if group_footer!="" else None)
    for group_name in ["", random_string("name", 10)]
    for group_header in ["", random_string("header", 20)]
    for group_footer in ["", random_string("footer", 20)]
]
