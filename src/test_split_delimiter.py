import unittest

from textnode import TextNode, TextType
from helper_functions import split_nodes_delimiter

class TestSplitDelimiter(unittest.TestCase):
    def test_bold_delim(self):
        node = TextNode("This word is **bold**, but only in the middle", TextType.TEXT)
        split_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(len(split_nodes), 3)
        self.assertEqual(split_nodes, [TextNode("This word is ", TextType.TEXT), 
                                       TextNode("bold" , TextType.BOLD), 
                                       TextNode(", but only in the middle", TextType.TEXT)])
    
    def test_multiple_nodes(self):
        node1 = TextNode("First _italic_ word", TextType.TEXT)
        node2 = TextNode("Already BOLD", TextType.BOLD)
        node3 = TextNode("Last _word_ also italic", TextType.TEXT)
        split_nodes = split_nodes_delimiter([node1, node2, node3], "_", TextType.ITALIC)
        self.assertEqual(len(split_nodes), 7)
        self.assertEqual(split_nodes, [TextNode("First ", TextType.TEXT),
                                       TextNode("italic", TextType.ITALIC),
                                       TextNode(" word", TextType.TEXT),
                                       TextNode("Already BOLD", TextType.BOLD),
                                       TextNode("Last ", TextType.TEXT),
                                       TextNode("word", TextType.ITALIC),
                                       TextNode(" also italic", TextType.TEXT)])

    def test_multiple_delims(self):
        node = TextNode("I told him **no way man**, but he said **yes way** or something", TextType.TEXT)
        split_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(len(split_nodes), 5)
        self.assertEqual(split_nodes, [TextNode("I told him ", TextType.TEXT),
                                       TextNode("no way man", TextType.BOLD),
                                       TextNode(", but he said ", TextType.TEXT),
                                       TextNode("yes way", TextType.BOLD),
                                       TextNode(" or something", TextType.TEXT),])

    def test_multiple_nodes_and_delims(self):
        node = TextNode("I told him **no way man**, but he said **yes way** or something", TextType.TEXT)
        node2 = TextNode("Last **bold** word", TextType.TEXT)
        split_nodes = split_nodes_delimiter([node, node2], "**", TextType.BOLD)
        self.assertEqual(len(split_nodes), 8)
        self.assertEqual(split_nodes, [TextNode("I told him ", TextType.TEXT),
                                       TextNode("no way man", TextType.BOLD),
                                       TextNode(", but he said ", TextType.TEXT),
                                       TextNode("yes way", TextType.BOLD),
                                       TextNode(" or something", TextType.TEXT),
                                       TextNode("Last ", TextType.TEXT),
                                       TextNode("bold", TextType.BOLD),
                                       TextNode(" word", TextType.TEXT),])

    def test_delim_at_beginning(self):
        node = TextNode("`Code Block` period!", TextType.TEXT)
        split_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(len(split_nodes), 3)
        self.assertEqual(split_nodes, [TextNode("", TextType.TEXT),
                                       TextNode("Code Block", TextType.CODE),
                                       TextNode(" period!", TextType.TEXT)])

    def test_multiple_passes(self):
        node = TextNode("This sentence has **bold** words and _italic_ words in it", TextType.TEXT)
        split_nodes1 = split_nodes_delimiter([node], "**", TextType.BOLD)
        split_nodes2 = split_nodes_delimiter(split_nodes1, "_", TextType.ITALIC)
        self.assertEqual(split_nodes2, [TextNode("This sentence has ", TextType.TEXT),
                                       TextNode("bold", TextType.BOLD),
                                       TextNode(" words and ", TextType.TEXT),
                                       TextNode("italic", TextType.ITALIC),
                                       TextNode(" words in it", TextType.TEXT)])