import random
import pandas as pd
import matplotlib.pyplot as plt

#def parameters(N = 15, W = 25):

    #"""Generate parameters for a knapsack problem with penalties
       #for exceeding weight limit."""

N = 15 # number of items
W = 25 # maximum weight of knapsack
penalty_per_unit = 2 # penalty per unit weight over the limit

random.seed(4)

weights = [random.randint(1, 10) for _ in range(N)] #theoretical weights of items
values = [random.randint(1, 10) for _ in range(N)] #known values of items
    #return N, W, weights, values, penalty_per_unit

#parameters_data = parameters()

real_weights  = [w + random.randint( - min(weights) + 1 , + 5) for w in weights]  # actual weights of items

n_item = [i for i in range(N)]
weight_per_item = dict(zip(n_item, weights))
real_weight_per_item = dict(zip(n_item, real_weights))
value_per_item = dict(zip(n_item, values))

print("weights:", weights)
print("real_weights:", real_weights)
print("values:", values)

def should_accept(method, repair):

    """Decide whether to accept item i based on the chosen method and
       the repairing strategy to apply."""

    knapsack = []
    discarded = []

 # ACCEPTANCE HEURISTICS

    if method == "h_conservative":
       overflow = 0  # initializing overflow
       current_weight = 0 #initializing knapsack weight
       current_value  = 0 #initializing knapsack value

       for i in weight_per_item.keys():
           if current_weight + 10 <= W: # 10 = worst case scenario
              knapsack.append(i)
              current_weight += real_weight_per_item[i]
              overflow = current_weight - W
              while True:
                    if  overflow > 0:
                        current_value -= penalty_per_unit * overflow
                        break
                    elif overflow <= 0:
                        current_value += value_per_item[i]
                        break
           else:
                discarded.append(i)
    elif method == "h_max_capacity":
        overflow = 0
        current_weight = 0
        current_value  = 0
        max_cap_usage = 0.8 * W # I use only 80% of capacity to keep margin

        for i in weight_per_item.keys():
            if current_weight <= max_cap_usage:
               knapsack.append(i)
               current_weight += real_weight_per_item[i]
               overflow = current_weight - W
               while True:
                    if overflow > 0:
                        current_value -= penalty_per_unit * overflow
                        break
                    elif overflow <= 0:
                        current_value += value_per_item[i]
                        break
            else:
               discarded.append(i)


    elif method == "h_value":
        overflow = 0
        current_weight = 0
        current_value  = 0

        for i in weight_per_item.keys():
            if value_per_item[i] >= sum(values) / len(values) and current_weight + weight_per_item[i] <= W:

                knapsack.append(i)
                current_weight += real_weight_per_item[i]
                overflow = current_weight - W

                while True:
                    if overflow > 0:
                        current_value -= penalty_per_unit * overflow
                        break
                    elif overflow <= 0:
                        current_value += value_per_item[i]
                        break
            else:
                discarded.append(i)

    print('\nAcceptation heuristic:\n')
    print(f"Knapsack: {knapsack}")
    print(f"Discarded: {discarded}")
    print(f"Current weight: {current_weight}")
    print(f"Current value: {current_value}")
    print(f"Overflow = {current_weight - W}")


    # REPAIR HEURISTICS

    if current_weight > W:
       # repair strategy needed.

        if repair == 'r_greedy':

            # worst value/weight ratio gets out first!

            knapsack_sorted = sorted(
                knapsack,
                key=lambda i: value_per_item[i] / real_weight_per_item[i]
            )

            while current_weight > W and knapsack_sorted:
                item_to_remove = knapsack_sorted.pop(0)
                knapsack.remove(item_to_remove)
                current_weight -= real_weight_per_item[item_to_remove]

            print("Repair applied with r_greedy.")


        elif repair == "r_value":

            # Remove items with lowest value first

            knapsack_sorted = sorted(knapsack, key=lambda i: value_per_item[i])

            while current_weight > W and knapsack_sorted:
                item_to_remove = knapsack_sorted.pop(0)
                knapsack.remove(item_to_remove)
                current_weight -= real_weight_per_item[item_to_remove]


            print("Repair applied with r_value.")


        elif repair == "r_weight":

            # Remove heaviest items first

            knapsack_sorted = sorted(knapsack, key=lambda i:
                                     real_weight_per_item[i],
                                     reverse=True)

            while current_weight > W and knapsack_sorted:
                item_to_remove = knapsack_sorted.pop(0)
                knapsack.remove(item_to_remove)
                current_weight -= real_weight_per_item[item_to_remove]


            print("Repair applied with r_weight.")


        elif repair == "r_random":
            # Remove random items until within weight limit

            while current_weight > W and knapsack:
                item_to_remove = random.choice(knapsack)
                knapsack.remove(item_to_remove)
                current_weight -= real_weight_per_item[item_to_remove]


            print("Repair applied with r_random.")


        elif repair is None or repair == "none":
            # nessun repair, ma sei fuori peso
            print("Warning: knapsack exceeds weight limit and no repair is applied.")
        else:
            raise ValueError(f"Unknown repair strategy: {repair}")
    else:
        print("No repair needed, knapsack is within weight limit.")

    final_value = sum(value_per_item[i] for i in knapsack)
    # ======================
    # LOG FINALE
    # ======================

    print('\nRepair heuristic:\n')
    print(f"Knapsack: {knapsack}")
    print(f"Current weight: {current_weight}")
    print(f"Final value: {final_value}")
    print(f"Overflow = {current_weight - W}")




should_accept("h_value", "r_greedy")