from DataStructures.Tree import binary_search_tree as bst
from DataStructures.Tree import bst_node as bst_node
from DataStructures.Utils.utils import handle_not_implemented


def setup_tests():
    empty_tree = bst.new_map()

    return empty_tree

def setup_one_node():
    one_node = bst.new_map()
    node = bst_node.new_node(1,1)
    
    one_node["root"] = node
    
    return one_node

def setup_three_nodes():
    three_nodes = bst.new_map()
    node_1 = bst_node.new_node(1, 10)
    node_3 = bst_node.new_node(10, 100)
    node_2 = bst_node.new_node(5, 50)

    node_2["left"] = node_1
    node_2["right"] = node_3
    node_2["size"] = 3

    three_nodes["root"] = node_2

    return three_nodes


def setup_seven_nodes():
    seven_nodes = bst.new_map()
    node_1 = bst_node.new_node(10, 100)
    node_2 = bst_node.new_node(20, 200)
    node_3 = bst_node.new_node(30, 300)
    node_4 = bst_node.new_node(40, 400)
    node_5 = bst_node.new_node(50, 500)
    node_6 = bst_node.new_node(60, 600)
    node_7 = bst_node.new_node(70, 700)

    node_2["left"] = node_1
    node_2["right"] = node_3
    node_2["size"] = 3

    node_6["left"] = node_5
    node_6["right"] = node_7
    node_6["size"] = 3

    node_4["left"] = node_2
    node_4["right"] = node_6
    node_4["size"] = 7

    seven_nodes["root"] = node_4

    return seven_nodes

def setup_unbalanced():
    unbalanced = bst.new_map()
    bst.put(unbalanced, 40, 40)
    bst.put(unbalanced, 20, 20)
    bst.put(unbalanced, 10, 10)
    bst.put(unbalanced, 30, 30)
    bst.put(unbalanced, 50, 50)
    bst.put(unbalanced, 60, 60)
    bst.put(unbalanced, 70, 70)
    bst.put(unbalanced, 80, 80)
    bst.put(unbalanced, 90, 90)
    
    return unbalanced

@handle_not_implemented
def test_new_binary_search_tree():
    empty_bst = bst.new_map()

    print(empty_bst)

    assert empty_bst["root"] is None
    assert empty_bst["type"] == "BST"



def test_put():
    empty_bst = setup_tests()
    three_bst = setup_three_nodes()

    # Insertar en un árbol vacío
    bst.put(empty_bst, 1, 1)

    assert empty_bst["root"] is not None
    assert empty_bst["root"] == bst_node.new_node(1, 1)

    # Insertar a la izquierda en un árbol con 3 nodos

    bst.put(three_bst, 7, 7)

    assert three_bst["root"]["right"]["left"]["key"] == 7
    assert three_bst["root"]["right"]["left"]["value"] == 7
    assert three_bst["root"]["right"]["left"]["size"] == 1
    assert three_bst["root"]["right"]["size"] == 2
    assert three_bst["root"]["size"] == 4
    assert three_bst["root"]["left"]["size"] == 1

    # Insertar a la derecha en un árbol con 3 nodos

    bst.put(three_bst, 3, 3)

    assert three_bst["root"]["left"]["right"]["key"] == 3
    assert three_bst["root"]["left"]["right"]["value"] == 3
    assert three_bst["root"]["left"]["right"]["size"] == 1
    assert three_bst["root"]["left"]["size"] == 2
    assert three_bst["root"]["size"] == 5
    assert three_bst["root"]["right"]["size"] == 2

    # Insertar en un árbol con 3 nodos, pero la llave ya existe

    bst.put(three_bst, 10, 9)

    assert three_bst["root"]["right"]["key"] == 10
    assert three_bst["root"]["right"]["value"] == 9
    assert three_bst["root"]["right"]["size"] == 2
    assert three_bst["root"]["size"] == 5
    assert three_bst["root"]["left"]["size"] == 2

    # Insertar en un árbol con 3 nodos, todo a la izquierda

    bst.put(three_bst, 0, 0)

    assert three_bst["root"]["left"]["left"]["key"] == 0
    assert three_bst["root"]["left"]["left"]["value"] == 0
    assert three_bst["root"]["left"]["left"]["size"] == 1
    assert three_bst["root"]["left"]["size"] == 3
    assert three_bst["root"]["size"] == 6
    assert three_bst["root"]["right"]["size"] == 2

    # Insertar en un árbol con 3 nodos, todo a la derecha

    bst.put(three_bst, 15, 15)

    assert three_bst["root"]["right"]["right"]["key"] == 15
    assert three_bst["root"]["right"]["right"]["value"] == 15
    assert three_bst["root"]["right"]["right"]["size"] == 1
    assert three_bst["root"]["right"]["size"] == 3
    assert three_bst["root"]["size"] == 7
    assert three_bst["root"]["left"]["size"] == 3


def test_get():
    empty_bst = setup_tests()
    three_bst = setup_three_nodes()

    # Obtener un valor de un árbol vacío
    assert bst.get(empty_bst, 1) is None

    # Obtener un valor de un árbol con 3 nodos
    assert bst.get(three_bst, 1) == 10
    assert bst.get(three_bst, 5) == 50
    assert bst.get(three_bst, 10) == 100

    # Obtener un valor que no existe en un árbol con 3 nodos
    assert bst.get(three_bst, 0) is None
    assert bst.get(three_bst, 15) is None



def test_remove():
    empty_bst = setup_tests()
    three_bst = setup_three_nodes()
    seven_bst = setup_seven_nodes()

    # Eliminar un valor de un árbol vacío
    bst.remove(empty_bst, 1)

    assert empty_bst["root"] is None

    # Eliminar un valor de un árbol con 3 nodos
    bst.remove(three_bst, 1)

    assert three_bst["root"]["size"] == 2
    assert three_bst["root"]["left"] is None
    assert three_bst["root"]["right"]["key"] == 10
    assert three_bst["root"]["right"]["value"] == 100
    assert three_bst["root"]["right"]["size"] == 1

    # Eliminar un valor que no existe en un árbol con 3 nodos
    bst.remove(three_bst, 0)

    assert three_bst["root"]["size"] == 2
    assert three_bst["root"]["left"] is None
    assert three_bst["root"]["right"] is not None

    # Eliminar un valor que no existe en un árbol con 7 nodos
    bst.remove(seven_bst, 0)

    assert seven_bst["root"]["size"] == 7
    assert seven_bst["root"]["left"] is not None
    assert seven_bst["root"]["right"] is not None

    # Eliminar una hoja de un árbol con 7 nodos
    bst.remove(seven_bst, 10)

    assert seven_bst["root"]["size"] == 6
    assert seven_bst["root"]["left"]["left"] is None
    assert seven_bst["root"]["left"]["right"] is not None

    # Eliminar un nodo con un hijo de un árbol con 7 nodos
    bst.remove(seven_bst, 60)

    assert seven_bst["root"]["size"] == 5
    assert seven_bst["root"]["right"]["right"] is None
    assert seven_bst["root"]["right"]["left"] is not None
    assert seven_bst["root"]["right"]["key"] == 70
    assert seven_bst["root"]["right"]["size"] == 2
    assert seven_bst["root"]["right"]["left"]["key"] == 50


def test_contains():
    empty_bst = setup_tests()
    three_bst = setup_three_nodes()

    # Verificar si un árbol vacío contiene un valor
    assert not bst.contains(empty_bst, 1)

    # Verificar si un árbol con 3 nodos contiene un valor
    assert bst.contains(three_bst, 1)
    assert bst.contains(three_bst, 5)
    assert bst.contains(three_bst, 10)

    # Verificar si un árbol con 3 nodos no contiene un valor
    assert not bst.contains(three_bst, 0)
    assert not bst.contains(three_bst, 15)


def test_size():
    empty_bst = setup_tests()
    three_bst = setup_three_nodes()
    seven_bst = setup_seven_nodes()

    # Verificar el tamaño de un árbol vacío
    assert bst.size(empty_bst) == 0

    # Verificar el tamaño de un árbol con 3 nodos
    assert bst.size(three_bst) == 3

    # Verificar el tamaño de un árbol con 7 nodos
    assert bst.size(seven_bst) == 7


def test_is_empty():
    empty_bst = setup_tests()
    three_bst = setup_three_nodes()

    # Verificar si un árbol vacío está vacío
    assert bst.is_empty(empty_bst)

    # Verificar si un árbol con 3 nodos está vacío
    assert not bst.is_empty(three_bst)


def test_key_set():
    empty_bst = setup_tests()
    three_bst = setup_three_nodes()

    # Verificar el conjunto de llaves de un árbol vacío
    key_set = bst.key_set(empty_bst)

    assert key_set["size"] == 0
    assert key_set["elements"] == []

    # Verificar el conjunto de llaves de un árbol con 3 nodos
    key_set = bst.key_set(three_bst)

    assert key_set["size"] == 3
    assert key_set["elements"][0] == 1
    assert key_set["elements"][1] == 5
    assert key_set["elements"][2] == 10


def test_value_set():
    empty_bst = setup_tests()
    three_bst = setup_three_nodes()

    # Verificar el conjunto de valores de un árbol vacío
    value_set = bst.value_set(empty_bst)

    assert value_set["size"] == 0
    assert value_set["elements"] == []

    # Verificar el conjunto de valores de un árbol con 3 nodos
    value_set = bst.value_set(three_bst)

    assert value_set["size"] == 3
    assert value_set["elements"][0] == 10
    assert value_set["elements"][1] == 50
    assert value_set["elements"][2] == 100


def test_min_key():
    empty_bst = setup_tests()
    three_bst = setup_three_nodes()
    seven_bst = setup_seven_nodes()

    # Verificar la llave mínima de un árbol vacío
    assert bst.min_key(empty_bst) is None

    # Verificar la llave mínima de un árbol con 3 nodos
    assert bst.min_key(three_bst) == 1

    # Verificar la llave mínima de un árbol con 7 nodos
    assert bst.min_key(seven_bst) == 10


def test_max_key():
    empty_bst = setup_tests()
    three_bst = setup_three_nodes()
    seven_bst = setup_seven_nodes()

    # Verificar la llave máxima de un árbol vacío
    assert bst.max_key(empty_bst) is None

    # Verificar la llave máxima de un árbol con 3 nodos
    assert bst.max_key(three_bst) == 10

    # Verificar la llave máxima de un árbol con 7 nodos
    assert bst.max_key(seven_bst) == 70


@handle_not_implemented
def test_delete_min():
    empty_bst = setup_tests()
    three_bst = setup_three_nodes()
    seven_bst = setup_seven_nodes()

    # Eliminar la llave mínima de un árbol vacío
    bst.delete_min(empty_bst)

    assert empty_bst["root"] is None

    # Eliminar la llave mínima de un árbol con 3 nodos
    bst.delete_min(three_bst)

    assert three_bst["root"]["size"] == 2
    assert three_bst["root"]["left"] is None
    assert three_bst["root"]["right"]["key"] == 10
    assert three_bst["root"]["right"]["value"] == 100
    assert three_bst["root"]["right"]["size"] == 1

    # Eliminar la llave mínima de un árbol con 7 nodos
    bst.delete_min(seven_bst)

    assert seven_bst["root"]["size"] == 6
    assert seven_bst["root"]["left"]["left"] is None
    assert seven_bst["root"]["left"]["right"] is not None


@handle_not_implemented
def test_delete_max():
    empty_bst = setup_tests()
    three_bst = setup_three_nodes()
    seven_bst = setup_seven_nodes()

    # Eliminar la llave máxima de un árbol vacío
    bst.delete_max(empty_bst)

    assert empty_bst["root"] is None

    # Eliminar la llave máxima de un árbol con 3 nodos
    bst.delete_max(three_bst)

    assert three_bst["root"]["size"] == 2
    assert three_bst["root"]["left"]["key"] == 1
    assert three_bst["root"]["left"]["value"] == 10
    assert three_bst["root"]["left"]["size"] == 1
    assert three_bst["root"]["right"] is None

    # Eliminar la llave máxima de un árbol con 7 nodos
    bst.delete_max(seven_bst)

    assert seven_bst["root"]["size"] == 6
    assert seven_bst["root"]["right"]["right"] is None
    assert seven_bst["root"]["right"]["left"] is not None
    assert seven_bst["root"]["right"]["key"] == 60
    assert seven_bst["root"]["right"]["size"] == 2
    assert seven_bst["root"]["right"]["left"]["key"] == 50

@handle_not_implemented
def test_floor():
    empty_bst = setup_tests()
    three_bst = setup_three_nodes()
    seven_bst = setup_seven_nodes()

    # Piso de un árbol vacío
    assert bst.floor(empty_bst, 1) is None

    # Piso de un árbol con 3 nodos
    assert bst.floor(three_bst, 0) is None
    assert bst.floor(three_bst, 2) == 1
    assert bst.floor(three_bst, 5) == 5
    assert bst.floor(three_bst, 10) == 10

    # Piso de un árbol con 7 nodos
    assert bst.floor(seven_bst, 5) is None
    assert bst.floor(seven_bst, 10) == 10
    assert bst.floor(seven_bst, 15) == 10
    assert bst.floor(seven_bst, 35) == 30
    assert bst.floor(seven_bst, 50) == 50
    assert bst.floor(seven_bst, 70) == 70
    assert bst.floor(seven_bst, 75) == 70

@handle_not_implemented
def test_ceiling():
    empty_bst = setup_tests()
    three_bst = setup_three_nodes()
    seven_bst = setup_seven_nodes()

    # Techo de un árbol vacío
    assert bst.ceiling(empty_bst, 1) is None

    # Techo de un árbol con 3 nodos
    assert bst.ceiling(three_bst, 0) == 1
    assert bst.ceiling(three_bst, 2) == 5
    assert bst.ceiling(three_bst, 5) == 5
    assert bst.ceiling(three_bst, 10) == 10

    # Techo de un árbol con 7 nodos
    assert bst.ceiling(seven_bst, 5) == 10
    assert bst.ceiling(seven_bst, 10) == 10
    assert bst.ceiling(seven_bst, 15) == 20
    assert bst.ceiling(seven_bst, 35) == 40
    assert bst.ceiling(seven_bst, 50) == 50
    assert bst.ceiling(seven_bst, 70) == 70
    assert bst.ceiling(seven_bst, 75) is None

@handle_not_implemented
def test_select():
    empty_bst = setup_tests()
    three_bst = setup_three_nodes()
    seven_bst = setup_seven_nodes()

    # Seleccionar de un árbol vacío
    assert bst.select(empty_bst, 1) is None

    # Seleccionar de un árbol con 3 nodos
    assert bst.select(three_bst, 1) == 5
    assert bst.select(three_bst, 2) == 10
    assert bst.select(three_bst, 3) == None

    # Seleccionar de un árbol con 7 nodos
    assert bst.select(seven_bst, 1) == 20
    assert bst.select(seven_bst, 2) == 30
    assert bst.select(seven_bst, 3) == 40
    assert bst.select(seven_bst, 4) == 50
    assert bst.select(seven_bst, 5) == 60
    assert bst.select(seven_bst, 6) == 70
    assert bst.select(seven_bst, 7) == None



def test_rank():
    empty_bst = setup_tests()
    three_bst = setup_three_nodes()
    seven_bst = setup_seven_nodes()

    # Rango de un árbol vacío
    assert bst.rank(empty_bst, 1) == 0

    # Rango de un árbol con 3 nodos
    assert bst.rank(three_bst, 1) == 0
    assert bst.rank(three_bst, 5) == 1
    assert bst.rank(three_bst, 10) == 2
    assert bst.rank(three_bst, 0) == 0
    assert bst.rank(three_bst, 15) == 3

    # Rango de un árbol con 7 nodos
    assert bst.rank(seven_bst, 10) == 0
    assert bst.rank(seven_bst, 20) == 1
    assert bst.rank(seven_bst, 30) == 2
    assert bst.rank(seven_bst, 40) == 3
    assert bst.rank(seven_bst, 50) == 4
    assert bst.rank(seven_bst, 60) == 5
    assert bst.rank(seven_bst, 70) == 6
    assert bst.rank(seven_bst, 0) == 0
    assert bst.rank(seven_bst, 75) == 7



def test_height():
    empty_bst = setup_tests()
    one_bst = setup_one_node()
    three_bst = setup_three_nodes()
    seven_bst = setup_seven_nodes()
    unbalanced_bst = setup_unbalanced()


    # Altura de un árbol vacío
    assert bst.height(empty_bst) == -1
    
    # Altura de un árbol con 1 nodo
    assert bst.height(one_bst) == 0

    # Altura de un árbol con 3 nodos
    assert bst.height(three_bst) == 1

    # Altura de un árbol con 7 nodos
    assert bst.height(seven_bst) == 2
    
    # Altura de un arbol desbalanceado
    assert bst.height(unbalanced_bst) == 5

def test_keys():
    empty_bst = setup_tests()
    three_bst = setup_three_nodes()
    seven_bst = setup_seven_nodes()

    # Llaves de un árbol vacío
    keys = bst.keys(empty_bst, 1, 10)

    assert keys["size"] == 0
    assert keys["elements"] == []

    # Llaves de un árbol con 3 nodos
    keys = bst.keys(three_bst, 1, 10)

    assert keys["size"] == 3
    assert keys["elements"][0] == 1
    assert keys["elements"][1] == 5
    assert keys["elements"][2] == 10

    # Llaves de un árbol con 7 nodos
    keys = bst.keys(seven_bst, 1, 100)

    assert keys["size"] == 7
    assert keys["elements"][0] == 10
    assert keys["elements"][1] == 20
    assert keys["elements"][2] == 30
    assert keys["elements"][3] == 40
    assert keys["elements"][4] == 50
    assert keys["elements"][5] == 60
    assert keys["elements"][6] == 70


def test_values():
    empty_bst = setup_tests()
    three_bst = setup_three_nodes()
    seven_bst = setup_seven_nodes()

    # Valores de un árbol vacío
    values = bst.values(empty_bst, 1, 10)

    assert values["size"] == 0
    assert values["elements"] == []

    # Valores de un árbol con 3 nodos
    values = bst.values(three_bst, 1, 100)

    assert values["size"] == 3
    assert values["elements"][0] == 10
    assert values["elements"][1] == 50
    assert values["elements"][2] == 100

    # Valores de un árbol con 7 nodos
    values = bst.values(seven_bst, 1, 1000)

    assert values["size"] == 7
    assert values["elements"][0] == 100
    assert values["elements"][1] == 200
    assert values["elements"][2] == 300
    assert values["elements"][3] == 400
    assert values["elements"][4] == 500
    assert values["elements"][5] == 600
    assert values["elements"][6] == 700