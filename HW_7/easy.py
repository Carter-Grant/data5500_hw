#Easy: (3 points)

#Write a Python function to insert a value 
# into a binary search tree. The function 
# should take the root of the tree and the 
# value to be inserted as parameters.

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

def main():
    root = None
    while (user_input := input("Enter a value to insert into the tree (or 'exit' to stop): ")) != 'exit':
        try:
            root = tree_insert(root, int(user_input))
            print(f"Inserted {user_input} into the tree.")
        except ValueError:
            print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
#chatGPT use: Q: i need to have something at the end of my function that asks the user to input a value to be put into the tree. here is my code so far:
#A: You're off to a good start with your Tree class and the tree_insert function. To add user input functionality, you can include a loop at the end of your code that continuously asks the user for a value to insert into the tree. Here's how you can do it:
#q: is there a simpler way that uses less code to do the main function while keeping everything else the same?
#a: #def main():root = None while (user_input := input("Enter a value to insert into the tree (or 'exit' to stop): ")) != 'exit':try:root = tree_insert(root, int(user_input)) print(f"Inserted {user_input} into the tree.") except ValueError:print("Please enter a valid integer.")