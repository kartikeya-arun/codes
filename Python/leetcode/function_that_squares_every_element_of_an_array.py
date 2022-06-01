class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        #make a new array
        #use map() function to map a lambda(anonymous) function to every element of an iterable.
        #use list() function to get list from a map object.
        #use sorted() function to sort the resulting array.
        result=sorted(list(map(lambda x:x**2,nums)))
        return result