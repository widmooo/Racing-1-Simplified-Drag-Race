def drag_race(length, anna, bob):
    anna_time = (length / anna.speed) + anna.reaction_time
    bob_time = (length / bob.speed) + bob.reaction_time
    if anna_time < bob_time:
        return "Anna is the winner"
    elif bob_time < anna_time:
        return "Bob is the winner"
    elif bob_time == anna_time:
        return "It's a draw"
