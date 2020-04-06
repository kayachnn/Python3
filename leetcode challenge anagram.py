class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_list = []
        for i in strs:
            sorted_list.append(''.join(sorted(i)))
        
        all_list = []
        for i in range(len(strs)):
            same_word_list = []
            for j in range(len(strs)):
                if(sorted_list[j] == sorted_list[i]):
                    same_word_list.append(strs[j])
            if(same_word_list not in all_list):
                all_list.append(same_word_list)
        return all_list
