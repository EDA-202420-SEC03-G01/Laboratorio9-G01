#from DataStructures.Utils import error as error


def new_list():
    #almacenar todos los datos, tamaño y demás (diccionario)
    lst = {
        "elements": [],
        "size": 0,
        "type": "ARRAY_LIST"
    }
    return lst

def get_element(lst,pos):
    return lst["elements"][pos]

def is_present(lst, element, cmp_function):
    size = lst["size"]
    if size>0:
        keyexist = False
        for keypos in range(0,size):
            info = lst["elements"][keypos]
            if (cmp_function(element, info) == 0):
                keyexist = True
                break
        if keyexist:
            return keypos
    return -1

def add_first(lst, elem):
    lst["elements"].insert(0,elem)
    lst["size"]+=1
    return lst

def add_last(lst,elem):
    lst["elements"].append(elem)
    lst["size"]+=1
    return lst

def size(lst):
    return lst["size"]

def is_empty(lst):
    if lst["size"] == 0:
        return True
    else:
        return False

def first_element(lst):
    return lst["elements"][0]

def last_element(lst):
    return lst["elements"][-1]

def remove_first(lst):
    del lst["elements"][0]
    lst["size"] -= 1
def remove_last(lst):

    if lst["size"] != 0:
        lst["elements"].pop(-1)
        lst["size"] -= 1
        
        return lst["elements"]
    
    else:
        
        return None

def delete_element(lst, pos):
    if lst["size"] != 0 and pos >= 0 and pos < lst["size"]:
        lst["elements"].pop(pos)
        lst["size"] -= 1
        return lst["elements"]

def insert_element(lst, element, pos):
    lst["elements"].insert(pos, element)
    lst["size"] += 1
    
    return lst
def change_info(lst, pos, new_info):
    lst["elements"][pos] = new_info
    return lst

def exchange(lst, pos1, pos2):
    info_pos1 = lst["elements"][pos1]
    info_pos2 = lst["elements"][pos2]
    lst["elements"][pos1] = info_pos2
    lst["elements"][pos2] = info_pos1
    return lst

def sub_list(lst, pos, numelem):
    lst_new = {
        "elements": [],
        "size": 0,
        "type": "ARRAY_LIST" #added 
    }
    
    for i_pos in range(pos,pos+numelem):
        lst_new["elements"].append(lst["elements"][i_pos])
        lst_new["size"]+=1
    
    return lst_new

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
    return lst

def shell_sort_original (my_list, sort_crit):
 
    #h = (shell_function(my_list))[1]
    
    if size(my_list) == 0 or size(my_list) == 1:
        
        return my_list
    
    else:
        
        h_list = (shell_function(my_list))
    
        for j in range(1, len(h_list) + 1):
            h = h_list[-j]
            i = 0
            pos = h
            print(h)

            while pos < size(my_list):
                #print(i)
                #print("+" + str(h))
                if sort_crit(get_element(my_list,i), get_element(my_list, pos)) == True:
                    #print(sort_crit(get_element(my_list,i), get_element(my_list, pos)))
                    exchange(my_list, i, pos)
                    
                if i >= h:
                    n = i
                    anterior_h = n-h
                    while anterior_h >= 0:
                        if sort_crit(get_element(my_list,anterior_h), get_element(my_list,n)) == True:
                            exchange(my_list, anterior_h, n)
                        n = anterior_h
                        anterior_h -= h
                        
                        
                
                if h == 1:
                    insertion_sort(my_list, sort_crit)
                    
                i += 1
                pos += 1
                
        return my_list

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