"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
    """Create a list containing the current and next two round numbers.

    Parameters:
        number (int): The current round number.

    Returns:
        list: The current round number and the two that follow.
    """

    return [number, number+1, number+2]


def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers.

    Parameters:
        rounds_1 (list): The first rounds played.
        rounds_2 (list): The second group of rounds played.

    Returns:
        list:  All rounds played.
    """

    return rounds_1 + rounds_2


def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number.

    Parameters:
        rounds (list): The rounds played.
        number (int): The round number.

    Returns:
        bool: Was the round played?
    """

    return number in rounds


def card_average(hand):
    """Calculate and returns the average card value from the list.

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        float: The average value of the cards in the hand.
    """
    sum = 0.0
    for i in range(len(hand)):
        sum += hand[i]
    avg = sum/len(hand)

    return (avg)


def approx_average_is_average(hand):
    """Return if the (average of first and last card values) OR ('middle' card) == calculated average.

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        bool: Does one of the approximate averages equal the `true average`?
    """
    # 1. Calculate the actual average of the whole hand
    actual_avg = sum(hand) / len(hand)
    
    # 2. Strategy 1: Average of the first and last card
    strat_1 = (hand[0] + hand[-1]) / 2
    
    # 3. Strategy 2: The middle card (median)
    strat_2 = hand[len(hand) // 2]
    
    # 4. Compare them! Return True if either one matches the actual average.
    return strat_1 == actual_avg or strat_2 == actual_avg


    


def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        bool: Are the even and odd averages equal?
    """

    avg_odds = 0
    sum_odds = 0
    avg_even = 0
    sum_even = 0
    count_odds = 0
    count_even = 0
    
    for i in range(len(hand)):
        # Even
        if i % 2 == 0:
            sum_even += hand[i]
            count_even+=1
        # Odds
        elif i % 2 != 0:
            sum_odds += hand[i]
            count_odds+=1

    avg_even = sum_even / count_even
    avg_odds = sum_odds / count_odds

    if avg_even == avg_odds:
        return True
    else:
        return False


def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        list: The hand with Jacks (if present) value doubled.
    """

    if hand[-1] == 11:
        hand[-1] = hand[-1]*2
    else:
        pass
    return hand
