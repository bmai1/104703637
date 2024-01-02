class Node:
    # comments for style50 ocd
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action


class StackFrontier:
    # comments for style50 ocd
    def __init__(self):
        self.frontier = []

    # comments for style50 ocd
    def add(self, node):
        self.frontier.append(node)

    # comments for style50 ocd
    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    # comments for style50 ocd
    def empty(self):
        return len(self.frontier) == 0

    # comments for style50 ocd
    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node


class QueueFrontier(StackFrontier):
    # comments for style50 ocd
    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node
