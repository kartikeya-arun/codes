class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self""" 
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
        Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
        Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'
    def intersect(self,object1):
        newSet=intSet()
        if len(self.vals)>len(object1.vals):
            for i in self.vals:
                if i in self.vals and i in object1.vals:
                    newSet.insert(i)
                        
        else:
            for i in object1.vals:
                if i in self.vals and i in object1.vals:
                    newSet.insert(i)
        return newSet.__str__()
    
    def __len__(self):
         return len(self.vals)
###############################################################################
#-------------------------------TESTING---------------------------------------#
###############################################################################
set1=intSet()
set2=intSet()
set1.insert(7)
set1.insert(3)
set1.insert(3)
set1.insert(6)
set1.insert(5)
set2.insert(5)
set2.insert(9)
set2.insert(12)
set2.insert(3)
set1.intersect(set2)
set3=intSet()
set4=intSet()
set3.insert(1)
set3.insert(0)
set3.insert(2)
set4.insert(3)
set4.insert(4)
set4.insert(5)
set3.intersect(set4)
