class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
#--------------SINGLY LINKED LIST--------------------
""""class Linked_list:
    def __init__(self):
        self.head=None
    
    def show(self):
        node=self.head
        while(node != None):
            print(node.data)
            node=node.next

    def pop(self):
        if self.head==None:
            return -1
        elif self.head.next == None:
            temp=self.head
            self.head=None
        else:
            temp=self.head
            while temp.next != None:
                prev=temp
                temp=temp.next

            prev.next=None
        return temp

    def Append(self,data):
        if self.head==None:
            newNode=Node(data)
            self.head=newNode
        else:
            newNode=Node(data)
            temp=self.head
            while temp != None:
                prev=temp
                temp=temp.next
        
            prev.next=newNode

    def InsertAt(self,index,data):
        NewNode=Node(data)
        if index==0:


#Append Node

link1=Linked_list()
link1.Append('Vipul')  
link1.Append("sahil")
link1.Append("Vedant")
link1.Append("karan")
link1.show()

#Pop Node 
print("poped Node: ",link1.pop())
print("poped Node: ",link1.pop())
print("poped Node: ",link1.pop())
print("poped Node: ",link1.pop())
print("poped Node: ",link1.pop())
print("poped Node: ",link1.pop())
link1.show()

#Insert At Position
 

"""
#--------------CIRCULER SINGLY LINKED LIST------------------

class Circuler_list:
    def __init__(self):
        self.tail=None


    def show(self):
        node=self.tail.next
        print(node.data)
        node=node.next
        while(node != self.tail.next):
            print(node.data)
            node=node.next
    
    def Append(self,data):
        newNode=Node(data)
        if self.tail==None:
            newNode.next=newNode
            self.tail=newNode
        else:

            newNode.next=self.tail.next
            self.tail.next=newNode
            self.tail=self.tail.next
    
    def IsCycle(self):
        node =self.tail.next
        if node == None:
            return False
        else:
            list=[]
            while node:
                list.append(node)
                if node.next.next in list:
                    return True
                else:
                    node=node.next
        return False



"""    def pop(self):
        if self.head==None:
            return -1
        elif self.head.next == None:
            temp=self.head
            self.head=None
        else:
            temp=self.head
            while temp.next != None:
                prev=temp
                temp=temp.next

            prev.next=None
        return temp
"""


link1=Circuler_list()
link1.Append('Vipul')  
link1.Append("sahil")
link1.Append("Vedant")
link1.Append("karan")
link1.Append("Koli")
#link1.show()

#print(link1.IsCycle())

node1=Node("50")
node2=Node("55")


nodemon1=Node("45")
nodemon2=nodemon1

nodemon3=Node("55")

print(nodemon1)
print(nodemon2)
print(nodemon3)

print()

print(nodemon1.data == nodemon2.data)

