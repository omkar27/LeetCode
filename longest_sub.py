class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) > 1:
            first = strs[0]
            print(first)
            long_str = ""
            for j in range(1,len(strs)):
                for i in range(len(first)):
                    if strs[j].startswith(first[:i+1]):
                        long_str = first[:i+1]
                    else:
                        break
            for j in range(1,len(strs)):
                if strs[j].startswith(long_str):
                    long_str= long_str
                else:
                    long_str = ""
                    break
            return long_str
        elif(len(strs) == 1):
            return strs[0]
        else:
            return ""