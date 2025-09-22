# --------------------------- linkedlist ---------------------------
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    # class attributes
    data = None
    next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.l = 0
    
    def append(self, data):
        new_node = Node(data)

        # if this is the first entry
        if not self.head:
            self.head = new_node
            return new_node
        
        # otherwise, traverse to the end of the linkedlist
        # and add
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        self.l += 1
    
    def pop(self):
        current = self.head

        # if the list has length 1
        if current.next == None:
            self.head = None
            return current.data
        
        # otherwise, traverse to the end of the ll
        while current.next.next:
            current = current.next
        rv = current.next.data
        current.next = None
        return rv
        
    
    # class attributes
    head = None
    l = 0

# --------------------------- Test Cases ---------------------------
import unittest

class TestLinkedList(unittest.TestCase):
    
    def setUp(self):
        """Set up a fresh LinkedList instance for each test."""
        self.ll = LinkedList()
    
    def test_empty_list_initialization(self):
        """Test that a new LinkedList is properly initialized."""
        self.assertIsNone(self.ll.head)
    
    def test_append_to_empty_list(self):
        """Test appending to an empty list."""
        node = self.ll.append(5)
        self.assertEqual(self.ll.head.data, 5)
        self.assertIsNone(self.ll.head.next)
        self.assertEqual(node.data, 5)
    
    def test_append_multiple_elements(self):
        """Test appending multiple elements to the list."""
        self.ll.append(1)
        self.ll.append(2)
        self.ll.append(3)
        
        # Check head
        self.assertEqual(self.ll.head.data, 1)
        
        # Check second node
        second = self.ll.head.next
        self.assertEqual(second.data, 2)
        
        # Check third node
        third = second.next
        self.assertEqual(third.data, 3)
        self.assertIsNone(third.next)
    
    def test_append_different_data_types(self):
        """Test appending different data types."""
        self.ll.append("hello")
        self.ll.append(42)
        self.ll.append([1, 2, 3])
        self.ll.append(None)
        
        self.assertEqual(self.ll.head.data, "hello")
        self.assertEqual(self.ll.head.next.data, 42)
        self.assertEqual(self.ll.head.next.next.data, [1, 2, 3])
        self.assertIsNone(self.ll.head.next.next.next.data)
    
    def test_pop_from_empty_list(self):
        """Test popping from an empty list."""
        with self.assertRaises(AttributeError):
            self.ll.pop()
    
    def test_pop_from_single_element_list(self):
        """Test popping from a list with one element."""
        self.ll.append(42)
        result = self.ll.pop()
        
        self.assertEqual(result, 42)
        self.assertIsNone(self.ll.head)
    
    def test_pop_from_multiple_elements(self):
        """Test popping from a list with multiple elements."""
        self.ll.append(1)
        self.ll.append(2)
        self.ll.append(3)
        
        # Pop the last element
        result = self.ll.pop()
        self.assertEqual(result, 3)
        
        # Check that the list now has 2 elements
        self.assertEqual(self.ll.head.data, 1)
        self.assertEqual(self.ll.head.next.data, 2)
        self.assertIsNone(self.ll.head.next.next)
        
        # Pop again
        result = self.ll.pop()
        self.assertEqual(result, 2)
        
        # Check that the list now has 1 element
        self.assertEqual(self.ll.head.data, 1)
        self.assertIsNone(self.ll.head.next)
    
    def test_pop_all_elements(self):
        """Test popping all elements from the list."""
        self.ll.append(1)
        self.ll.append(2)
        self.ll.append(3)
        
        # Pop all elements
        self.assertEqual(self.ll.pop(), 3)
        self.assertEqual(self.ll.pop(), 2)
        self.assertEqual(self.ll.pop(), 1)
        
        # List should be empty now
        self.assertIsNone(self.ll.head)
    
    def test_append_after_pop(self):
        """Test appending after popping elements."""
        self.ll.append(1)
        self.ll.append(2)
        self.ll.pop()  # Remove 2
        
        self.ll.append(3)
        
        # Check the final state
        self.assertEqual(self.ll.head.data, 1)
        self.assertEqual(self.ll.head.next.data, 3)
        self.assertIsNone(self.ll.head.next.next)
    
    def test_large_list_operations(self):
        """Test operations on a larger list."""
        # Add 100 elements
        for i in range(100):
            self.ll.append(i)
        
        # Verify first and last elements
        self.assertEqual(self.ll.head.data, 0)
        current = self.ll.head
        for i in range(99):
            current = current.next
        self.assertEqual(current.data, 99)
        
        # Pop the last element
        result = self.ll.pop()
        self.assertEqual(result, 99)
    
    def test_node_creation(self):
        """Test Node class creation and attributes."""
        node = Node(42)
        self.assertEqual(node.data, 42)
        self.assertIsNone(node.next)
    
    def test_node_linking(self):
        """Test that nodes can be properly linked."""
        node1 = Node(1)
        node2 = Node(2)
        node1.next = node2
        
        self.assertEqual(node1.data, 1)
        self.assertEqual(node1.next.data, 2)
        self.assertIsNone(node2.next)

def run_tests():
    """Run all tests and display results."""
    unittest.main(verbosity=2)

if __name__ == "__main__":
    run_tests()
