# Topics : Array, Hash table, string
from typing import List
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        lowercase_letters = [chr(i) for i in range(ord('a'), ord('z') + 1)]
        result = []
        common_char_counts = {}
        for letter in words[0]:
            if letter in common_char_counts:
                common_char_counts[letter] += 1
            else:
                common_char_counts[letter] = 1
        for i in range(1, len(words)):
            current_char_counts = {}
            for letter in words[i]:
                if letter in current_char_counts:
                    current_char_counts[letter] += 1
                else:
                    current_char_counts[letter] = 1
            common_char = {}
            for key, value in common_char_counts.items():
                if key in current_char_counts.keys():
                    common_char[key] = min(common_char_counts[key],current_char_counts[key])
            common_char_counts = common_char
        for key, value in common_char_counts.items():
            for i in range(value):
                result.append(key)
        return result
def main():
    # Create a Solution object
    solution = Solution()

    # Define test cases
    words_list = [
        ["bella", "label", "roller"],
        ["cool", "lock", "cook"],
        ["hello", "world", "python"]
    ]

    # Iterate over each test case
    for words in words_list:
        print(f"Common characters in {words}: {solution.commonChars(words)}")

if __name__ == "__main__":
    main()