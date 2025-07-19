class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        result=[folder[0]]

        for f in (folder[1:]):
            if not f.startswith(result[-1]+"/"):
                result.append(f)
        
        return result

        