class Solution:

    def decrypt(self, n, arr1, arr2):

        arr3 = []
        for i in range(len(arr1)):
            arr3.append(bin(arr1[i] | arr2[i]))

        result = []

        for r in arr3:
            r = r.replace("1","#", n).replace("0", " ", n)
            result.append(r[2:])

        print(result)

p = Solution()

p.decrypt(5, [9,20,28,18,11], [30,1,21,17,28])
p.decrypt(6, [46,33,33,22,31,50], [27,56,19,14,14,10])