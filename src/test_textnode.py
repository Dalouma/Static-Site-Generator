import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_capitalization(self):
        node = TextNode("Capitalized or Not", TextType.TEXT)
        node2 = TextNode("capitalized or not", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_link_absence(self):
        node = TextNode("random text", TextType.TEXT)
        node2 = TextNode("random text", TextType.TEXT, "")
        self.assertNotEqual(node, node2)

    def test_text_type_diff(self):
        node = TextNode("random text", TextType.TEXT)
        node2 = TextNode("random text", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_NONE_url(self):
        node = TextNode("random text", TextType.TEXT)
        node2 = TextNode("random text", TextType.TEXT, None)
        self.assertEqual(node, node2)


if __name__ == "__main__":
    unittest.main()