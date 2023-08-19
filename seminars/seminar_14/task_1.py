import re


def string_cleaner(s):
    return re.sub(r'[^a-z ]*', '', s.lower())


if __name__ == '__main__':
    print(string_cleaner('Py#$%^thon i_+=s a g/*-+ooD lan%gu12357age'))
