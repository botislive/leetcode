class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        temp=[]
        for i, n in enumerate(arr1):
            if n not in arr2:
                temp.append(n)
        
        result=[]
        for n1 in arr2:
            for n2 in arr1:
                if n1==n2:
                    result.append(n2)
        return result+sorted(temp)


        