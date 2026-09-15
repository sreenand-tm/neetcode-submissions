class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = {}

        for i in range(len(strs)):
            alpha = ''.join(sorted(strs[i]))

            if alpha not in output:
                output[alpha] = []

            output[alpha].append(strs[i])

        return list(output.values())