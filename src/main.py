from textnode import TextNode, TextType

def main():
    test = TextNode("blah blah", TextType.BOLD)
    test2 = TextNode("blah blah", TextType.BOLD)
    print(test)
    print(test == test2)

main()