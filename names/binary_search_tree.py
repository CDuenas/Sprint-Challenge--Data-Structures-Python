class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # take the current value of our node (self.value)
        # compare to the new value we want to insert
        # IF self.left is already taken by a node
        # make that (left) node, call insert
        # set the left to the new node with the new value
        if value < self.value:
            if self.left == None:
                self.left = BSTNode(value)

            else:
                self.left.insert(value)

        # if new value >= self.value
            # IF self.right is already taken by a node
                # make that (right) node call insert
            # set the right child to the new node with new value
        else:
            if self.right == None:
                self.right = BSTNode(value)

            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        # compare the target to current value
        # if current value < target
        found = False
        if self.value >= target:
            # check the left subtree (self.left.contains(target))
            # if you cannot go left, return False
            if self.left is None:
                return False
            found = self.left.contains(target)

        # if current value >= target
        if self.value < target:
            # check if right subtree contains target
            # if you cannot go right, return False
            if self.right is None:
                return False
            found = self.right.contains(target)

        return found

    # Return the maximum value found in the tree

    def get_max(self):
        # the largest value will always be to the right of the current node
        # if we can go right, lets find the largest number there by calling get_max on the right subtree
        # if we cannot go right, return the current value
        if not self.right:
            return self.value
        return self.right.get_max()

    # Call the function `fn` on the value of each node

    def for_each(self, fn):
        # call function on the current value fn(self.value)
        # if you can go left, call for_each on the left tree
        # if you can go right, call for_each on the right tree
        fn(self.value)
        if self.left:
            self.left.for_each(fn)

        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if self.left:
            self.left.in_order_print(self.left)

        print(node.value)

        if self.right:
            self.right.in_order_print(self.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node=None):
        # create a queue for nodes
        Que = []
        # add the first node to the queue
        Que.append(self)
        # while queue is not empty
        while len(Que) > 0:
            # remove the first node from the queue
            # print the removed node
            # add all children into the queue
            current = Que.pop(0)
            print(current.value)

            if current.left:
                Que.append(current.left)

            if current.right:
                Que.append(current.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node=None):
        # create a stack for nodes
        stack = []
        # add the first node to the stack
        stack.append(self)
        # while the stack is not empty
        while len(stack) > 0:
            # get the current node from the top of the stack
            # print that node
            # add all children to the stack
            current = stack.pop(len(stack)-1)
            print(current.value)
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
