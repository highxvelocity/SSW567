"""Overly complicated hello world script to allow for some testing"""


class HelloClass(object):
    __slots__ = "text_to_print"

    def __init__(self, text):
        if text != "":
            self.text_to_print = text

    def __str__(self):
        return self.text_to_print


def print_text():
    class_to_print = HelloClass("Hello World")
    print(class_to_print)
    return class_to_print
