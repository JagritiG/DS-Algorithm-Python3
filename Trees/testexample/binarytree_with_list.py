# Lists as tree representation
def binary_tree(r):
    """constructs a list with a root node and two empty sublists for the children."""
    return [r, [], []]


# Insert a new list (left child) into the second position of the root list
# If it has something in second position, push it down the tree as the
# left child we are adding.
def insert_left(root, new_branch):

    # Obtain the (possibly empty) list corresponds to the current left child
    t = root.pop(1)

    # Add the new left child, installing the old left child
    # as the left child of the new one
    if len(t) > 1:
        root.insert(1, [new_branch, t, []])
    else:
        root.insert(1, [new_branch, [], []])

    return root


# Insert right child
def insert_right(root, new_branch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [new_branch, [], t])
    else:
        root.insert(2, [new_branch, [], []])

    return root


# Functions for getting and setting the root value,
# as well as getting the left or right subtrees.
def get_root_value(root):
    return root[0]


def set_root_value(root, new_value):
    root[0] = new_value


def get_left_child(root):
    return root[1]


def get_right_child(root):
    return root[2]


# Driver code
# Construct a tree with root value 5
r = binary_tree(5)
print(r)
print(get_root_value(r))

# Insert left child
insert_left(r, 10)
insert_left(r, 11)
print(r)
print(get_root_value(r))
print(get_left_child(r))

# Insert right child
insert_right(r, 22)
print(r)
print(get_root_value(r))
print(get_right_child(r))

# Set root value
set_root_value(get_left_child(r), 34)
print(r)
insert_left(r, 22)
print(r)
print(get_root_value(r))
print(get_left_child(r))
