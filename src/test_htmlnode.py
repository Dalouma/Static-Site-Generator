import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


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

    def test_leaf_to_html_no_val(self):
        node = LeafNode('p')
        try:
            print(node.to_html())
        except ValueError:
            return
        # FAIL
        self.assertEqual(0, 1)

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_multiple_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_to_html_with_3gens_2children(self):
        grandparent = ParentNode(
            "p",
            [
                ParentNode(
                    "div",
                    [
                        LeafNode("b", "Bold Text"),
                        LeafNode("img", "", {"src": "/example/filepath/picture.jpg", "alt": "A Picture"})
                    ]
                ),
                ParentNode(
                    "div",
                    [
                        LeafNode("a", "Click me!", {"href": "https://example.com"}),
                        LeafNode("i", "Italic Text")
                    ]
                )
            ]
        )
        self.assertEqual(grandparent.to_html(), '<p><div><b>Bold Text</b><img src="/example/filepath/picture.jpg" alt="A Picture"></img></div><div><a href="https://example.com">Click me!</a><i>Italic Text</i></div></p>')

    def test_to_html_with_parent_no_children(self):
        node = ParentNode('p', [])
        self.assertEqual(node.to_html(), '<p></p>')

    def test_to_html_with_parent_None_children(self):
        node = ParentNode('p', None)
        try:
            print(node.to_html())
        except ValueError:
            return
        self.assertEqual(0, 1)

    def test_to_html_with_parent_None_Tag(self):
        node = ParentNode(None, "text")
        try:
            print(node.to_html())
        except ValueError:
            return
        self.assertEqual(0, 1)

if __name__ == "__main__":
    unittest.main()