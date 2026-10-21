## Group Anagrams leetcode problem
### (https://neetcode.io/problems/anagram-groups/question?list=neetcode150)

def group_anagrams( strs: list[str]) -> list[list[str]]:
    if len(strs) == 1:
        return [strs]
    grouped_anagram_list: list[list[str]] = []
    signature_mappings: dict[str, list[str]] = {}
    for str in strs:
        str_sorted = "".join(sorted(str))
        if str_sorted not in signature_mappings:
            signature_mappings[str_sorted] = []
        signature_mappings[str_sorted].append(str)
    for signature in signature_mappings:
        grouped_anagram_list.append(sorted(signature_mappings[signature]))
    return sorted(grouped_anagram_list)