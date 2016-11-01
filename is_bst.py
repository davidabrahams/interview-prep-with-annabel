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
    return False


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
    return None

if __name__ == "__main__":
    import doctest
    doctest.testmod()