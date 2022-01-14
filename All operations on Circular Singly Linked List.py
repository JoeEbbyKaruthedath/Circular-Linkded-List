# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 20:57:01 2022

@author: joeeb
"""


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
         
    def __iter__(self):
        node = self.head
        while node:
            yield node
            if node.next == self.head:
                break
            node = node.next
            
    #creation of circular singly linked list
    def createCSLL(self, nodeValue):
        node = Node(nodeValue)
        node.next = node
        self.head = node
        self.tail = node
        
    def insertCSLL(self, value, location):
        if self.head is None:
            return "The head reference is None"
        else:
            newNode = Node(value)
            if location == 0:
                newNode.next = self.head
                self.head = newNode
                self.tail.next = newNode
            elif location == 1:
                newNode.next = self.tail.next
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index+=1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
                
    def traverseCSLL(self):
        if self.head == None:
            print("The CSLL does not exist")
        else:
            node = self.head
            while node:
                print(node.value)
                node = node.next
                if node.next == self.head:
                    break #You have reached the end of the Circular Singly Linked List
                
    def searchCSLL(self, target):
        if self.head == None:
            print("The CSLl does not exist")
        else:
            node = self.head
            while node:
                if node.value == target:
                    print("The value is found")
                    break
                elif node.next == self.head: #Searching if we have reached the end of the CSLL
                    print("The target does not exist")
                    break
                node = node.next
    def deleteNode(self, location):
        if self.head == None:
            print("The node does not exist")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.tail.next = self.head
            elif location == 1:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else :
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = self.head
                    self.tail = node 
            else : 
                tempNode = self.head
                index = 0
                while index < location -1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next
                
    def TotalDeleteCSLL(self):
        if self.head == None:
            print("The CSLL does not exist")
        else:
            self.head = None #
            self.tail.next = None
            self.tail = None
             



#Initializing the Circular Singly Linked List	    
circularSLL = CircularSinglyLinkedList()

#Inserting the values to CSLL
circularSLL.createCSLL(1)
circularSLL.insertCSLL(0, 0)
circularSLL.insertCSLL(2, 1)
circularSLL.insertCSLL(3, 1)
circularSLL.insertCSLL(45, 2)
circularSLL.insertCSLL(99, 1)

#Traversing the CSLL
circularSLL.traverseCSLL()

#Searching the CSLL
circularSLL.searchCSLL(45)

#Deleting some elements of the CSLL
circularSLL.deleteNode(0)
circularSLL.deleteNode(1)
circularSLL.deleteNode(2)

#Deleting the enitre CSLL
circularSLL.TotalDeleteCSLL()

print([node.value for node in circularSLL])                
