from LCS import Solution


def is_subsequence(candidate: str, text: str) -> bool:
    """Return True when every candidate character occurs in order in text."""
    characters = iter(text)
    return all(character in characters for character in candidate)


def main() -> None:
    test_cases = [
        ("abcde", "ace", 3),
        ("abc", "abc", 3),
        ("abc", "def", 0),
        ("AGGTAB", "GXTXAYB", 4),
        ("ezupkr", "ubmrapg", 2),
    ]

    solution = Solution()
    for case_number, (text1, text2, expected_length) in enumerate(test_cases, start=1):
        subsequence = solution.longestCommonSubsequence(text1, text2)

        assert isinstance(subsequence, str), "The solution must return a string"
        assert is_subsequence(subsequence, text1), "Result is not a subsequence of text1"
        assert is_subsequence(subsequence, text2), "Result is not a subsequence of text2"
        assert len(subsequence) == expected_length, (
            f"Expected length {expected_length}, got {len(subsequence)}"
        )
        print(f"Test case {case_number}: {text1!r}, {text2!r}")
        print(f"LCS length: {expected_length}")
        print(f"Longest common subsequence: {subsequence or '(empty)'}")
        print()


if __name__ == "__main__":
    main()
