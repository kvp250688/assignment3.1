
# coding: utf-8

# In[38]:


#Write a Python Program(with class concepts) to find the area of the triangle using the below formula.area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
#Function to take the length of the sides of triangle from user should be defined in the parentclass and function to calculate the area should be defined in subclass.

class Polygon:

    def __init__(self, n):
        self.number_of_sides = n

    def print_num_sides(self):
        '''a quick, informational print statement'''
        print('There are ' + str(self.number_of_sides) + 'sides.')

class Triangle(Polygon):

    def __init__(self, lengths_of_sides):
        Polygon.__init__(self, 3)
        self.lengths_of_sides = lengths_of_sides  # list of three numbers
    def get_area(self):
        '''return the area of the triangle using the semi-perimeter method'''
        a, b, c = self.lengths_of_sides
        s = (a + b + c) / 2
        return (s*(s-a)*(s-b)*(s-c)) ** 0.5
tri = Triangle([3, 4, 5])
print(tri.get_area())


# In[33]:


#Write a function filter_long_words() that takes a list of words and an integer n and returns the list of words that are longer than n.
def listing(guess, number):

    new_list = []

    for i in range(len(guess)):
        if len(guess[i]) > number:
            new_list.append(guess[i])

    print (new_list)

list1 = input("take input: ")

list = list1.split(",")

def main():
    global list, integer1
    integer = input()
    integer1 = int(integer)
    listing(list, integer1)

main()


# In[34]:


#Write a Python program using function concept that maps list of words into a list of integers representing the lengths of the corresponding words.

def map_to_lengths_for(words):
    lengths = []
    for word in words:
        lengths.append(len(word))
    return lengths


def map_to_lengths_map(words):
    return map(len, words)


def map_to_lengths_lists(words):
    return [len(word) for word in words]


if __name__ == "__main__":
    words = ['ab', 'try', 'test']
    print(map_to_lengths_for(words))
    print(map_to_lengths_map(words))
    print(map_to_lengths_lists(words))


# In[36]:


#Write a Python function which takes a character (i.e. a string of length 1) and returns True if it is a vowel, False otherwise.

def is_vowel(char):
    vowels = ('a', 'e', 'i', 'o', 'u')
    if char not in vowels:
        return False
    return True


if __name__ == "__main__":
    print(is_vowel(1))
    print (is_vowel('a'))
    print (is_vowel('b'))

