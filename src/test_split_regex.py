import unittest
from helper_functions import *

class TestSplitRegex(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_images_immediate(self):
        node = TextNode(
            "![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png) and some padding",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
                TextNode(" and some padding", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT
        )
        new_nodes = split_nodes_link([node])
        self.assertEqual(
            [
                TextNode("This is text with a link ", TextType.TEXT),
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and ", TextType.TEXT),
                TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),
            ],
            new_nodes
        )

    def test_split_links_immediate(self):
        node = TextNode(
            "[to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT
        )
        new_nodes = split_nodes_link([node])
        self.assertEqual(
            [
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and ", TextType.TEXT),
                TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),
            ],
            new_nodes
        )

    def test_split_images_and_links(self):
        node = TextNode(
            "[to boot dev](https://www.boot.dev) and ![image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT
        )

        split_image_first = split_nodes_image([node])
        self.assertEqual(
            [
                TextNode("[to boot dev](https://www.boot.dev) and ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png")
            ],
            split_image_first
        )
        split_links_second = split_nodes_link(split_image_first)
        self.assertEqual(
            [
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png")
            ],
            split_links_second
        )

        split_links_first = split_nodes_link([node])
        self.assertEqual(
            [
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and ![image](https://i.imgur.com/3elNhQu.png)", TextType.TEXT)
            ],
            split_links_first
        )
        split_image_second = split_nodes_image(split_links_first)
        self.assertEqual(
            [
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png")
            ],
            split_image_second
        )