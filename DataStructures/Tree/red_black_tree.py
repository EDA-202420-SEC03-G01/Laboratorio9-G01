from DataStructures.List import array_list as al
from DataStructures.Tree import rbt_node as rbt_node


#put de BST
def put(my_bst, key, value):
    my_bst["root"] = insert_node(my_bst["root"], key, value)
    return my_bst

#todavía no lo hemos completado
def insert_node(root, key, value):
    contador = 0
    if root is None:
        nodo = rbt_node.new_node(key, value)
        root = nodo
    elif rbt_node.get_key(root) == key:
        root["value"] = value
    elif root["key"] > key:
        root["left"] = insert_node(root["left"], key, value)
        contador += 1
        if contador == 2:
            rotate_right(root)
    else:
        root["right"] = insert_node(root["right"], key, value)
        rotate_left(root['right'])
    #size
    if root["left"] is not None and root["right"] is not None:
        root["size"] = 1 + root["left"]["size"] + root["right"]["size"]
    if root["left"] is None and root["right"] is not None:
        root["size"] = 1 + root["right"]["size"]
    if root["right"] is None and root["left"] is not None:
        root["size"] = 1 + root["left"]["size"]
    
    
    return root

def rotate_left(node):
    """ 
    Rota el hijo derecho hacia la izquierda.
    Args:
        node: nodo que tiene hijo derecho rojo.
    Return:
        Nuevo nodo con el hijo izquierdo rojo
    Solución:
    1. Intercambiar el hijo izquierdo del hijo derecho del nodo
    por el hijo derecho del nodo.
    2. Intercambia los colores del nodo y del hijo derecho del nodo

    """
    #1
    node["right"]["left"]["left"] = node["right"]
    node["right"] = node["right"]["left"]
    #2
    
    


def rotate_right(node):
    """
    Rota el hijo izquierdo hacia la derecha.
    Args:
    node: nodo que tiene hijo izquierdo rojo.
    Return:
    Nuevo nodo con el hijo derecho rojo
    Solución:
    1. Intercambiar el hijo derecho del hijo izquierdo del nodo
    por el hijo izquierdo del nodo.
    2. Intercambia los colores del nodo y del hijo izquierdo del nodo.
    """
    

def flip_colors(node):
    """
    Cambiar los colores del nodo y de sus hijos izquierdo
    y derecho.
    """
    flip_node_color(node)
    flip_node_color(node['left'])
    flip_node_color(node['right'])
    

def flip_node_color(node):
    """
    Cambiar el color del nodo: RED pasa a BLACK y
    BLACK pasa a RED.
    """
    color = node['color']
    if color == 'RED':
        color = 'BLACK'
    elif color == 'BLACK':
        color = 'RED'

#funciones que en teoría deberían funcionar
def new_map(cmp_function):
    """
    Crear un mapa ordenado basado en un árbol binario ordenado balanceado RBT.
    El árbol inicialmente esta vacio.
    """
    rbt = {'root': None, # rbt_node inicial
    'cmp_function': cmp_function, # función de comparación de llaves
    'type': 'RBT' }
    if(cmp_function is None):
        rbt['cmp_function'] = sort_crit
    return rbt

def sort_crit(ele1, ele2):
    return ele1 < ele2
    

def get(my_bst, key):
    valor = recorrido_get(my_bst['root'], key)
    return valor

def recorrido_get(nodo, key):
    llave = rbt_node.get_key(nodo)
    if nodo != None:
        if key == llave:
            return rbt_node.get_value(nodo)
        elif key > llave:
            return recorrido_get(nodo['right'],key)
        else:
            return recorrido_get(nodo['left'],key)
    else:
        return None
    
def contains(my_bst, key):
    contain = recorrido_con(my_bst['root'], key)
    return contain

def recorrido_con(nodo, key):
    llave = rbt_node.get_key(nodo)
    if nodo != None:
        if key == llave:
            return True
        elif key > llave:
            return recorrido_get(nodo['right'],key)
        else:
            return recorrido_get(nodo['left'],key)
    else:
        return False

def size(my_bst):
    if my_bst['root'] is None:
        size = 0
    else: 
        size = my_bst['root']['size']
    return size

def is_empty(my_bst):
    vacia = False
    if my_bst['root'] is None:
        vacia = True
    return vacia

def key_set(my_bst):
    key_list = al.new_list()
    if is_empty != True:
        root = my_bst['root']
        recursive_search_key(root,key_list)          
    return key_list

def recursive_search_key(nodo,lista):
    if nodo != None:
        recursive_search_key(nodo['left'],lista)
        al.add_last(lista, nodo['key'])
        recursive_search_key(nodo['right'],lista)
        
def value_set(my_bst):
    value_list = al.new_list()
    if is_empty != True:
        root = my_bst['root']
        recursive_search_value(root,value_list)
    return value_list

def recursive_search_value(nodo,lista):
    if nodo != None:
        recursive_search_value(nodo['left'],lista)
        al.add_last(lista, nodo['value'])
        recursive_search_value(nodo['right'],lista)

def left_key(my_bst):
    min_llave = min_key_node(my_bst['root'])
    return min_llave

def min_key_node(nodo):
    if nodo is None:
        return None
    elif nodo['left'] is None:
        return nodo['key']
    else:
        return min_key_node(nodo['left'])

def right_key(my_bst):
    min_llave = max_key_node(my_bst['root'])
    return min_llave

def max_key_node(nodo):
    if nodo is None:
        return None
    elif nodo['right'] is None:
        return nodo['key']
    else:
        return max_key_node(nodo['right'])
    
#ya hechas (Santiago)

def height(my_bst):
    if my_bst == None:
        return -1
    else: 
        nodo = my_bst.get("key")
        if nodo == None: 
            if my_bst["root"] == None:
                return -1
            else:
                return recursive_height(my_bst["root"])
        else:
            return recursive_height(my_bst)

def recursive_height(node):
    if node == None:
        return -1
    else:
        left_h = recursive_height(node["left"])
        right_h = recursive_height(node["right"])
        return 1 + max(left_h, right_h)

def keys(my_bst, lo_key, hi_key):
    key_list = al.new_list()
    if my_bst != None:
        if my_bst["root"] != None:
            recursive_search_keys(my_bst["root"], lo_key, hi_key, key_list)
    al.quick_sort(key_list, sort_crit)
    return key_list

def values(my_bst, lo_key, hi_key):
    key_list = al.new_list()
    if my_bst != None:
        if my_bst["root"] != None:
            recursive_search_values(my_bst["root"], lo_key, hi_key, key_list)
    al.quick_sort(key_list, sort_crit)
    return key_list

def recursive_search_keys(nodo, lo_key, hi_key, lista):
    if nodo != None:
        if lo_key <= nodo["key"] <= hi_key:
            al.add_last(lista, nodo["key"])
            recursive_search_keys(nodo["right"], lo_key, hi_key, lista)
            recursive_search_keys(nodo["left"], lo_key, hi_key, lista)
        elif nodo["key"] > hi_key:
            recursive_search_keys(nodo["left"], lo_key, hi_key, lista)
        elif nodo["key"] < lo_key:
            recursive_search_keys(nodo["right"], lo_key, hi_key, lista)

def recursive_search_values(nodo, lo_key, hi_key, lista):
    if nodo != None:
        if lo_key <= nodo["value"] <= hi_key:
            al.add_last(lista, nodo["value"])
        recursive_search_values(nodo["right"], lo_key, hi_key, lista)
        recursive_search_values(nodo["left"], lo_key, hi_key, lista)
        

def sort_crit(ele1, ele2):
    return ele1 < ele2