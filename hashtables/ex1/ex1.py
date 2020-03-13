#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    def makeTuple(x , y):
        return (x, y)
    if len(weights) == 1:
        return None
    for index, item in enumerate(weights):
        hash_table_insert(ht, item, index )
        if hash_table_retrieve(ht, limit - item) is not None:
            firstAnswer = index
            firstItem = item
            limit = limit - item
      
       
    for index, item in enumerate(weights):
        if limit - item == 0 and index != firstAnswer:
            # print(limit)
            secondAnswer = index
            secondItem = item
        
            # print(secondAnswer)
    if firstAnswer is not None and secondAnswer is not None:
        if firstAnswer < secondAnswer:
            answer = makeTuple(secondAnswer, firstAnswer)
            return answer
        else:
            answer = makeTuple(firstAnswer, secondAnswer)
            return answer
    else:
        return None

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
