class UnionFind(object):
    def __init__(self, groups):
        self.groups = groups
        self.robots = set()
        for group in self.groups:
            self.robots.update(group.split('-'))
        self.root = {}
        self.root_len = {}
        for robot in self.robots:
            self.root_len[robot] = 1
            self.root[robot] = robot
        self.create_tree()

    def find_root(self, robot):
        if self.root[robot] == robot:
            return robot
        else:
            return self.find_root(self.root[robot])

    def union(self, root1, root2):
        len_union1 = self.root_len[root1]
        len_union2 = self.root_len[root2]
        if root1 <= root2:
            root, root_orig = root2, root1
        else:
            root, root_orig = root1, root2

        self.root[root_orig] = root
        self.root_len.pop(root_orig)
        self.root_len[root] = len_union1 + len_union2
        for robot in self.robots:
            if self.root[robot] == root_orig:
                self.root[robot] = root


    def create_tree(self):
        for group in self.groups:
            robot1, robot2 = group.split('-')
            root1 = self.find_root(robot1)
            root2 = self.find_root(robot2)
            if root1 != root2:
                self.union(root1, root2)

    def check(self, robot1, robot2):
        return self.root[robot1] == self.root[robot2]


def check_connection(network, first, second):
    union_find = UnionFind(network )
    return union_find.check(first, second)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "scout2", "scout3") == True, "Scout Brotherhood"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "super", "scout2") == True, "Super Scout"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "dr101", "sscout") == False, "I don't know any scouts."
