import unittest
from helper_functions import *

class TestTextToTextNode(unittest.TestCase):
    def test_basic_all(self):
        text = "This is **text** with an _italic_ word and a `code block` and an " \
        "![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        nodes = text_to_textnodes(text)
        # print(nodes)
        self.assertEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
            nodes
        )

    def test_only_text(self):
        text = "This sentence only has normal text"
        nodes = text_to_textnodes(text)
        self.assertEqual(
            [
                TextNode("This sentence only has normal text", TextType.TEXT)
            ],
            nodes
        )

    def test_only_bold(self):
        text = "**Bold words**"
        nodes = text_to_textnodes(text)
        self.assertEqual(
            [
                TextNode("", TextType.TEXT),
                TextNode("Bold words", TextType.BOLD),
                TextNode("", TextType.TEXT),
            ],
            nodes
        )

    def test_only_italic(self):
        text = "_Slant words_"
        nodes = text_to_textnodes(text)
        self.assertEqual(
            [
                TextNode("", TextType.TEXT),
                TextNode("Slant words", TextType.ITALIC),
                TextNode("", TextType.TEXT),
            ],
            nodes
        )

    def test_only_code(self):
        text = "`Big code block`"
        nodes = text_to_textnodes(text)
        self.assertEqual(
            [
                TextNode("", TextType.TEXT),
                TextNode("Big code block", TextType.CODE),
                TextNode("", TextType.TEXT),
            ],
            nodes
        )

    def test_only_image(self):
        text = "![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg)"
        nodes = text_to_textnodes(text)
        self.assertEqual(
            [
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            ],
            nodes
        )

    def test_only_link(self):
        text = "[link](https://boot.dev)"
        nodes = text_to_textnodes(text)
        self.assertEqual(
            [
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
            nodes
        )

    def test_empty_string(self):
        nodes = text_to_textnodes("")
        self.assertEqual(
            [
                TextNode("", TextType.TEXT)
            ],
            nodes
        )

    def test_code_and_image(self):
        text = "`code block` and ![image](https://rand-image.fake.com)"
        nodes = text_to_textnodes(text)
        self.assertEqual(
            [
                TextNode("", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://rand-image.fake.com")
            ],
            nodes
        )