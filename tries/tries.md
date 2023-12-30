## Overview
A trie is a data structure, also called a prefix tree, is helpful when performing word searches.  In linear time we can look in a group of text and determine if a word or prefix exists. We are able to insert, search a word, and search a prefix in O(n) time.

The datas structure consists of a graph of nodes where each node can have 0 to 26 children.  Each node also has boolean property stating whether or not the letter is the end of a word. Below is an example of a trie consisting of the words "hey" and "hi".
![image](https://github.com/mlizchap/DataStructureNotes/assets/40478204/82271a20-ceab-4c5b-bbdf-f682fca0714c)


## Creating the Nodes
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

## Creating the Class
Next let's take a look at creating the main Trie class.  We'll start by initiating it with an empty root node.  This node will eventually connect to all of the other nodes.
```python
class Trie:
    def __init__(self):
        self.root = TrieNode()
```

## Insert
In order to add nodes to the class, we'll use an insert method.  When adding a word we'll create a pointer and point it to the root.  We'll then iterate through each of the characters in the word and do a check if the letter is in the current node's children or not.  If not we'll create a new node and add this new node to the current node's children.  We'll then point the current node's next pointer to the child node of the letter.  This will either be the new node created or the existing node if it exists.  Finally when we're on the last letter, we'll set the word flag to True, indicating it's the last letter of a word.
```python
def insert(self, word):
    curr = self.root
    for c in word:
        if c not in curr.children:
            curr.children[c] = TrieNode()
        curr = curr.children[c]
    curr.word = True
```
[PIC]

## search
Let's now look at the method that will search for a complete word. Just as in the `insert` method, we'll create a current pointer set to the root and then interate through the characters in the word.  
```python
def search(self, word):
    curr = self.root
    for c in word:
        if c not in curr.children:
            return False
        curr = curr.children[c]
    return curr.word
```
## starts with

