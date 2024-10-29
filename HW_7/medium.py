#Medium: (5 points)

#2. Implement a Python function to search 
# for a value in a binary search tree. 
# The method should take the root of the tree 
# and the value to be searched as parameters. 
# It should return True if the value is found in the tree, 
# and False otherwise.

class Tree:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None

def tree_insert(root, key):
    if root is None:
        return Tree(key)
    if key < root.key:
        root.left = tree_insert(root.left, key)
    else:
        root.right = tree_insert(root.right, key)
    return root

def tree_search(root, key):
    if root is None:
        return False  # Base case: key not found
    if key == root.key:
        return True  # Key found
    elif key < root.key:
        return tree_search(root.left, key)  # Search left subtree
    else:
        return tree_search(root.right, key)
    
def main():
    root = None
    # Build the tree by inserting some predefined values
    values_ex = [3, 1, 4, 1, 5, 9, 2, 6]  # Example values
    for value in values_ex:
        root = tree_insert(root, value)

    while True:
        search_input = input("Enter a value to search for in the tree (or 'exit' to stop searching): ")
        if search_input.lower() == 'exit':
            break
        try:
            value = int(search_input)
            search = tree_search(root, value)
            if search:
                print("True")
            else:
                print("False")
        except ValueError:
            print("Not an integer.")

if __name__ == "__main__":
    main()

#ChatGPT Questions: 
#Q: i need to change my main function to search for a value instead of insert one. How would I do this? 
#A: o modify your main function to search for a value instead of inserting one into the binary search tree, you can adjust the flow to first build the tree with some values and then allow the user to search for specific values.
