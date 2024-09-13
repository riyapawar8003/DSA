# Java program to illustrate how to find the middle element
# by counting the number of nodes

class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

# Helper function to find length of linked list
def getLength(head):

    # Variable to store length
    length = 0

    # Traverse the entire linked list and increment length
    # by 1 for each node
    while head:
        length += 1
        head = head.next

    # Return the number of nodes in the linked list
    return length

# Function to find the middle element of the linked list
def getMiddle(head):

    # Finding length of the linked list
    length = getLength(head)

    # Traverse till we reach half of the length
    mid_index = length // 2
    while mid_index:
        head = head.next
        mid_index -= 1

    # Head now will be pointing to the middle element
    return head.data

def main():

    # Create a hard-coded linked list:
    # 10 -> 20 -> 30 -> 40 -> 50 -> 60
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)
    head.next.next.next = Node(40)
    head.next.next.next.next = Node(50)
    head.next.next.next.next.next = Node(60)

    print(getMiddle(head))

if __name__ == "__main__":
    main()