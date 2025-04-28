import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props(self):
        node = HTMLNode("p", "This is a paragraph.", None, {"href": "randomlink.com", "target": "_blank"})
        self.assertEqual(node.props_to_html()[0], " ")

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
        


if __name__ == "__main__":
    unittest.main()