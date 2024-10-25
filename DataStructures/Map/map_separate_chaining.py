from DataStructures.List import single_linked_list as lt
from DataStructures.List import array_list as al
from DataStructures.Map import map_entry as me
from DataStructures.Map import map_functions as mf
import random
import copy

def new_map(num_elements, load_factor, prime=109345121):
    lista = al.new_list()
    for i in range(mf.next_prime(num_elements/load_factor)):
        al.add_last(lista, lt.new_list())
    map = {"prime": prime,
           "capacity": mf.next_prime(num_elements/load_factor),
           "scale": random.randint(1, prime-1),
           "shift": random.randint(0, prime-1),
           "table": lista,
           "current_factor": 0,
           "limit_factor": load_factor,
           "size": 0,
           "type": "CHAINING"}
    return map

def size(my_map):
    size = my_map["size"]
    return size

def is_empty (my_map):
    if my_map["size"] == 0:
        return True
    else:
        return False

def put(map, key, value):
    
    hash = mf.hash_value(map, key)
    bucket = al.get_element(map['table'], hash)
    entry = me.new_map_entry(key, value)
    pos = lt.is_present(bucket, key, cmp_function)
    if pos >= 0:    # La pareja ya exista, se reemplaza el valor
        lt.change_info(bucket, pos, entry)
    else:
        lt.add_last(bucket, entry)   # La llave no existia
        map['size'] += 1
        map['currentfactor'] = map['size'] / map['capacity']

    if (map['current_factor'] >= map['limit_factor']):
        rehash(map)

    return map

def cmp_function(element1, element2):
    if element1 == element2["key"]:
        return 0
    return -1

def rehash(my_map):
    lista = my_map["table"]
    old_map = copy.deepcopy(my_map)
    for i in range(mf.next_prime(my_map["capacity"]*2)):
        al.add_last(lista, lt.new_list())
    my_map["capacity"]=mf.next_prime(my_map["capacity"]*2)
    lista_llaves = key_set(old_map)
    lista_values = value_set(old_map)
    my_map["table"] = lista
    for i in range(al.size(lista_llaves)):
        llave = al.get_element(lista_llaves,i)
        valor = al.get_element(lista_values,i)
        put(my_map,llave,valor)
    return my_map

def key_set (my_map):
    key_list = al.new_list()
    lista_grande = my_map["table"]
    for i in range(al.size(lista_grande)):
        lista_interna = al.get_element(lista_grande, i)
        if lt.is_empty(lista_interna) == False:
            for j in range(lt.size(lista_interna)):
                valor = lt.get_element(lista_interna, j)
                if valor["key"] != "__EMPTY__":
                    al.add_last(key_list, valor["key"])
    return key_list

def value_set (my_map):
    value_list = al.new_list()
    lista_grande = my_map["table"]
    for i in range(al.size(lista_grande)):
        lista_interna = al.get_element(lista_grande, i)
        if lt.size(lista_interna) != 0:
            for j in range(lt.size(lista_interna)):
                valor = lt.get_element(lista_interna, j)
                if valor["value"] != "__EMPTY__":
                    al.add_last(value_list, valor["value"])
    return value_list

def contains(map, key):
    lista = map["table"]
    presente = False
    indice = mf.hash_value(map, key)
    indice_dentro = 0
    if lt.size(al.get_element(lista,indice)) != 0:
        lista_pequena = al.get_element(lista,indice)
        while indice_dentro < lt.size(lista_pequena) and presente == False:
            valor = lt.get_element(lista_pequena, indice_dentro)
            if valor["key"] == key:
                presente = True
            else:
                indice_dentro += 1
    return presente

def get(map, key):
    hash = mf.hash_value(map, key)
    bucket = al.get_element(map['table'], hash)
    pos = lt.is_present(bucket, key, cmp_function)
    if pos >= 0:
        return lt.get_element(bucket, pos)["value"]
    else:
        return None
    
def remove(map, key):
    indice_dentro = 0
    acabar = False
    if contains(map, key) == True:
        indice = mf.hash_value(map, key)
        lista_pequena = al.get_element(map["table"],indice)
        while indice_dentro < lt.size(lista_pequena) and acabar == False:
            if lt.get_element(lista_pequena,indice_dentro)["key"] == key:
                lt.change_info(lista_pequena,indice_dentro, me.new_map_entry("__EMPTY__", "__EMPTY__"))
                acabar = True
            else:
                indice += 1
        map["size"] -= 1
    return map