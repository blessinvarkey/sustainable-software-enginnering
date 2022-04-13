# A program to implement a skip list.

# TODO: implement the `getNode` function, which is a prerequisite for __getitem__ and __setitem__
# TODO: implement the `length`

import random

class Node:
  """
  An item in the skip list holding the data itself and pointers to 
  the successors of the item at all levels.
  """
 
  def __init__(self, data, max_lvl):
    self.data = data
    self.successors = [None] * (max_lvl + 1)
    # By convention, the width is 0 if no successor is present.
    # Otherwise it specifies the deviation of the indices between 
    # this item and the succeeding item in a level.
    self.widths = [0] * (max_lvl + 1)

  def __str__(self):
    return f'Node(data={self.data}, \
successors={list(map(lambda n: n.data if n else None, self.successors))}, \
widths={self.widths})'

class SkipList:
  """
  A class modelling a skip list and providing common list operations.
  """
  
  def __init__(self, max_lvl, p):
    self.max_lvl = max_lvl
    self.head = None
    self.p = p

  def insert(self, data, index = None):
    """
    Insert a new element into the list.
    
    If index isn't specified, or the index exceeds the highest index 
    in the list, the item is inserted at the tail of the list.
    """
    if self.head == None:
      self.head = Node(data, self.max_lvl)
      return self.head
    else:
      n = Node(data, self.max_lvl)
      if index is not None and index < 1:
        # item will be inserted before current head
        n.successors = [self.head] * (self.max_lvl + 1)
        n.widths = [1] * (self.max_lvl + 1)
        self.head = n
      else:
        current = self.head
        # find the item in each level that will preceed the newly inserted item
        to_update = [[None, 0]] * (self.max_lvl + 1)
        i = 0
        for level in range(self.max_lvl, -1, -1):
          while current.successors[level] and \
                (index == None or current.widths[level] + i < index):
            i = i + current.widths[level]
            current = current.successors[level]
          to_update[level] = (current, i)

        # choose the max level in that a pointer to the new item should be added
        max_lvl = 0
        while random.random() < self.p and max_lvl < self.max_lvl:
          max_lvl = max_lvl + 1

        # insert the new item and update its predecessors 
        for level in range(self.max_lvl + 1):
          pred, pred_index = to_update[level]
          if level <= max_lvl:
            n.successors[level] = pred.successors[level]
            new_pred_width = i - pred_index + 1
            if pred.successors[level]:
              n.widths[level] = pred.widths[level] - new_pred_width + 1
            pred.widths[level] = new_pred_width
            pred.successors[level] = n
          else:
            pred.widths[level] = pred.widths[level] + 1
      return n

  def get_node(self, index):
    """
    Returns the node of this skip list at the given index or None if no 
    item exist for this index.
    """
    # TODO your code here
    return None

  def __getitem__(self, index):
    """Overwrites reading with the array operator `list[i]`."""
    n = self.get_node(index)
    if n:
      return n.data
    else:
      raise IndexError

  def __setitem__(self, index, value):
    """Overwrites writing with the array operator `list[i]`."""
    n = self.get_node(index)
    if n:
      n.data = value
    else:
      raise IndexError

  def __len__(self):
    """Return the amount of items in this list."""
    # TODO your code here
    return 0

  def __str__(self):
    result = ""
    if self.head:
      for i in range(self.max_lvl, -1, -1):
        str = f"lvl {i}: {self.head.data}"
        current = self.head
        while current.successors[i]:
          str += f"  -{current.widths[i]}>  {current.successors[i].data}"
          current = current.successors[i]
        if result != "":
          result += "\n"
        result += str
    return result

if __name__ == 'builtins' or __name__ == '__main__':
  l = SkipList(4, .5)
  l.insert(15)
  l.insert(4)
  l.insert(2)
  l.insert(5)
  l.insert(10)
  l.insert(11)
  l.insert(56)
  l.insert(200, 0)
  l.insert(400, 7)
  print("Skip List structure:")
  print(l)
