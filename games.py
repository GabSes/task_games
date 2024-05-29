def read_data_from_file(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
    return lines

def process_data(lines):
    # Get the number of participants
    num_participants = int(lines[0].strip())
    
    if num_participants < 5 or num_participants > 20:
        print("Invalid number of participants")
        return None

    category_scores = [0] * 10
    valid_games = False  # Flag to check if there are valid games

    for line in lines[1:]:
        data = list(map(int, line.strip().split()))
        category = data[0]
        scores = data[1:]

        # Check if the category is valid
        if category < 1 or category > 10:
            print(f"Non-existent game category: {category}")
            continue

        # Check if the number of scores is correct
        if len(scores) != 5:
            print(f"Incorrect number of scores for category {category}")
            continue
        
        valid_games = True
        category_scores[category - 1] += sum(scores)

    if not valid_games:
        print("No valid games")
        return None

    return category_scores

def print_results(category_scores):
    if category_scores is None:
        return

    max_score = -1
    min_score = float('inf')
    max_categories = []
    min_categories = []

    # Determine the categories with most and least points
    for i, score in enumerate(category_scores):
        if score > 0:
            if score > max_score:
                max_score = score
                max_categories = [i + 1]
            elif score == max_score:
                max_categories.append(i + 1)

            if score < min_score:
                min_score = score
                min_categories = [i + 1]
            elif score == min_score:
                min_categories.append(i + 1)
        
        print(f"{i + 1} {score}")

    # Print the categories with most and least points
    if max_categories and min_categories:
        print(f"Categories with most points: {', '.join(map(str, max_categories))} ({max_score} points)")
        print(f"Categories with least points: {', '.join(map(str, min_categories))} ({min_score} points)")

if __name__ == "__main__":
    file_name = 'data.txt'
    data = read_data_from_file(file_name)
    category_scores = process_data(data)
    print_results(category_scores)


