def getSortedRoundTotalScores(round: dict[str: dict[str:int]]) -> list[tuple[str, int]]:
    round_total_scores = []
    for name, scores in round.items():
        round_total_scores.append((name, sum(list(scores.values()))))

    return sorted(
        round_total_scores,
        key = lambda person_score: person_score[1],
        reverse = True
    )

def showRoundResults(round_number, round_name, winner_name, winner_score):
    print(f"Ronda {round_number} - {round_name}:")
    print(f"  Ganador: {winner_name} ({winner_score} pts)")
    print("  ... (tabla de posiciones)")
    print()

def simulateCompetition(rounds: list[dict["theme":str,"score":dict[str:dict[str:int]]]]):
    results = {}
    total_rounds = len(rounds)

    for round_number in range(total_rounds):
        round = rounds[round_number]
        round_name = round['theme']
        round_scores = round['scores']

        sorted_round_total_scores = getSortedRoundTotalScores(round_scores)

        for name, score in sorted_round_total_scores:
            if not name in results:
                results[name] = {
                    "total_score": score,
                    "rounds_winned": 0,
                    "best_round": score,
                }
            else:
                results[name]["total_score"] += score
                if score > results[name]["best_round"]:
                    results[name]["best_round"] = score

        winner_name, winner_score = sorted_round_total_scores[0]
        results[winner_name]["rounds_winned"] += 1

        showRoundResults(round_number+1, round_name, winner_name, winner_score)