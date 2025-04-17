def member(list1, list2):
    common = set(list1) & set(list2)
    if common:
        print("True")
        print("Matched Count:", len(common))
        return True
    else:
        print("False")
        print("Matched Count: 0")
        return False

L1 = [1, 4, 6, 3, 8, 10, 7]
L2 = [11, 12, 3, 15, 10, 7]
member(L1, L2)
