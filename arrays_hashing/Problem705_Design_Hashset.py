'''
https://leetcode.com/problems/design-hashset/description/
Design a HashSet without using any built-in hash table libraries.
Implement MyHashSet class:
void add(key) Inserts the value key into the HashSet.
bool contains(key) Returns whether the value key exists in the HashSet or not.
void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.
'''


class ListNode:
    def __init__(self, key):
        self.key = key
        self.next = None


class MyHashSet(object):
    def __init__(self):
        self.set = [ListNode(0) for i in range(10 ** 4)]

    def add(self, key):
        cur = self.set[key % len(self.set)]
        while cur.next:
            if cur.next.key == key: return
            cur = cur.next

        cur.next = ListNode(key)

    def remove(self, key):
        cur = self.set[key % len(self.set)]
        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next

    def contains(self, key):
        cur = self.set[key % len(self.set)]
        while cur.next:
            if cur.next.key == key: return True
            cur = cur.next

        return False