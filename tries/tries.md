## Overview
A trie is a data structure, also called a prefix tree, is helpful when performing word searches.  In linear time we can look in a group of text and determine if a word or prefix exists. We are able to insert, search a word, and search a prefix in O(n) time.

The datas structure consists of a graph of nodes where each node can have 0 to 26 children.  Each node also has boolean property stating whether or not the letter is the end of a word. Below is an example of a trie consisting of the words "hey there you".
[PIC 1]

## Creating the class
The smallest component of a trie is a node.  Each node represents a letter and will have a `children` and `word` property.  The `children` property can either be an array consisting of the letters of the alphabet or a hashmap.  Either way it will be an organization of all the potential child nodes.  The other property, `word`, will consist of whether or not the letter is the end of the word.

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False
```

For example when creating the word "hey" we will first create an empty trie node as the root.  The root will then point to the trie node "h" by adding it to its children, "h" will point to the node "e", and finally "e" will point to "y". The letter "y" will have a `word` property set to `True` indicating it's the end of a word, while the other letters will be set to `False`.



## Insert

## search

## starts with

