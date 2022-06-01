# If you know how HashTable works then it should be an easy problem. I believe that as a Software Engineer, understanding how HashTable works is compulsory.

#     To build HashTable, we need buckets as a static array to store a list of pairs (key, value) which has the same bucket index:
#         The bucket index = hash_code(key) % BUCKET_SIZE
#         The larger BUCKET_SIZE is, the low chance collision happens.
#         To get a hash code of an integer value, we can use their value directly. But for other types like String, Object,... we need to write an efficient hash function to get the hash code that causes as low collision as possible.
#     For different keys but share the same bucket index, we can store pair of (key, value) as a list or Balanced BST:
#         If we store it as a list, in the worst case, it will cost O(N) for put, get, remove operations, where N is the number of keys in the same bucket. Here I choose to implement this way since it's easy to implement.
#         If we store it as a Balanced BST, in the worst case, it will cost O(logN) for put, get, remove operations, where N is the number of keys in the same bucket.

class MyHashMap:

    def __init__(self):
        self.bucket_size=1000
        self.buckets=[[] for _ in range(self.bucket_size)]
    def getBucket(self,key):
        return self.buckets[key%self.bucket_size]
    def findIndexOfKey(self,bucket,key):
        for i in range(len(bucket)):
            if bucket[i][0]==key:
                return i
        return -1
    def put(self, key: int, value: int) -> None:
        bucket=self.getBucket(key)
        nodeIndex=self.findIndexOfKey(bucket,key)
        if nodeIndex!=-1:
            bucket[nodeIndex][1]=value
        else:    
            bucket.append([key,value])
    def get(self, key: int) -> int:
        bucket=self.getBucket(key)
        nodeIndex=self.findIndexOfKey(bucket,key)
        if nodeIndex==-1:return -1
        return bucket[nodeIndex][1]
    def remove(self, key: int) -> None:
        bucket=self.getBucket(key)
        nodeIndex=self.findIndexOfKey(bucket,key)
        if nodeIndex==-1:return
        del bucket[nodeIndex]
# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

# Complexity:

#     Time:
#         init: O(BUCKET_SIZE), where BUCKET_SIZE is the size of buckets.
#         put, get, remove: O(1) in average, O(min(N, MAX_RANGE_VALUE/BUCKET_SIZE)) in the worst case.
#     Space:
#         O(BUCKET_SIZE + N), where N is number of elements that we have added into our HashTable.
