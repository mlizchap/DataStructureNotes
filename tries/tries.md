## Overview
A trie is a data structure, also called a prefix tree, is helpful when performing word searches.  In linear time we can look in a group of text and determine if a word or prefix exists. We are able to insert, search a word, and search a prefix in O(n) time.

The datas structure consists of a graph of nodes where each node can have 0 to 26 children.  Each node also has boolean property stating whether or not the letter is the end of a word. Below is an example of a trie consisting of the words "hey there you".
![image](https://github.com/mlizchap/DataStructureNotes/assets/40478204/c6215973-feb7-4d60-a433-cb3c7505b187)



## Creating the class
The smallest component of a trie is a node.  Each node represents a letter and will have a `children` and `word` property.  The `children` property can either be an array consisting of the letters of the alphabet or a hashmap.  Either way it will be an organization of all the potential child nodes.  The other property, `word`, will consist of whether or not the letter is the end of the word.

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False
```
The following example represents the word "hey".
![image](https://github.com/mlizchap/DataStructureNotes/assets/40478204/b94a5f75-dd49-4aae-b631-10c69a9a0cd0)

The root will be as follows:
```python
class TrieNode:
    def __init__(self):
        self.children = {"h"}
        self.word = False
```

The next 2 nodes will be the follwing:
```python
class TrieNode:
    def __init__(self):
        self.children = {"e"}
        self.word = False

class TrieNode:
    def __init__(self):
        self.children = {"y"}
        self.word = True
```
And finally the last node will look similar to the previous nodes, except that the `word` property will be set to True, indicating the end of a complete word and the hash set will be empty, indicating there are no following letters.
```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = True
```

For example when creating the word "hey" we will first create an empty trie node as the root.  The root will then point to the trie node "h" by adding it to its children, "h" will point to the node "e", and finally "e" will point to "y". The letter "y" will have a `word` property set to `True` indicating it's the end of a word, while the other letters will be set to `False`.



## Insert

## search

## starts with

