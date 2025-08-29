class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.height = 0

    def print_stack(self):
        if self.top == None:
            print('The stack is empty')
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def push(self, value):
        if isinstance(value, Node):
            new_node = value
        else:
            new_node = Node(value)
            
        new_node.next = self.top
        self.top = new_node
        self.height += 1
        return True
    
    def pop(self):
        if self.height == 0:
            return None
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.height -= 1
        return temp
    

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0        

    def print_queue(self):
        if self.first == None:
            print('The queue is empty')
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def enqueue(self,value):
        if isinstance(value, Node):
            new_node = value
        else:
            new_node = Node(value)
        
        new_node.next = None
        if self.length == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1
        return True
    
    def dequeue(self):
        if self.length == 0:
            return None
        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            temp.next = None
        self.length -= 1
        return temp
    

class StackQueueExchange:
    def __init__(self):
        self.stack = Stack()
        self.queue = Queue()

    def push_to_stack(self, value):
        #Push a value to the stack
        self.stack.push(value)
    
    def enqueue_to_queue(self, value):
        #Enqueue a value to the queue
        self.queue.enqueue(value)
        
    def pop_from_stack_to_queue(self):
        #Pop from stack and enqueue to queue
        if self.stack.height == 0:
            return None
        
        node = self.stack.pop()
        # When popped from stack, enqueue it to queue
        if node:
            self.queue.enqueue(node)
            return node
    
    def dequeue_from_queue_to_stack(self):
        #Dequeue from queue and push to stack
        if self.queue.length == 0:
            return None
        
        node = self.queue.dequeue()
        # When dequeued from queue, push it to stack
        if node:
            self.stack.push(node)
            return node
        
    def print_stack(self):
        self.stack.print_stack()
    
    def print_queue(self):
        self.queue.print_queue()
        

linkedsystem = StackQueueExchange()

linkedsystem.push_to_stack(10)
linkedsystem.push_to_stack(20)
linkedsystem.push_to_stack(30)

linkedsystem.enqueue_to_queue(15)
linkedsystem.enqueue_to_queue(25)
linkedsystem.enqueue_to_queue(35)

print('Stack Contents:')
linkedsystem.print_stack()

print('Queue Contents:')
linkedsystem.print_queue()

linkedsystem.dequeue_from_queue_to_stack()

print('Stack Contents:')
linkedsystem.print_stack()

print('Queue Contents:')
linkedsystem.print_queue()

linkedsystem.pop_from_stack_to_queue()

print('Stack Contents:')
linkedsystem.print_stack()

print('Queue Contents:')
linkedsystem.print_queue()







        






    


