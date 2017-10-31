def list_to_dict(arr1, arr2):
    new_list = zip(arr1, arr2)
    new_dict = dict(new_list)
    print new_dict

list_to_dict(["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"],["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"])