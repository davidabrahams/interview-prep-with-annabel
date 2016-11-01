
class Tree(object):

    def __init__(self):
        self.x = None
        self.l = None
        self.r = None

def recurs_process(tree):
    """
    Recursively traverse the tree and assign each tree a minimum, and
    maximum field, where these are the min and max values found in that
    tree.

    O(N) time best and worst case
    """

    min_pos = [tree.x]
    max_pos = [tree.x]

    for t in [tree.l, tree.r]:
        if t is not None:
            recurs_process(t)
            min_pos.append(t.minimum)
            max_pos.append(t.maximum)

    tree.minimum = min(min_pos)
    tree.maximum = max(max_pos)

def tree_is_bst(tree):
    """
    >>> tree_is_bst(get_tree_from_tuple(1))
    True
    >>> tree_is_bst(get_tree_from_tuple((10, (5, 2, (7, 6, None)), 15)))
    True
    >>> tree_is_bst(get_tree_from_tuple((10, (5, 2, (7, 6, 5)), 15)))
    False
    >>> tree_is_bst(get_tree_from_tuple((10, (5, 2, (9, 7, 8)), 15)))
    False
    >>> tree_is_bst(get_tree_from_tuple((10, (5, 2, (9, 7, 16)), 15)))
    False
    
    """
    recurs_process(tree)
    is_bst = True
    if tree.l is not None:
        is_bst = is_bst and (tree.l.maximum < tree.x) and tree_is_bst(tree.l)
    if tree.r is not None:
        is_bst = is_bst and (tree.r.minimum > tree.x) and tree_is_bst(tree.r)

    return is_bst


def get_tree_from_tuple(tup):
    """
    Helper function to create a tree from a tuple. Tuples have three forms:
    
    1. (X, L, R) where X is a value (ie, 3) and L and R are both also tuple
    representations of a tree.

    2. i, where i is an integer. This is a tree with no children.

    3. None. This is an empty child.

    This function should work with the following inputs. These are all BSTs:

    >>> assert get_tree_from_tuple((2, 1, 3));
    >>> assert get_tree_from_tuple((2, None, 3));
    >>> assert get_tree_from_tuple((10, (5, 2, (7, 6, None)), 15));


    """
    if tup is None:
        return None
    else:
        t = Tree()
        if isinstance(tup, int):
            t.x = tup
        else:
            t.x = tup[0]
            t.l = get_tree_from_tuple(tup[1])
            t.r = get_tree_from_tuple(tup[2])
        return t

if __name__ == "__main__":
    import doctest
    doctest.testmod()