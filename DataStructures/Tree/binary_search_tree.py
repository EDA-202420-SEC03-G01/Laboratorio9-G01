from DataStructures.List import array_list as al
from DataStructures.Tree import bst_node as bst_node

def remove (my_bst, key):
    my_bst['root'] = remove_rec(my_bst['root'], key, my_bst['cmp_function'])
    return my_bst
    
def remove_rec(nodo, key, cmp_function):
    """
    Eliminar el nodo con la key en el BST.
    Retornar el nodo BST resultante sin el nodo que contiene la key.
    Args:
    node: nodo desde donde se busca la key a eliminar
    key: llave a eliminar
    Solución:
    Si el node es None -> retornar None
    Si el node NO es None:
    (1) si key es igual a node['key'] (nodo a eliminar) -> revisar Opción 1 casos 1.1, 1.2 y 1.3
    Actualizar la propiedad 'size' de los nodos involucrados.
    (2) si key es menor a node['key'] -> Continuar la eliminación por el node['left']
    (3) si key es mayor a node['key'] -> Continuar la eliminación por el node['right']
    """
    llave = bst_node.get_key(nodo)
    if nodo != None:
        if key == llave:
            if root.left is None:
            return root.right

        # When root has only left child
        if root.right is None:
            return root.left

        # When both children are present
        succ = get_successor(root)
        root.key = succ.key
        root.right = del_node(root.right, succ.key)
        elif key > llave:
            return recorrido_get(nodo['right'],key)
        else:
            return recorrido_get(nodo['left'],key)
    else:
        return None

def new_map():
    mapa = {'root': None,
     'type': "BST"}
    return mapa

def get(my_bst, key):
    valor = recorrido_get(my_bst['root'], key)
    return valor

def recorrido_get(nodo, key):
    llave = bst_node.get_key(nodo)
    if nodo != None:
        if key == llave:
            return bst_node.get_value(nodo)
        elif key > llave:
            return recorrido_get(nodo['right'],key)
        else:
            return recorrido_get(nodo['left'],key)
    else:
        return None

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

def contains(my_bst, key):
    contain = recorrido_con(my_bst['root'], key)
    return contain

def recorrido_con(nodo, key):
    llave = bst_node.get_key(nodo)
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

def min_key(my_bst):
    min_llave = min_key_node(my_bst['root'])
    return min_llave

def min_key_node(nodo):
    if nodo is None:
        return None
    elif nodo['left'] is None:
        return nodo['key']
    else:
        return min_key_node(nodo['left'])

def max_key(my_bst):
    min_llave = max_key_node(my_bst['root'])
    return min_llave

def max_key_node(nodo):
    if nodo is None:
        return None
    elif nodo['right'] is None:
        return nodo['key']
    else:
        return max_key_node(nodo['right'])

#cambiar
def delete_min(my_bst):
    my_bst['root'] = delete_min_rec(my_bst['root'])
    return my_bst

#no funciona todavía
def delete_min_rec(nodo):
    if nodo is None:
        return None
    else:
        if nodo['left'] is None:
            return nodo['right']
        else:
            delete_min_rec(nodo['left'])
            nodo['size'] -= 1

def delete_max(my_bst):
    max_llave = max_key(my_bst)
    remove(my_bst, max_llave)
    return my_bst

def floor(my_bst, key):
    lista = key_set(my_bst)
    pos = al.is_present(lista, key, cmp_function)
    llave_menor = None
    if al.is_empty(lista) != True:
        if pos != 0:
            llave_menor = lista[pos-1]
        else:
            llave_menor = lista[pos]
    return llave_menor

def ceiling(my_bst, key):
    lista = key_set(my_bst)
    pos = al.is_present(lista, key, cmp_function)
    llave_mayor = None
    if al.is_empty(lista) != True:
        if pos != al.size(lista):
            llave_mayor = lista[pos+1]
        else:
            llave_mayor = lista[pos]
    return llave_mayor

def select(my_bst, pos):
    lista = key_set(my_bst)
    return ceiling(my_bst,lista[pos])

def cmp_function(uno, dos):
    if uno == dos:
        return 0
    
#ya hechas
def rank(my_bst, key):
    if my_bst["root"] == None:
        return 0
    else:
        return recursive_rank(my_bst["root"], key)

def recursive_rank(node, key):
    if node == None:
        return 0
    elif node["key"] != key:
        if node["key"] > key:
            return recursive_rank(node["left"], key)
        elif node["key"] < key:
            return recursive_rank(node["right"], key)
    else:
        if node["left"] == None:
            return 0
        else:
            return node["left"]["size"]

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