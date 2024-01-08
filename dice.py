import random

def throw_dice(dice_maximum, number_of_dice):
    return [random.randrange(1,dice_maximum + 1) for x in range(number_of_dice)]

def get_successes(number_of_dice, difficulty = 6):
    dice_result = throw_dice(10, number_of_dice)
    print(dice_result)
    n_of_successes = len([x for x in dice_result if x >= difficulty])
    n_of_tens = len([x for x in dice_result if x == 10])
    n_of_botches = len([x for x in dice_result if x == 1])
    return n_of_successes - max(0, n_of_botches - n_of_tens)