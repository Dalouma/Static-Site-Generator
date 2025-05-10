import unittest
from converters import markdown_to_html_node

class TestMarkdownToHTMLNode(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_codeblock_with_extra_backticks(self):
        md = """
```
`This is text that _should_ remain
the **same** even with inline stuff`
```
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>`This is text that _should_ remain\nthe **same** even with inline stuff`\n</code></pre></div>",
        )

    def test_different_headers(self):
        md = """
# This is header 1

## This is header 2

###### This is header 6

"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>This is header 1</h1><h2>This is header 2</h2><h6>This is header 6</h6></div>",
        )

    def test_one_block_quote(self):
        md = """
> Hello, hello!
> An unbelievable sight.
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote><p>Hello, hello! An unbelievable sight.</p></blockquote></div>"
        )

    def test_block_quote_no_space(self):
        md = """
> Hello, hello!
>An unbelievable sight.
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote><p>Hello, hello! An unbelievable sight.</p></blockquote></div>"
        )

    def test_block_quote_two_para(self):
        md = """
>Hello, hello!
>An unbelievable sight.
>
>I had no idea.
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote><p>Hello, hello! An unbelievable sight.</p><p>I had no idea.</p></blockquote></div>"
        )

    def test_block_quote_with_inline_md(self):
        md = """
>_Hello, hello!_
> An **unbelievable** sight.
>
> `I had no idea.`
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote><p><i>Hello, hello!</i> An <b>unbelievable</b> sight.</p><p><code>I had no idea.</code></p></blockquote></div>"
        )

    def test_one_unordered_list(self):
        md = """
- Elden Ring
- Expedition 33
- Monster Hunter Wilds
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>Elden Ring</li><li>Expedition 33</li><li>Monster Hunter Wilds</li></ul></div>"
        )

    def test_two_unordered_lists(self):
        md = """
- Elden Ring
- Expedition 33
- Monster Hunter Wilds

- Wuthering Waves
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>Elden Ring</li><li>Expedition 33</li><li>Monster Hunter Wilds</li></ul><ul><li>Wuthering Waves</li></ul></div>"
        )

    def test_unordered_list_with_inline_md(self):
        md = """
- _Elden_ Ring
- Expedition **33**
- `Monster Hunter` Wilds
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li><i>Elden</i> Ring</li><li>Expedition <b>33</b></li><li><code>Monster Hunter</code> Wilds</li></ul></div>"
        )

    def test_unordered_list_with_empty_element(self):
        md = """
- Elden Ring
- 
- Monster Hunter Wilds
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>Elden Ring</li><li></li><li>Monster Hunter Wilds</li></ul></div>"
        )

    def test_one_ordered_list(self):
        md = """
1. Elden Ring
2. Expedition 33
3. Monster Hunter Wilds
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>Elden Ring</li><li>Expedition 33</li><li>Monster Hunter Wilds</li></ol></div>"
        )

    def test_ordered_list_with_numerical_first_char(self):
        md = """
1. Elden Ring
2. 69 Nice
3. Monster Hunter Wilds
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>Elden Ring</li><li>69 Nice</li><li>Monster Hunter Wilds</li></ol></div>"
        )

    def test_ordered_list_with_extra_whitespace(self):
        md = """
1.     Elden Ring
2.   69 Nice
3.              Monster Hunter Wilds
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>Elden Ring</li><li>69 Nice</li><li>Monster Hunter Wilds</li></ol></div>"
        )