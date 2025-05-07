import unittest
from markdown_functions import *

class TestBlockToBlockType(unittest.TestCase):
    def test_heading(self):
        block = "### this is a heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)

    def test_code(self):
        block = """```This is a code block```"""
        self.assertEqual(block_to_block_type(block), BlockType.CODE)
    
    def test_empty_code_block(self):
        block = """``````"""
        self.assertEqual(block_to_block_type(block), BlockType.CODE)

    def test_quotes(self):
        block = ">The quick brown fox\n>Jumps over the lazy dog."
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)
    
    def test_not_all_quotes(self):
        block = ">This is a quote.\nBut this one is not"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_empty_quote(self):
        block = ">"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)

    def test_unordered_list(self):
        block = "- First item\n- second item\n- third item"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)

    def test_not_all_list_items(self):
        block = ">This is a quote.\n- But this is an unordered list item"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_ordered_list(self):
        block = "1. Item 1\n2. Item 2\n3. Item 3"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)

    def test_incorrect_ordering(self):
        block = "1. Item 1\n32. Item 2\n3. Item 3"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_incorrect_ordering_two(self):
        block = "1. Item 1\n2. Item 2\n32. Item 3"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_empty_item(self):
        block = "1. item one\n2. \n3. item three"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)

    def test_missing_space(self):
        block = "1. item one\n2.\n3. item three"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_mixed_list(self):
        block = "1. item one\n- item two"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_mixed_list_two(self):
        block = "- item one\n2. item two"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_double_digit_length_ordered_list(self):
        block = """1. item one
2. item two
3. item three
4. item four
5. item five
6. item six
7. item seven
8. item eight
9. item nine
10. item ten
11. item eleven
12. item twelve
13. item thirteen"""
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)