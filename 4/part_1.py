def score_line(line: str) -> int:
    """Get the score of a single line"""
    numbers = line.split(":")[-1].strip("\n")
    winners = set(numbers.split("|")[0].split())
    drawn = set(numbers.split("|")[-1].split())
    drawn_winners = len(winners.intersection(drawn))
    if drawn_winners == 0:
        return 0
    else:
        return 2 ** (drawn_winners - 1)


if __name__ == '__main__':

    score = 0
    with open("input.txt", "r") as f:
        for line in f.readlines():
            score += score_line(line)

    print(f"The pile of scratch cards is worth {score}!")

