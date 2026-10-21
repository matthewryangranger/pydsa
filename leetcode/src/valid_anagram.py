## Valid Anagram leetcode problem
### (https://leetcode.com/problems/valid-anagram/description/)

def valid_anagram(s: str, t: str) -> bool:
    seen_map_s: dict[str, int] = {}
    seen_map_t: dict[str, int] = {}
    for char_c in s:
        seen_map_s[char_c] = seen_map_s.get(char_c, 0) + 1
    for char_c in t:
        seen_map_t[char_c] = seen_map_t.get(char_c, 0) + 1

    return seen_map_s == seen_map_t