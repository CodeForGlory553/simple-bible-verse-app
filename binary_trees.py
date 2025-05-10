import matplotlib.pyplot as plt
import matplotlib.patches as patches

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root):
        self.root = root  # Accepting a TreeNode directly

    def _get_node_depth(self, node):
        if node is None:
            return 0
        else:
            return 1 + max(self._get_node_depth(node.left), self._get_node_depth(node.right))

    def _get_positions(self, root):
        positions = {}
        depth = self._get_node_depth(root)

        def traverse(node, x, y, level):
            if node:
                positions[node.data] = (x, y)
                width = 2**(depth - level - 1)
                traverse(node.left, x - width, y - 1, level + 1)
                traverse(node.right, x + width, y - 1, level + 1)

        traverse(root, 0, 0, 0)
        return positions

    def _draw_node(self, ax, position, label):
        circle = patches.Circle(position, radius=0.15, facecolor='lightblue', edgecolor='black')
        ax.add_patch(circle)
        ax.text(position[0], position[1], label, ha='center', va='center', fontsize=10, fontweight='bold')

    def _draw_edge(self, ax, pos1, pos2):
        ax.plot([pos1[0], pos2[0]], [pos1[1], pos2[1]], 'k-', linewidth=1.5)  # Using lines instead of arrows for better clarity

    def visualize(self):
        if not self.root:
            return

        positions = self._get_positions(self.root)
        fig, ax = plt.subplots(figsize=(8, 6))  # Adjusting figure size for better readability

        for node_data, pos in positions.items():
            self._draw_node(ax, pos, node_data)

        for node_data, pos1 in positions.items():
            node = self.find_node(self.root, node_data)
            if node.left and node.left.data in positions:
                self._draw_edge(ax, pos1, positions[node.left.data])
            if node.right and node.right.data in positions:
                self._draw_edge(ax, pos1, positions[node.right.data])

        # Adjusting plot limits
        all_x = [p[0] for p in positions.values()]
        all_y = [p[1] for p in positions.values()]
        ax.set_xlim(min(all_x) - 1, max(all_x) + 1)
        ax.set_ylim(min(all_y) - 1, max(all_y) + 1)
        ax.invert_yaxis()  # Root at the top
        ax.axis('off')
        ax.set_title("Binary Tree Structure")
        plt.show()

    def find_node(self, current_node, data):
        if current_node is None:
            return None
        if current_node.data == data:
            return current_node
        left_search = self.find_node(current_node.left, data)
        if left_search:
            return left_search
        return self.find_node(current_node.right, data)

    def pre_order(self, node):
        if node:
            print(node.data, end=' ')
            self.pre_order(node.left)
            self.pre_order(node.right)

    def in_order(self, node):
        if node:
            self.in_order(node.left)
            print(node.data, end=' ')
            self.in_order(node.right)

    def post_order(self, node):
        if node:
            self.post_order(node.left)
            self.post_order(node.right)
            print(node.data, end=' ')

# Creating the binary tree
root = TreeNode('R')
node1 = TreeNode('A')
node2 = TreeNode('B')
node3 = TreeNode('C')
node4 = TreeNode('D')
node5 = TreeNode('E')

root.left = node1
root.right = node2

node1.left = node3
node1.right = node4

node2.left = node5

tree_operations = BinaryTree(root)

#print("Pre-order Traversal:")
#tree_operations.pre_order(root)
#print("\nIn-order Traversal:")
#tree_operations.in_order(root)
print("\nPost-order Traversal:")
tree_operations.post_order(root)

# Visualizing the tree
tree_operations.visualize()