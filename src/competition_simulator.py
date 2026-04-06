def getSortedRoundTotalScores(round: dict[str: dict[str:int]]) -> list[tuple[str, int]]:
    round_total_scores = []
    for name, scores in round.items():
        round_total_scores.append((name, sum(list(scores.values()))))

    return sorted(
        round_total_scores,
        key = lambda person_score: person_score[1],
        reverse = True
    )

def showTable(headers: list[str], data: list[list], title: str, identation: int = 2):
    table_strings = [title]

    stringified_data = [
        [str(item) for item in line]
        for line in data
    ]

    # Get the lengths of all data + headers
    all_string_lengths = [
        len(string)
        for string in headers + sum(stringified_data, [])
    ]

    # Get the maximum used size on all columns
    column_size = max(all_string_lengths) + 1

    line_string = "-"*(column_size*len(headers))
    table_strings.append(line_string)

    headers_string = "".join(header.ljust(column_size) for header in headers)
    table_strings.append(headers_string)
    table_strings.append(line_string)


    for line in stringified_data:
        table_strings.append("".join([
            item.ljust(column_size)
            for item in line
        ]))
    table_strings.append(line_string)

    print("\n".join([" "*identation + string for string in table_strings]))
    print()

def showRoundResults(round_number, round_name, sorted_round_total_scores: list[tuple[str, int]]):
    winner_name, winner_score = sorted_round_total_scores[0]
    print(f"Ronda {round_number} - {round_name}:")
    showTable(["Cocinero", "Puntuacion"], sorted_round_total_scores, f"Ganador: {winner_name} ({winner_score} pts)")
    print()

def simulateCompetition(rounds: list[dict["theme":str,"score":dict[str:dict[str:int]]]]):
    results = {}
    total_rounds = len(rounds)

    for round_number in range(total_rounds):
        round = rounds[round_number]
        round_name = round['theme']
        round_scores = round['scores']

        sorted_round_total_scores = getSortedRoundTotalScores(round_scores)

        # Save round results
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

        winner_name = sorted_round_total_scores[0][0]
        results[winner_name]["rounds_winned"] += 1

        showRoundResults(round_number+1, round_name, sorted_round_total_scores)

    # Prepare results data to be printed
    results_table_data = sorted([
        [
            cook_name, 
            cook_results["total_score"],
            cook_results["rounds_winned"],
            cook_results["best_round"],
            cook_results["total_score"] / total_rounds 
        ] 
        for cook_name, cook_results in results.items()
    ], reverse=True, key=lambda row: row[1])

    showTable(
        ["Cocinero", "Puntaje", "Rondas ganadas", "Mejor ronda", "Promedio"],
        results_table_data,
        "Tabla de posiciones final:",
        0
    )