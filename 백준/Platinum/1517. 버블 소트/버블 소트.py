from dataclasses import dataclass
import sys

input = sys.stdin.readline


@dataclass
class Node:
    st: int
    ed: int
    val: int = 1
    parent_node: "Node" = None
    left_node: "Node" = None
    right_node: "Node" = None


class SegmentTree:
    def __init__(self, st: int, ed: int) -> None:
        self.node = self.make_tree(Node(st=st, ed=ed))
    
    def make_tree(self, node: Node) -> None:
        if node.st == node.ed:
            return Node(st=node.st, ed=node.ed, parent_node=node)
        
        mid = (node.st+node.ed) // 2
        node.left_node = self.make_tree(Node(st=node.st, ed=mid, parent_node=node))
        node.right_node = self.make_tree(Node(st=mid+1, ed=node.ed, parent_node=node))

        node.val = node.left_node.val + node.right_node.val
        return node

    def query(self, st: int, ed: int, node: Node = None) -> int:
        if node is None:
            node = self.node
            
        if node.st > ed or node.ed < st:
            return 0

        if st <= node.st and node.ed <= ed:
            return node.val
        
        left_sum = self.query(st, ed, node.left_node) 
        right_sum = self.query(st, ed, node.right_node)

        return left_sum + right_sum 
    
    def update(self, val:int, node: Node = None) -> int:
        if node is None:
            node = self.node
            
        if not (node.st <= val <= node.ed):
            return
        else:
            node.val -= 1

        if node.left_node is not None:
            self.update(val, node.left_node)
        
        if node.right_node is not None:
            self.update(val, node.right_node)


n = int(input())
line = list(map(int, input().split()))

set_sorted_line = set(sorted(line))
num_mapper = {old: new for new, old in enumerate(set_sorted_line)}

line = [num_mapper[i] for i in line]

segment_tree = SegmentTree(st=0, ed=len(set_sorted_line)-1)

result = 0
for i in line:
    result += segment_tree.query(0, i-1)
    segment_tree.update(i)

print(result)