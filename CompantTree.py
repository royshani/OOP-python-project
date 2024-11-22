from Company import Company
from CompanyNode import CompanyNode
class CompanyTree():
    def __init__(self, root=None):
        if (isinstance(root, CompanyNode) or isinstance(root, None)) and root.get_parent() is None:
            self.root = root
        else:
            raise ValueError("amigo, lets say your root is not the brownest root in the forest")

    def set_root(self, root):
        if (isinstance(root, CompanyNode) or isinstance(root, None)):
            self.root = root
            return True
        else:
            return False

    def get_root(self):
        return self.root

    def parent_is_right(self, node):
        if node.get_parent() == self.root:
            return True
        if self.parent_is_right(node.get_parent()):
            return True
        else:
            return False


    def __str__(self): # fill
        node = self.root
        queue = []
        queue.append(node)
        queue.append('\n')
        tree_str = ""
        while len(queue) != 0:
            if not isinstance(queue[0], CompanyNode):
                tree_str += queue[0]
                queue.remove(queue[0])
            if len(queue) != 0:
                if isinstance(queue[0], CompanyNode):
                    if not queue[0].is_leaf():
                        for i in queue[0].get_children():
                            queue.append(i)
                            if i is queue[0].get_children()[-1]:
                                if self.parent_is_right(i):
                                    queue.append('\n')
                            if i is not queue[0].get_children()[-1]:
                                queue.append(" * ")
                        tree_str += queue[0].__str__()
                        queue.remove(queue[0])
                    else:
                        tree_str += queue[0].__str__()
                        queue.remove(queue[0])
        new_tree = tree_str[0:len(tree_str) - 1]
        return new_tree

    def order_tree(self, node, post_order_tree=[]):
        if node.is_leaf():
            post_order_tree.append(node)
            return
        for i in range(len(node.get_children())):
            CompanyTree.order_tree(self, node.get_children()[i], post_order_tree)
            if i == (round(len(node.get_children())) / 2) - 1 or len(node.get_children()) == 1:
                post_order_tree.append(node)
        return post_order_tree


    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        post_order_tree = []
        self.order_tree(self.root, post_order_tree)
        if self.n == len(post_order_tree):
            raise StopIteration
        else:
            self.n += 1
            return post_order_tree[self.n - 1]


    def insert_node(self, node):
        post_order_tree = []
        self.order_tree(self.root, post_order_tree)
        if isinstance(node, CompanyNode):
            if node.get_parent() is None and node.test_node_order_validity() and not self.root.is_ancestor(node):
                for i in post_order_tree:
                    if i.add_child(node):
                        return True
                return False
        else:
            return False
        return self

    def remove_node(self, name):
        post_order_tree = []
        self.order_tree(self.root, post_order_tree)
        for j in post_order_tree:
            if j.name == name:
                node = j
                if node not in post_order_tree:
                    return None
                for i in node.get_children():
                    node.get_parent().add_child(i)
                for child in node.get_children():
                    node.get_children().remove(child)
                node.get_parent().get_children().remove(node)

                return node