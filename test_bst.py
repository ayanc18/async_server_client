import pickle
import collections
import json

from bst import BST
bin_tree = BST()
with open('bst_server.pkl', 'rb') as fp:
    bin_tree = pickle.load(fp)
print("From server:")
print("inorder")
print(bin_tree.inorder_traversal())
print("preorder")
print(bin_tree.preorder_traversal())
print("postorder")
print(bin_tree.postorder_traversal())

bin2_tree = BST()
f = open('bst_client.json', "r")
node_list = json.load(f)
for node in node_list:
    bin2_tree.insert(node['value_received'],node['client_id'])
#bst inorder from the client tree
print("From client")
print("Inorder")
print(bin2_tree.inorder_traversal())
print("preorder")
print(bin2_tree.preorder_traversal())
print("postorder")
print(bin2_tree.postorder_traversal())
f.close()

flag1, flag2, flag3 = False, False, False
compare = lambda x, y: collections.Counter(x) == collections.Counter(y)

if compare(bin_tree.inorder_traversal(),bin2_tree.inorder_traversal()):
    flag1 = True
if compare(bin_tree.preorder_traversal(),bin2_tree.preorder_traversal()):
    flag2 = True
if compare(bin_tree.postorder_traversal(),bin2_tree.postorder_traversal()):
    flag3 = True
if flag1 and flag2 and flag3:
    print("BSTs are identical")
else:
    print("not similar")

del bin_tree
del bin2_tree



