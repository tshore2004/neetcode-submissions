class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        A = []
        for i, num in enumerate(numbers):
            A.append([num, i])

        A.sort()
        i, j = 0, len(numbers)-1
        while i<j:
            curr = A[i][0] + A[j][0]
            if curr == target:
                # print (A)
                # print (A[i][1] + 1)
                # print (A[j][1])
                return [A[i][1] + 1, A[j][1] + 1]
                # return [min(A[i][1], A[j][1]), max(A[i][1], A[j][1])]

                # print (curr)
            elif curr < target:
                i+=1
            else:
                j-=1

        return []