class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linked:
    def __init__(self):
        self.head=None
    def show(self):
        node=self.head
        while node is not None:
            print(node.data)
            node=node.next
link=linked()
n1=Node("salamma")
link.head=n1
n2=Node("Ilari")
n1.next=n2
link.show()
#n1.next=n2
