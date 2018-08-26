import unittest

from helloworld import print_text


class HelloWorldTests(unittest.TestCase):
    def test_hello_world(self):
        class_to_print = print_text()
        self.assertEqual(class_to_print.text_to_print, "Hello World")

    def test_not_empty(self):
        class_to_print = print_text()
        self.assertNotEqual(class_to_print.text_to_print, "")


if __name__ == "__main__":
    unittest.main()
