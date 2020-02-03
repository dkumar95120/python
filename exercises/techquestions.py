import sys
from time import time

class Stack:
    def __init__ (self):
        self.items = []

    def push (self, key):
        self.items.append(key)

    def pop (self):
        return self.items.pop()

    def isEmpty (self):
        return self.items == []

    def top (self):
        return self.items[-1]

def sorted_insert (S, key):
    if S.isEmpty() or key > S.top():
        S.push (key)
    else:
        temp = S.pop()
        sorted_insert(S, key)
        S.push(temp)

def sortStack(S):
    if not S.isEmpty():
        temp = S.pop()
        sortStack(S)
        sorted_insert(S, temp)

S = Stack()
S.push(-5)
S.push(30)
S.push(10)
S.push(2)
S.push(100)
S.push(-1)
print("Stack Sort")
print ("Before:", S.items)
sortStack(S)
print ("After :", S.items)

def anagram(s,t):
    # find if anagram of t exists in s
    res = True
    for chr in list(t):
        res = res and chr in list(s)
        if not res:
            break
    return res
print('============================')
s='udacity'
for t in ['ad','adx','adu','ads']:
    print('{:>5} anagram in {:>10}: {}'.format(t, s, anagram(s, t)))

###############################################################################

def is_palindrome (s):
    if len(s) == 1:
        return True
    mid = (len(s) + 1) // 2 
    i = 0
    while (i < mid) and (s[i] == s[-i-1]):
        i += 1

    return (i == mid)

def largest_palindrome(s):
    # find largest palindrome in s
    i=0
    while i < len(s) - 1:
        slen = len(s) - i
        i += 1
        for j in range(i):
            if is_palindrome(s[j:j+slen]):
                return s[j:j+slen]
    return None
print('============================')
print("      word  \tPalindrome")
for s in ['madamx', 'xdaoo', 'asxmaam', 'xmadam']:
    print('{:>10}\t{}'.format(s, largest_palindrome(s)))

###############################################################################

# O(n) solution to find LCS of two given values n1 and n2
 
# A binary tree node
class Node:
    # Constructor to create a new binary node
    def __init__(self, key):
        self.key =  key
        self.left = None
        self.right = None
 
# Finds the path from root node to given root of the tree.
# Stores the path in a list path[], returns true if path 
# exists otherwise false
# This function returns pointer to LCA of two given
# values n1 and n2
# This function assumes that n1 and n2 are present in
# Binary Tree
def findLCA(root, n1, n2):
     
    # Base Case
    if root is None:
        return None
 
    # If either n1 or n2 matches with root's key, report
    #  the presence by returning root (Note that if a key is
    #  ancestor of other, then the ancestor key becomes LCA
    if root.key == n1 or root.key == n2:
        return root 
 
    # Look for keys in left and right subtrees
    left_lca = findLCA(root.left, n1, n2) 
    right_lca = findLCA(root.right, n1, n2)
 
    # If both of the above calls return Non-NULL, then one key
    # is present in once subtree and other is present in other,
    # So this node is the LCA
    if left_lca and right_lca:
        return root 
 
    # Otherwise check if left subtree or right subtree is LCA
    return left_lca if left_lca else right_lca

def find_LCA (root, n1, n2):
    node = findLCA (root, n1, n2)   
    return node.key if node else None

# Driver program to test above function
# Let's create the Binary Tree shown in above diagram

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
print('============================')
print ("LCA(4, 5) = %d" %(find_LCA(root, 4, 5)))
print ("LCA(4, 6) = %d" %(find_LCA(root, 4, 6)))
print ("LCA(3, 4) = %d" %(find_LCA(root, 3, 4)))
print ("LCA(2, 4) = %d" %(find_LCA(root, 2, 4)))

###############################################################################

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList(object):
    def __init__(self, elem=None):
        self.head = elem

    def append (self, new_elem):
        elem = self.head
        if elem:
            prev = elem
            while elem:
                prev = elem
                elem = elem.next
            prev.next = new_elem
        else:
            self.head = new_elem

    def get_number (self):
        number = 0
        elem = self.head
        sign = -1 if elem.data < 0 else 1
        while elem:
            number = number*10 + abs(elem.data)
            elem = elem.next

        return number*sign

    def length(self):
        llen = 0
        elem = self.head
        while elem:
            llen += 1
            elem = elem.next
        return llen

    def item_from_top(self,pos):
        i = 1
        elem = self.head
        while elem and i < pos:
            i += 1
            elem = elem.next
        return elem.data if elem else None

    def item_from_end (self, npos):
        i = 0
        # start a patrolling pointer with a lead of npos elements
        patrol = self.head
        while (i < npos) and patrol:
            i += 1
            patrol = patrol.next
        # now the patrolling pointer is npos from top
        # start a new pointer from top (topptr)
        topptr = self.head
        # Now traverse through the list marching both pointers simultaneously
        # when patrolling pointer reaches bottom, the top pointer would be at npos from last!
        while patrol:
            topptr = topptr.next
            patrol = patrol.next
        return topptr.data
    
    def sort (self):
        sorted = False  # assume that the list is not sorted to begin with
        while not sorted:
            prev = None
            this = self.head
            next = this.next
            sorted = True # assuming that list is now sorted provide no further updates are needed
            while next:
                snext = next.next
                if next.data < this.data:
                    # swap their next pointers
                    if prev:
                        prev.next = next 
                    next.next = this
                    this.next = snext
                    if this == self.head:
                        self.head = next
                    # swap this pointer with next pointer
                    cur = this
                    this = next
                    next = cur
                    sorted = False # reset sorted flag since updates were needed
                else:
                    prev = this
                    this = next
                    next = snext 
               
    def reverse (self):
        #initialize this and next pointers
        this = self.head
        if not this: return self

        next = this.next
        # set next of head pointer to None for list termination
        this.next = None 
        while next:
            # save the next to next (second next) pointer for further marching
            snext = next.next
            # now set the next.next pointer to this pointer
            next.next = this
            # now march both this and next pointers using current next and snext pointers
            this = next
            next = snext            

        # make sure to reset head pointer to this pointer (last node from the original list)
        self.head = this
        return self


    def print(self):
        elem = self.head
        sys.stdout.write('Linked List: [')
        while elem.next:
            sys.stdout.write (str(elem.data)+',')
            elem = elem.next
        sys.stdout.write(str(elem.data)+']')
        sys.stdout.flush()
        print()

    def print_node(self, elem):
        if elem.next:
            self.print_node(elem.next)
        # print the node now that you have reached the end of the list
        if (elem == self.head):
            sys.stdout.write (str(elem.data))
        else:
            sys.stdout.write (str(elem.data)+',')

    def print_reverse_iterative(self):
        sys.stdout.write('Reverse print iterative Linked List: [')
        last_node = None
        while last_node != self.head.next:
            elem = self.head
            while elem.next != last_node:
                elem = elem.next
            sys.stdout.write (str(elem.data)+',')
            last_node = elem
        sys.stdout.write(str(self.head.data)+']')
        sys.stdout.flush()
        print()


    def print_reverse(self):
        elem = self.head
        sys.stdout.write('Reverse Print Linked List: [')
        self.print_node(elem)
        sys.stdout.write(']')
        sys.stdout.flush()
        print()

ll = LinkedList(Node(40))
ll.append(Node(30))
ll.append(Node(20))
ll.append(Node(10))
ll.append(Node(50))
ll.append(Node(60))
ll.append(Node(70))
print('============================')
ll.print()
print('Sorted')
ll.sort()
ll.print()
ll.print_reverse()
ll.print_reverse_iterative()

for loc in range(7):
    i = loc + 1
    print('item {} from top {}'.format(i, ll.item_from_top(i)))
    print('item {} from end {}'.format(i, ll.item_from_end(i)))
    print()

print("Reversed ")
ll.reverse().print()

###############################################################################

class Stack(object):
    def __init__(self):
        self.storage = []

    def push (self, elem):
        self.storage.append(elem)

    def pop (self):
        return self.storage.pop()

    def is_empty (self):
        return len(self.storage) == 0

    def top_element(self):
        return self.storage[-1]

    def sortedInsert(self, elem):
        if self.is_empty() or elem > self.top_element():
            self.push(elem)
        else:
            temp = self.pop()
            self.sortedInsert(elem)
            self.push(temp)

    def sort(self):
        if not self.is_empty():
            temp = self.pop()  
            self.sort()
            self.sortedInsert(temp);

    def print (self):
        print('Stack:',self.storage)

S = Stack()
S.push(10)
S.push(5)
S.push(20)
S.push(3)
S.push(15)
S.push(7)
S.push(6)
S.print()
S.sort()
print("Sorted",)
S.print()

def first_missing_number(s):
    # finds a missing number given a string with numbers from 1 to n
    #convert string to tokens with digits
    numstr = s.split()
    numbers = [int(num) for num in numstr]
    seqnum = sorted(numbers)
    missing = False
    for i, num in enumerate(seqnum):
        if i+1 != num:
            missing = True
            break
    return i+1 if missing else None
print('============================')

s = '10 9 5 4 7 6 3 1 2'
n = first_missing_number(s)
print ("in", s, "first missing number is", n)
print('============================')

def cash_units(cash):
    print("currency needed for ${}".format(cash))
    bills = [500,100, 50, 20, 10, 5, 1]
    for bill in bills:
        if cash >= bill:
            n = cash // bill
            print ('{:>3} ${:>3}'.format(n, bill))
            cash = cash % bill
        if not cash:
            break
cash_units(12345)
cash_units(1234)
cash_units(123)
cash_units(12)
cash_units(1)

def reverse_words(s):
    words = s.split()
    s=''
    for i in range(len(words),0,-1):
        s += words[i-1] + ' '

    return s

print('============================')
print(reverse_words('She is a nice girl'))

def currency_format(amount, sym='$'):
    t =''
    s=amount
    # first process fraction for cents
    try:
        d = s.index('.')
        num = float(s)
        cents=round((num - int(num)) * 100)
        t='.'+str(cents)
        s=s[:d]
    except:
        pass
    # now splice commas at every thousand place in whole numbers
    while len(s) > 3:
        t = ','+s[-3:] + t
        s = s[:-3]

    t = sym+s+t
    return t
print('============================')

print(currency_format('1234567.894'))

def divisors (n):
    # find all divisors of n besides itself
    factors = []

    if isinstance (n, int) and n > 4:
        for i in range(2, n//2 +1):
            if not n % i:
                factors.append(i)
    return factors

def subset_sum(numbers, target, partial=[]):
    s = sum(partial)

    # check if the partial sum is equals to target
    if s == target: 
        return True
        
    found = False
    for i in range(len(numbers)):
        n = numbers[i]
        remaining = numbers[i+1:]
        found = subset_sum(remaining, target, partial + [n]) 
        if found:
            break
    return found

candidates=[]
for i in range(4,101): # No factors for numbers less than 4
    factors = divisors(i)
    if sum(factors) > i:
        candidates.append(i)

print('Numbers where sum of divisors is greater than the number yet any subset sum is not equal to the number')
# now filter out ones where any comination of the sum of factors is not the number
print("Room# DivSum Divisors")
for num in candidates:
    factors = divisors(num)
    if not subset_sum(factors, num):
        print ('{:3}    {:3}   {}'.format(num, sum(factors), factors))

# find number of pairs of numbers in given sequence matching target difference 
def subset_dif(numbers, target, pivot=None):
    match = 0
    pairs = []
    if pivot:
        for num in numbers:
            if (num - pivot) == target:
                pairs.append([num, pivot])
                match += 1

        return match, pairs

    for i in range(len(numbers)):
        n = numbers[i]
        remaining = numbers[i+1:]
        nmatch, npairs = subset_dif(remaining, target, n)
        match += nmatch
        for  pair in npairs:
            pairs.append(pair)

    return match, pairs

print(subset_dif([1, 1, 5, 6, 9, 16, 27], 4)) # 3 (Due to 2x [1, 5], and [5, 9])
print(subset_dif([1, 1, 3, 3], 2)) # 4 (Due to 4x [1, 3])

def next_pal_num (n):
    if n < 9:
        return n+1
    pal = False
    while not pal:
        n += 1
        s = str(n)
        mid = len(s) // 2
        i = 0
        while (s[i] == s[-i-1]) and i < mid: 
            i += 1
        if i == mid:
            pal = True
    return n
print("===========\n  #  next_pal\n============")
for i in range(0,1000,50):
    print ('{:4}   {:4}'.format(i,next_pal_num(i)))


def non_primes (n):
    a=[0]*n
    for incr in range(2, n):
        if not a[incr]:
            for i in range(incr, n, incr):
                if (i > incr):
                    a[i] = 1
    return a

def prime(n):
    a = non_primes(n)
    p = []
    for i in range(2, n):
       if not a[i]:
          p.append(i)
    return p

n=1000
start_time=time()
p = prime(n)
print()
print("prime numbers till", n)
print("Total", p)
print(len(p))
print("time taken:{:10.4f}".format(time()-start_time))

from itertools import permutations
class jumble(object):
    def __init__(self, jumble_words):
        self.words = []
        self.jumble_words = jumble_words

    def permute(self, word):
        return [''.join(x) for x in permutations(word)]
def add (a, b):
    sum=[]
    for i in range(a):
        sum.append(i)
    for i in range(b):
        sum.append(i)

    return len(sum)
print (add(3,5))

### multiply two numbers given as a linked list
### for example: 1->2 * 1->0 = 120

l1 = LinkedList()
l1.append(Node(-1))
l1.append(Node(2))
l1.append(Node(3))

l2 = LinkedList()
l2.append(Node(-2))
l2.append(Node(0))

a = l1.get_number()
b = l2.get_number()
print()
print ('{}x{} = {}'.format(a,b, a*b))

class BNode (object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def has_digit (self, digit):
        node = None
        if self.data == digit:
            node = self
        else:
            if not node and self.left:
                node = self.left.has_digit(digit)
            if not node and self.right:
                node = self.right.has_digit(digit)
        return node


class BTree (object):
    def __init__(self, root):
        self.root = root

    def has_number (self, number):
        digits = list(str(number))
        elem = self.root
        i=0
        found = False
        #find first digit in the tree
        elem = elem.has_digit(int(digits[0]))
        if elem:
            found = True
            i = 1
        # now find remaining digits from the node with first digit
        while elem and i < len(digits) and found:
            if elem.left and (int(digits[i]) == elem.left.data):
                elem = elem.left
            elif elem.right and (int(digits[i]) == elem.right.data):
                elem = elem.right
            else:
                found = False
            i += 1
        return found


bn = BNode(3)
bt = BTree(bn)
bn.left = BNode(4)
bn.right = BNode(5)
bn.left.left = BNode(6)
bn.left.right = BNode(7)
bn.right.left = BNode(8)
bn.right.right = BNode(9)
print()
print('{:3} {}'.format('359', bt.has_number(359)))
print('{:3} {}'.format('38', bt.has_number(38)))
print('{:3} {}'.format('47', bt.has_number(47)))
print('{:3} {}'.format('6', bt.has_number(6)))

def grade(score, total):
    scale={}
    scale['A'] = 90
    scale['B'] = 80
    scale['C'] = 70
    scale['D'] = 60

    percent = round(score*100./total)

    if percent < 60:
        return 'F', percent

    for grade in sorted(scale.keys()):
        if scale[grade] <= percent:
            break

    return grade, percent
print()
print(grade(28,30))
print(grade(35,40))
print(grade(31,35))
print(grade(36,45))
print(grade(32,45))
print(grade(22,35))