import unittest
from markdown_functions import markdown_to_blocks

class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
        
    def test_empty_string(self):
        md = ""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks, []
        )

    def test_three_newlines(self):
        md = """
This is the first block


This is the second block
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is the first block",
                "This is the second block"
            ]
        )

    def test_excessive_newlines(self):
        md = """






This is the first block










This is the second block








"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is the first block",
                "This is the second block"
            ]
        )