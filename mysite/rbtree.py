# Red-Black Tree, described in Chapter 13 of CLRS
from typing import Any

class RBtree:
    def __init__(self) -> None:
        self.__NIL = {'key': '','value':None,'isBlack':True,'parent':None,'leftChild':None,'rightChild':None}
        self.__root = self.__NIL
        self.__size = 0

    def __nodeByKey(self, key) -> dict[str, Any]:
        node = self.__root
        while node['key'] != key and node != self.__NIL:
            if key < node['key']:
                node = node['leftChild']
            else:
                node = node['rightChild']
        return node

    def __leftRotate(self, x) -> None:
        y = x['rightChild']
        y['parent'] = x['parent'] 
        if y['parent'] == self.__NIL:
            self.__root = y
        elif y['parent']['leftChild'] == x:
            y['parent']['leftChild'] = y
        else:
            y['parent']['rightChild'] = y
        x['rightChild'] = y['leftChild']
        if x['rightChild'] is not self.__NIL: x['rightChild']['parent'] = x
        y['leftChild'] = x
        x['parent'] = y

    def __rightRotate(self, y) -> None:
        x = y['leftChild']
        x['parent'] = y['parent']
        if x['parent'] == self.__NIL:
            self.__root = x
        elif x['parent']['leftChild'] == y:
            x['parent']['leftChild'] = x
        else:
            x['parent']['rightChild'] = x
        y['leftChild'] = x['rightChild']
        if y['leftChild'] is not self.__NIL: y['leftChild']['parent'] = y
        x['rightChild'] = y
        y['parent'] = x

    def __fixTree(self, node) -> None:
        nodeParent = node['parent']
        if nodeParent['isBlack']:
            self.__root['isBlack'] = True
            return
        nodeGrandParent = nodeParent['parent']
        if nodeParent == nodeGrandParent['leftChild']:
            nodeuncle = nodeGrandParent['rightChild']
            if nodeuncle['isBlack'] == False:
                nodeParent['isBlack'] = nodeuncle['isBlack'] = True
                nodeGrandParent['isBlack'] = False
                return self.__fixTree(nodeGrandParent)
            if node == nodeParent['rightChild']:
                self.__leftRotate(nodeParent)
                self.__rightRotate(nodeGrandParent)
                node['isBlack'] = True
                nodeGrandParent['isBlack'] = False
                return
            self.__rightRotate(nodeGrandParent)
            nodeParent['isBlack'] = True
            nodeGrandParent['isBlack'] = False
        else:
            nodeuncle = nodeGrandParent['leftChild']
            if nodeuncle['isBlack'] == False:
                nodeParent['isBlack'] = nodeuncle['isBlack'] = True
                nodeGrandParent['isBlack'] = False
                return self.__fixTree(nodeGrandParent)
            if node == nodeParent['leftChild']:
                self.__rightRotate(nodeParent)
                nodeParent = node
            self.__leftRotate(nodeGrandParent)
            nodeParent['isBlack'] = True
            nodeGrandParent['isBlack'] = False

    def insert(self, key, value) -> None:
        self.__size += 1
        traversalNode = self.__root
        if traversalNode == self.__NIL:  # Empty tree.
            self.__root = {'key': key,'value':value,'isBlack':True,'parent':self.__NIL,'leftChild':self.__NIL,'rightChild':self.__NIL}
            return
        y = self.__NIL
        newNode = {'key': key,'value':value,'isBlack':False,'parent':self.__NIL,'leftChild':self.__NIL,'rightChild':self.__NIL}
        #Travel down until we reach a leaf of the tree
        while traversalNode != self.__NIL:
            y = traversalNode
            if key < traversalNode['key']:
                traversalNode = traversalNode['leftChild'] #Node is equal to left subnode
            else:
                traversalNode = traversalNode['rightChild'] #right subnode
        #add the new node to the correct side of the parent node
        newNode['parent'] = y
        if y == self.__NIL:
            self.__root == newNode # create a traversalNode here
        elif newNode['key'] < y['key']:
            y['leftChild'] = newNode
        else:
            y['rightChild'] = newNode
        self.__fixTree(newNode)
                
    def GetValue(self, key) -> str:
        node = self.__nodeByKey(key)
        if node != self.__NIL:
            #print(key, 'exists.')
            return node['value']
        else:
            #print(key, 'does not exist.')
            return None

    def treeWalk(self, node=None) -> None:
        if node == None: node = self.__root
        if node != self.__NIL:
            self.treeWalk(node['leftChild'])
            print(node['key'])
            self.treeWalk(node['rightChild'])