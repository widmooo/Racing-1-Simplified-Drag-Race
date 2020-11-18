def drag_race(length, anna, bob):
    anna_time = (length / anna.speed) + anna.reaction_time 
    anna_time_i = int(anna_time) 
    bob_time = (length / bob.speed) + bob.reaction_time 
    bob_time_i = int(bob_time) 
    if anna_time_i > bob_time_i:
        print("Anna is the winner")
        print("Anna should win in " + str(anna_time_i) + " seconds")
    elif bob_time_i < anna_time_i:
        print("Bob is the winner")
        print("Bob should win in" + str(bob_time_i) + "seconds")
    elif bob_time_i == anna_time_i:
        print("It's a draw")