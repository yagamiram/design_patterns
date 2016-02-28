'''
In python most of the data types are objects. [This is need more analysis. It's just my assumption here]
Example:
array_list = list() // creates an object for the class list. so array_list is an object

Most of the objects are iterable and few are non-iterable.

example:
The for loop iterates the object I created called array_list. 
for elem in array_list:
  print elem
  
How it iterates an object ?????? 
Ans: They follow iterator pattern.

The list, dict, set, tuple etc are called containers. And the containers are iterable in python. Just by the object of the container
we are able to iterate it to get the elements. 

okay enough lecture. how this is related to iterator pattern ? What is an iterator pattern ?
Accessing the elements of a class without knowing its internal representation.
The idea behind this pattern is to have an object which you can loop over without needing to know the internal representation of the data.

Now you can able to relate from what I mentioned before and from the iterator pattern definition.

First understand how FOR loop works:

When Python executes the for loop, it first invokes the __iter__() method of the container to get the iterator of the container. 
It then repeatedly calls the next() method (__next__() method in Python 3.x) of the iterator until the iterator raises a StopIteration exception. 
Once the exception is raised, the for loop ends.

Now understand what is "iterator" and "iterable" means :
Iterable - A container is said to be iterable if it has the __iter__ method defined.
Iterator - An iterator is an object that supports the iterator protocol which basically means that the following two methods need to be defined.
It has an __iter__ method defined which returns itself.
It has a next method defined (__next__ in Python 3.x) which returns the next value every time the next method is invoked on it.

Consider the below example:

Here Deck is container that stores all the cards in it. The class Deck has a member variable
called cards which is a list of card objects. Don't bother about the Card class implementation.

class Card(object):
    def __init__(self, rank, suit):
        FACE_CARD = {11: 'J', 12: 'Q', 13: 'K'}
        self.suit = suit
        self.rank = rank if rank <=10 else FACE_CARD[rank]
    def __str__(self):
        return "%s%s" % (self.rank, self.suit)
    
class Deck(object):
    def __init__(self):
        self.cards = []
        for s in ['S', 'D', 'C', 'H']:
            for r in range(1, 14):
                self.cards.append(Card(r, s))

Now to print all cards in the deck what you will do ?
>>> for c in Deck().cards: print c
...
1S
2S

Like above you will call the member variable cards from the object Deck(). But Deck is basically a container not the Card to access it
to get the card number and its rank. This is not a good way to write code. And one drawback of this is, you have to know
the internal representation of the Deck class and you accessing a member variable outside the class which is not a good sign.

So how to change this so that the Deck object becomes a itertor instead of using the member variable of its to iterate to get
the values?

We just need to add an __iter__ method to our class that returns an iterator.

class Deck(object):
    def __init__(self):
        self.cards = []
        for s in ['S', 'D', 'C', 'H']:
            for r in range(1, 14):
                self.cards.append(Card(r, s))
    def __iter__(self):
        return iter(self.cards)
        
>>> for c in Deck(): print c
...
1S
2S
#... snip ...#

This is the example of iterator pattern. Iterating the object to get the information without knowing the internal 
reoresentation of the object.

One another example of this pattern. Decode yourself to understand.

Links: 
http://ginstrom.com/scribbles/2007/10/08/design-patterns-python-style/
http://www.shutupandship.com/2012/01/understanding-python-iterables-and.html
'''
"""Implementation of the iterator pattern with a generator"""
def count_to(count):
    """Counts by word numbers, up to a maximum of five"""

    numbers = ["one", "two", "three", "four", "five"]
    # The zip keeps from counting over the limit
    for number, pos in zip(numbers, range(count)):
        yield number

# Test the generator
count_to_two = lambda : count_to(2)
count_to_five = lambda : count_to(5)

print "Counting to two…"
for number in count_to_two():
    print number,
print "\n"
print "Counting to five…"
for number in count_to_five():
    print number,
