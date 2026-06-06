**Problem Description**



**Context**

This project models a knapsack problem with stochastic item weights in a logistics-inspired setting. The scenario assumes that a courier must decide whether to accept or reject a set of packages. For each package, the declared weight and the value are known in advance. However, the real weight is uncertain and is revealed only when the courier collects the package. This creates a decision-making problem under uncertainty: a package may appear feasible based on its declared weight, but its real weight may later cause the total load to exceed the knapsack capacity.



**Problem Structure**

The problem is structured in two stages.



**Stage 1: Acceptance Decision**

In the first stage, the decision maker observes:

* the number of available items;
* the maximum knapsack capacity;
* the value of each item;
* the theoretical or declared weight of each item.



The real weight is not known at this stage.

Based on this limited information, an acceptance heuristic decides whether each item should be accepted into the knapsack or discarded.



**Stage 2: Real Weight Observation**

In the second stage, the real weights of the accepted items are revealed. If the total real weight of the accepted items is lower than or equal to the knapsack capacity, the solution is feasible. If the total real weight exceeds the capacity, the solution is infeasible and a repair heuristic is applied to remove items until the capacity constraint is respected.



**Main Assumptions**

The project is based on the following assumptions:

* item values are known in advance;
* declared item weights are known in advance;
* real item weights are uncertain and revealed only after the acceptance decision;
* the knapsack has a fixed maximum capacity;
* exceeding the capacity generates a penalty proportional to the overflow;
* repair heuristics can be applied only after real weights are observed.



**Objective**

The objective is to compare different heuristic strategies under weight uncertainty.

The analysis focuses on the trade-off between:

* maximizing the value of the accepted items;
* avoiding infeasible solutions;
* limiting overflow risk;
* preserving useful items after repair.



The project does not aim to find a mathematically optimal solution. Instead, it compares practical heuristic approaches for a stochastic decision-making problem.



**Acceptance Heuristics**

The project considers three acceptance heuristics.



**Conservative Heuristic**

The conservative heuristic accepts an item only if there is enough capacity under a worst-case weight assumption.

This strategy is designed to reduce the risk of exceeding the knapsack capacity. However, it may be too cautious and leave a large amount of capacity unused.



**Maximum Usable Capacity Heuristic**

The maximum usable capacity heuristic accepts items while using only a fixed percentage of the total capacity.

The idea is to keep a safety margin in case the real weights are higher than the declared weights. This heuristic uses the capacity more than the conservative strategy, but it can still be sensitive to weight fluctuations.



**Value-Based Heuristic**

The value-based heuristic prioritizes items whose value is above the average item value.

This strategy aims to increase the knapsack value by selecting more valuable items. However, because it focuses more on value, it may generate solutions that are more exposed to infeasibility when real weights exceed expectations.



**Repair Heuristics**

Repair heuristics are applied only when the accepted set of items exceeds the knapsack capacity after real weights are revealed.

The project considers four repair strategies.



**Greedy Repair**

The greedy repair heuristic removes items with the lowest value-to-weight ratio first.

This strategy tries to preserve items that provide higher value relative to their weight.



**Value Repair**

The value repair heuristic removes items with the lowest value first.

This strategy aims to preserve the most valuable items, regardless of their weight.



**Weight Repair**

The weight repair heuristic removes the heaviest items first.

This strategy is effective for quickly reducing the total weight, but it may remove high-value items.



**Random Repair**

The random repair heuristic removes items randomly until the capacity constraint is respected. This strategy does not use information about item value or item weight, so it is mainly useful as a baseline comparison.



**Evaluation Logic**

The behaviour of the heuristics can be evaluated through indicators such as:

* selected items;
* discarded items;
* total real weight;
* overflow;
* final knapsack value;
* whether a repair heuristic was needed;
* final solution after repair.



The comparison highlights how different heuristics manage the trade-off between value maximization and feasibility under uncertainty.



**Limitations**



The current implementation is based on a limited experimental setting with randomly generated item weights and values. The results should therefore be interpreted as illustrative rather than conclusive.

A more robust analysis could include:

* a larger number of items;
* more simulation runs;
* different probability distributions for real weights;
* average performance indicators across multiple instances;
* comparison of feasibility rate, average value, average overflow and runtime.



The main purpose of the project is to show how Python can be used to model uncertainty, implement heuristic decision rules and analyse the behaviour of solutions under stochastic weights.

