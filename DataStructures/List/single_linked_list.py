#import pytest
#from DataStructures.Utils import error as error

from DataStructures.List import list_node as node



def first_element (lst):
    if lst["first"] != None:
        return lst["first"]["info"]

def new_list ():
    newlist = {'first': None,
     'last': None,
     'size': 0}
    return newlist
    
def add_first (lst, elem):
    nodo = node.new_single_node(elem)
    nodo['next'] = lst['first']
    if lst['first'] is None:
        lst['first'] = nodo
        lst['last'] = nodo
    else:
        lst["first"] = nodo 
    lst["size"] += 1
    return lst    

def add_last (lst, elem):
    nodo = node.new_single_node(elem)
    if lst['first'] is None:
        lst['first'] = nodo
    else:
        lst["last"]["next"] = nodo
    lst["last"] = nodo
    lst["size"] += 1
    return lst

def is_empty(lst):
    if lst['size'] == 0:
        return True
    else:
        return False
    
def get_element(lst,pos):
    if lst['size'] == 0 or lst['size'] < pos:
        return -1
    else:
        n = 0
        nodo_actual = lst['first']
        while n < pos:
            nodo_actual = nodo_actual['next']
            n+=1
        return nodo_actual['info']

def size(lst):
    size = lst["size"]
    return size

def last_element (lst):
    if lst["size"] != 0:
        last = lst["last"]['info']
        return last
    else:
        return -1
    
def is_present (lst, elem, cmp_function):
    acabar = False
    act = lst["first"]
    pos = 0
    if lst["size"] == 0:
        return -1
    else:
        while acabar == False and act != None:
            if cmp_function(elem, act["info"]) == 0:
                acabar = True
            else:
                pos += 1
                act = act["next"]
        if acabar == True:
            return pos
        else:
            return -1

def change_info (lst, pos, new_info):
    act = lst["first"]
    contador = 0
    while contador < pos:
        act = act["next"]
        contador += 1
    act["info"] = new_info
    return lst

def insert_element (lst, elem, pos):
    if pos == 0:
        add_first(lst, elem)   
        return lst
    elif pos == lst["size"]:
        add_last(lst,elem)
        return lst
    else:
        nodo = node.new_single_node(elem)
        act = lst["first"]
        contador = 0
        ant = act
        while contador < pos:
            act = act["next"]
            contador += 1
            if contador + 1 == pos:
                ant = act
        ant["next"] = nodo
        nodo["next"] = act
    lst["size"] += 1
    return lst

def exchange(lst, pos1, pos2):
    elemento_pos1 = get_element(lst,pos1)
    elemento_pos2 = get_element(lst,pos2)
    change_info(lst,pos1,elemento_pos2)
    change_info(lst,pos2,elemento_pos1)
    return lst

def sub_list(lst, pos, num_elem):
    sublist = new_list()
    n = 0
    nodo_actual = lst['first']
    while n < pos:
        nodo_actual = nodo_actual['next']
        n+=1
    i = 0
    while i < num_elem: #número de elementos contandolo
        add_last(sublist,nodo_actual['info'])
        nodo_actual = nodo_actual['next']
        i+=1
    return sublist

def delete_element (lst, pos):
    if lst["size"] != 0:
        if pos != 0 and pos != (lst["size"] - 1):
            nodo_act = lst["first"]
            n = 0
            while n < pos-1:
                nodo_sig = nodo_act["next"]
                nodo_act = nodo_sig
                n += 1
            nodo_act["next"] = nodo_act["next"]["next"]
            lst["size"] -= 1
        elif pos == 0:
            remove_first(lst,pos)
        elif pos == (lst["size"] - 1):
            remove_last(lst)
            return lst
        
def remove_first (lst):
    if lst["size"] != 0:
        lst["first"] = lst["first"]["next"]
        lst["size"] -= 1
        return lst["first"]["info"]
    else:
        return None

def remove_last (lst):
    if lst["size"] != 0:
        pos_penultimo_nodo = ((lst["size"]) - 2)
        n = 0
        nodo_actual= lst["first"]
        while n < pos_penultimo_nodo:
            nodo_actual = nodo_actual['next']
            n+=1
        nodo_eliminado = nodo_actual["next"]
        nodo_actual["next"] = None
        lst["last"] = nodo_actual
        lst["size"] -= 1        
        return nodo_eliminado

def merge(lst, aux_lst, sort_crit, lo, m, hi):
    for k in range(lo, hi+1):
        change_info(aux_lst,k,get_element(lst,k))
    i = lo
    j = m+1
    for k in range(lo,hi+1):
        if(i > m):
            change_info(lst,k,get_element(aux_lst,j))           
            j += 1                            
        elif(j > hi):
            change_info(lst,k,get_element(aux_lst,i))              
            i += 1                          
        elif sort_crit(get_element(aux_lst,i),get_element(aux_lst,j)) or get_element(aux_lst,i) == get_element(aux_lst,j):    
            change_info(lst,k,get_element(aux_lst,i)) 
            i += 1
        else:
            change_info(lst,k,get_element(aux_lst,j)) 
            j += 1

def recursive_merge_sort(lst, aux_lst, lo, hi, sort_crit):
    if lo < hi:
        m = (hi+lo)//2
        recursive_merge_sort(lst, aux_lst, lo, m, sort_crit)
        recursive_merge_sort(lst, aux_lst, m+1, hi, sort_crit)
        merge(lst, aux_lst, sort_crit, lo, m, hi)

def merge_sort(lst, sort_crit):
    
    size_lst = size(lst)
    if size_lst > 1:
        aux_lst = sub_list(lst,0,size_lst)
        recursive_merge_sort(lst, aux_lst, 0, size_lst-1, sort_crit)
    
    return lst
    
def partition(lst, sort_crit, low, high):
    pivot = get_element(lst, high)
    i = low-1
    for pos in range(low, high):
        element = get_element(lst, pos)
        if sort_crit(element,pivot):
            i += 1
            exchange(lst,pos, i)
    exchange(lst,i+1,high)
    return i+1

def recursive_quick_sort(lst, sort_crit, low, high):
    # Paso 1. aplicar la función partition y obtener la posición del pivot
    # Paso 2. ordenamiento recursivo del rango [lo, pivot-1]
    # Paso 3. ordenamiento recursivo del rango [pivot+1, hi]
    if low < high:
        pivot_pos = partition(lst, sort_crit, low, high)
        recursive_quick_sort(lst, sort_crit, low, pivot_pos-1)
        recursive_quick_sort(lst, sort_crit, pivot_pos+1, high)
    return lst

def quick_sort(lst,sort_crit):
    recursive_quick_sort(lst, sort_crit, 0, size(lst)-1)
    return lst

def insertion_sort (lst, sorting_criteria):
    if size(lst) < 2:
        return lst
    else:
        for i in range(1, size(lst)):
            j = i
            while j > 0 and sorting_criteria(get_element(lst, j), get_element(lst, j-1)) == True:
                exchange(lst, j, j-1)
                j -= 1
    return lst

def selection_sort(lst, sorting_criteria):
    
    if size(lst) < 2:
        return lst
    else:
        for i in range(0, size(lst)):
            min = i
            for j in range(i, size(lst)):
                if sorting_criteria(get_element(lst, j), get_element(lst, min)) == True:
                    min = j
            if get_element(lst, i) != get_element(lst, min):
                exchange(lst, i, min)
    
    return lst, 

def shell_sort (my_list, sort_crit):
 
    #h = (shell_function(my_list))[1]
    h_list = (shell_function(my_list))
    ho = 0
    
    if size(my_list) == 0 or size(my_list) == 1:
        
        return my_list
    
    else:
    
        for j in range(1, len(h_list) - 1):
            h = h_list[-j]
            for i in range(0, size(my_list) - 1):
                
                if sort_crit(get_element(my_list,i-1), get_element(my_list, h+ho-1)) == True:
                    exchange(my_list, i-1, h+ho-1)
                    
                if i >= h:
                    if sort_crit(get_element(my_list,i-h-1), get_element(my_list,i-1)):
                        exchange(my_list, i-h-1, i-1)
                
                if h == 1:
                    insertion_sort(my_list, sort_crit)
                
                ho += 1
        return my_list

def shell_function (my_list):
    
    h = 0
    hi = 0
    h_values = []
    
    while h < ((size(my_list))//3):
        h = 3*hi + 1
        hi += 1
        h_values.append(h)
    
    return h_values

def shell_function (my_list):
    
    h = 0
    h_values = []
    
    while h < ((size(my_list))//3):
        h = 3*h + 1
        h_values.append(h)
    
    return h_values

def shell_sort (my_list, sort_crit):
 
    #h = (shell_function(my_list))[1]
    
    if size(my_list) == 0 or size(my_list) == 1:
        
        return my_list
    
    else:
        
        h_list = (shell_function(my_list))
        
    
        for j in range(1, len(h_list) + 1):
            h = h_list[-j]
            i = h
            print(h)

            while i < size(my_list):
            
                #print(i)
                #print("+" + str(h))
                #if sort_crit(get_element(my_list,i), get_element(my_list, pos)) == True:
                    #print(sort_crit(get_element(my_list,i), get_element(my_list, pos)))
                    #exchange(my_list, i, pos)
                    
                if i >= h:
                    n = i
                    anterior_h = n-h
                    while (anterior_h >= 0) and sort_crit(get_element(my_list,n), get_element(my_list,anterior_h)) == True:
                        exchange(my_list, anterior_h, n)
                        n = anterior_h
                        anterior_h -= h
                        
                        
                
                #if h == 1:
                    #insertion_sort(my_list, sort_crit)
            
                i += 1
                #pos += 1
            
        return my_list