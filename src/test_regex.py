import unittest
from converters import *


class TestRegex(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
        
    def test_link_extract(self):
        matches = extract_markdown_links(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        )
        self.assertListEqual([("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")], matches)

    def test_both_extract(self):
        matches_img = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and a link [to boot dev](https://www.boot.dev) at the end."
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches_img)
        matches_link = extract_markdown_links(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and a link [to boot dev](https://www.boot.dev) at the end."
        )
        self.assertEqual([("to boot dev", "https://www.boot.dev")], matches_link)

    def test_link_immediate(self):
        matches = extract_markdown_links(
            "[to boot dev](https://www.boot.dev)"
        )
        self.assertEqual([("to boot dev", "https://www.boot.dev")], matches)

    def test_image_immediate(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)