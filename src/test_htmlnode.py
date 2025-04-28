import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_props(self):
        node = HTMLNode("p", "This is a paragraph.", None, {"href": "randomlink.com", "target": "_blank"})
        self.assertEqual(node.props_to_html()[0], " ")
        self.assertEqual(repr(node), "HTMLNode(tag: p, value: This is a paragraph., children: None, props: {'href': 'randomlink.com', 'target': '_blank'})")
    
    def test_no_props(self):
        node = HTMLNode("p", "This is a paragraph.")
        self.assertEqual(node.props_to_html(), "")
    
    def test_empty_node(self):
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), "")
        self.assertEqual(repr(node), "HTMLNode(tag: None, value: None, children: None, props: None)")

    def test_repr(self):
        node = HTMLNode("p", "This is a paragraph.", None, {"href": "randomlink.com", "target": "_blank"})
        node_string = repr(node)
        self.assertIn("HTMLNode(", node_string)
        self.assertIn("tag", node_string)
        self.assertIn("value", node_string)
        self.assertIn("children", node_string)
        self.assertIn("props", node_string)
    
    def test_arg_order(self):
        node = HTMLNode(props={"href": "randomlink.com"}, value="Title Goes Here", tag="h1")
        node_string = repr(node)
        self.assertIn("tag: h1", node_string)
        self.assertIn("value: Title Goes Here", node_string)
        self.assertIn("props: {'href': 'randomlink.com'}", node_string)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_h1(self):
        node = LeafNode("h1", "Hello, world!")
        self.assertEqual(node.to_html(), "<h1>Hello, world!</h1>")

    def test_leaf_to_html_hyperlink(self):
        node = LeafNode("a", "Website Link", {'href': 'https://example.com'})
        self.assertEqual(node.to_html(), '<a href="https://example.com">Website Link</a>')

    def test_leaf_to_html_image(self):
        node = LeafNode("img", "", {"src": "/example/filepath/orange.png", "alt": "An orange"})
        self.assertEqual(node.to_html(), '<img src="/example/filepath/orange.png" alt="An orange"></img>')


if __name__ == "__main__":
    unittest.main()