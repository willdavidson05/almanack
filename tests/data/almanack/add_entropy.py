# add_entropy.py

def add_entropy():
    def add_entropy_to_file(file_path, lines_of_code):
        """
        Adds lines of code to the specified file.

        Args:
            file_path: Path to the .md file.
            lines_of_code: List of lines of code to add.
        """
        with open(file_path, "w") as f:
            for i in lines_of_code:
                f.write(i + "\n")

    # Define the lines of code for each file
    high_entropy_code = """
        "## Section One: Numbers and Letters",
        "In a galaxy far, far away, 83742 starships assembled. The quantum flux at 9.81m/s² was **astounding**!",
        "- Item 1: @x&8lKj$1#d7",
        "- Item 2: zP9Q6v^5wT!rC",
        "- Item 3: 4837-19xy#A!z",
        "## Section Two: Random Sentences",
        "Lorem ipsum dolor sit amet, 42 nebulas in the cosmic sea. Quisque finibus, $100 billion, at ipsum tristique:",
        "1. `function(x) { return x * 42; }`",
        "2. The quick brown fox jumps over 13 lazy dogs.",
        "3. Supercalifragilisticexpialidocious - a word with magic.",
        "### Subsection: Mixed Content",
        "```python",
        "def entropy(data):",
        "    from collections import Counter",
        "    import math",
        "    count = Counter(data)",
        "    length = len(data)",
        "    return -sum(frequency / length * math.log(frequency / length, 2) for frequency in count.values())",
        "",
        'print(entropy("Random Data 1234!"))',
        "```",
    """
    low_entropy_code = """
        "## Simple List",
        "- Item 1",
        "- Item 2",
        "- Item 3",
        "- Item 4",
        "- Item 5",
    """

    # Dictionary of entropy levels for each file
    entropy_levels = {
        "high_entropy/high_entropy.md": high_entropy_code,
        "low_entropy/low_entropy.md": low_entropy_code,
    }

    # Add entropy to each file
    for file_path, lines_of_code in entropy_levels.items():
        add_entropy_to_file(file_path, lines_of_code)

if __name__ == "__main__":
    add_entropy()
