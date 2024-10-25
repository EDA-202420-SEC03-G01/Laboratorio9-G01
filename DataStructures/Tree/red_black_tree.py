from DataStructures.List import array_list as al
from DataStructures.Tree import rbt_node as rbt_node


#put de BST
def put(my_bst, key, value):
    my_bst["root"] = insert_node(my_bst["root"], key, value)
    return my_bst

def insert_node(root, key, value):
    if root is None:
        nodo = bst_node.new_node(key, value)
        root = nodo
    elif bst_node.get_key(root) == key:
        root["value"] = value
    elif root["key"] > key:
        root["left"] = insert_node(root["left"], key, value)
    else:
        root["right"] = insert_node(root["right"], key, value)
    if root["left"] is not None and root["right"] is not None:
        root["size"] = 1 + root["left"]["size"] + root["right"]["size"]
    if root["left"] is None and root["right"] is not None:
        root["size"] = 1 + root["right"]["size"]
    if root["right"] is None and root["left"] is not None:
        root["size"] = 1 + root["left"]["size"]
    return root