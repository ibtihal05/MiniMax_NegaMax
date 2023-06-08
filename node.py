from interface import nodes_positions,vals
nodes_positions=nodes_positions
vals=vals
global feuille
feuille=0
class Node:
      
    def __init__(self, parent=None, leftChild=None, rightChild=None, val=None, position=None, path=None):
        self.parent = parent
        self.leftChild = leftChild
        self.rightChild = rightChild
        self.val = val
        self.position = position
        self.path = path


def create_tree(father, nb_level, nb_level_final, nodes):
    global feuille
    if father==None : #first node 'root'
        father=Node()
        father.position = nodes_positions.pop(0)
        nodes.append(father)
    
    leftChild=Node(father)
    rightChild=Node(father)

    father.leftChild=leftChild
    father.rightChild=rightChild

    leftChild.position=nodes_positions.pop(0)
    rightChild.position=nodes_positions.pop(0)
    nodes.append(leftChild)
    nodes.append(rightChild)
    
    if(nb_level<nb_level_final-1) :
        create_tree(leftChild, nb_level+1, nb_level_final, nodes)
        create_tree(rightChild, nb_level+1, nb_level_final, nodes)
    else :
        leftChild.val=int(vals[feuille])
        feuille=feuille+1
        rightChild.val=int(vals[feuille])
        feuille=feuille+1




