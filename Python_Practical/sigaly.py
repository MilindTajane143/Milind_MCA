def__init__(slef,data)
       self.data=data  
    
    self.next=None

    def__init__(self)
    self.head=None

    def is_empty(self):
        return self.head is none
    def append(self,data):
        new_code=Node(data)
        if self.is_empty():
            self.head=new_node
            else:
                current=self.head
                while current.next
                current=current.next
                current.next=new _node

           def prepend(self,data)
           new_node=node(data)
           new_node.next=self.head
           self.head=new_node

           def display(self):
               if self.is_empty():
                   print("list is empty")
                   return
                current=self.head
                while current:
                    print("current.next
                          print("None")
                          def delete(self,key):
                              if self.is_empty():
                                  print("list is empty.nothing to delete")
                                  retrun
                                  if self.head.data==key:
                                      self.head=self.head.next
                                      return
                                    current=self.head
                                    previos=none
                                    while current and current.data!=key:
                                        previous=current
                                        current=current.next
                                        if current is none:
                                            print(f"Node with data{Key} not found")
                                            return
                                        previous.next=current.next
                                        sll=singlyLinkedList()
                                        sll.append(1)
                                        sll.append(2)
                                        sll.append(3)
                                        sll.append(0)

                                        print("Initial list:")
                                        s||.display()
                                        
                                        sll.display(2)
                                        print("After deleting node with value 2:")
                                        sll.display()

                                        
                                        
                                        
