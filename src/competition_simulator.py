def getSortedRoundTotalScores(round: dict[str: dict[str:int]]) -> list[tuple[str, int]]:
    round_total_scores = []
    for name, scores in round.items():
        round_total_scores.append((name, sum(list(scores.values()))))

    return sorted(
        round_total_scores,
        key = lambda person_score: person_score[1],
        reverse = True
    )

def simulateCompetition(rounds: list[dict["theme":str,"score":dict[str:dict[str:int]]]]):
    results = {}
    total_rounds = len(rounds)

    for round_number in range(total_rounds):
        round = rounds[round_number]
        round_name = round['theme']
        round_scores = round['scores']

        sorted_round_total_scores = getSortedRoundTotalScores(round_scores)