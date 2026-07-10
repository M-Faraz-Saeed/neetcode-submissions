class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        main_list = []
        groups = []
        
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word not in main_list:
                main_list.append(sorted_word)
                groups.append([word])
            else:
                index = main_list.index(sorted_word)
                groups[index].append(word)
        return groups

        