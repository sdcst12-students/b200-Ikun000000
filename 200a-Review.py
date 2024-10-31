def getIntegers(myList):
    # Extract integers from the input list or tuple
    integers = [x for x in myList if isinstance(x, int)]
    return integers

def getFactor(myList, number):
    # Extract numbers from myList that are factors of 'number'
    factors = [x for x in myList if isinstance(x, int) and number % x == 0]
    return factors

def getNegatives(myList):
    # Extract negative numbers from the input list or tuple
    negatives = [x for x in myList if isinstance(x, (int, float)) and x < 0]
    return negatives

def getIntersection(list1, list2):
    # Find the intersection of list1 and list2, sort, and return it as a list
    common = sorted(set(list1).intersection(list2))
    return common

def getUnion(list1, list2):
    # Find the union of list1 and list2, remove duplicates, sort, and return it as a list
    union = sorted(set(list1).union(list2))
    return union   

def getMerge(list1, list2):
    # Convert list1 to a list if it’s a tuple
    result = list(list1) if isinstance(list1, tuple) else list(list1)
    # Iterate over elements in list2
    for element in list2:
        if element in result:
            index = result.index(element)
            result.insert(index + 1, element)
        else:
            result.append(element)
    return tuple(result) if isinstance(list1, tuple) else result

# Test cases
def main():
    easy1 = [5, 10, 15, 2, 4, 6, 8]
    easy2 = [-2, -4, -6, 2, 4, 6, 0.1]
    numbers1 = [3, 5, 8, 12, 11, 19, 10, 7, 2, 15, 25, 34, 16, 32, 50, 60, 100, -3, 0.25]
    numbers2 = [3, 7, 11, 15, 19, 23, 27, 31, 35, 39, 44, 50]
    try:
        assert getIntegers([3, 4, 1.2, 1.3, 5]) == [3, 4, 5]
        assert getFactor(range(10), 12) == [1, 2, 3, 4, 6]
        assert getNegatives([-3, -1, 0, 1, 4]) == [-3, -1]
        assert getUnion(easy1, easy2) == [-6, -4, -2, 0.1, 2, 4, 5, 6, 8, 10, 15]
        assert getIntersection(easy1, easy2) == [2, 4, 6]
        assert getMerge(easy1, easy2) == [5, 10, 15, 2, 2, 4, 4, 6, 6, 8, -2, -4, -6, 0.1]
        print("All assertions passed")
    except AssertionError:
        print("At least 1 assertion failed")

if __name__ == "__main__":
    main()

