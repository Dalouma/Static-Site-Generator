import unittest
from markdown_functions import extract_title


class TestExtractTitle(unittest.TestCase):
    def test_only_header(self):
        md = """
# This is a header
"""
        h1 = extract_title(md)
        self.assertEqual(
            h1,
            "This is a header"
        )

    def test_header_and_other(self):
        md = """
# This is a header

This is a paragraph.
It has words in it
"""

    def test_no_header(self):
        md = """
This is a paragraph
"""
        try:
            extract_title(md)
        except Exception:
            return