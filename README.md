**Stochastic Knapsack Heuristics**

**Project Overview**
This project implements a Python simulation of a knapsack problem with stochastic item weights. The problem is inspired by a logistics setting in which a courier must decide whether to accept packages based on declared weights. However, the real weight of each package is only revealed when the courier collects it. As a result, the accepted set of packages may exceed the vehicle or knapsack capacity once the real weights become known.
The goal of the project is to compare different acceptance and repair heuristics under uncertainty.

**Problem Setting**
The problem is structured in two stages:

**Stage 1: Acceptance Decision**
At the first stage, the decision maker observes:
* the number of items;
* the knapsack capacity;
* the value of each item;
* the theoretical or declared weight of each item.

The real weight is not known yet.
Based on this information, an acceptance heuristic decides whether each item should be accepted or discarded.

**Stage 2: Real Weight Observation and Repair**
At the second stage, the real weights are revealed. If the total real weight of the accepted items exceeds the knapsack capacity, the solution becomes infeasible. In that case, a repair heuristic is applied to remove items until the capacity constraint is respected. If the capacity is exceeded before repair, a penalty proportional to the excess weight is considered.

**Acceptance Heuristics**
The project compares three acceptance heuristics:

**Conservative Heuristic**
This heuristic accepts an item only if there is enough capacity under a worst-case weight assumption. It keeps a strong safety margin but may lead to low knapsack value.

**Maximum Usable Capacity Heuristic**
This heuristic uses only a fixed percentage of the total capacity in order to keep a margin against weight uncertainty. It exploits capacity better than the conservative heuristic but remains sensitive to real weight fluctuations.

**Value-Based Heuristic**
This heuristic prioritizes items with value above the average item value, while considering declared weights. It tends to generate higher knapsack value but may be more exposed to infeasibility when real weights are higher than expected.

**Repair Heuristics**
When the real weight of accepted items exceeds the capacity, the following repair heuristics are considered:

**Greedy Repair**
Removes items with the lowest value-to-weight ratio first.

**Value Repair**
Removes items with the lowest value first.

**Weight Repair**
Removes the heaviest items first.

**Random Repair**
Randomly removes items until the capacity constraint is respected.

**Files in This Repository**
* knapsack\_problem.py: Python implementation of the stochastic knapsack simulation and heuristics.
* key\_findings.md: summary of the main experimental observations.
* problem\_description.md: explanation of the logistics setting and modelling assumptions.

**Main Concepts**
This project demonstrates:
* stochastic weights;
* decision-making under uncertainty;
* heuristic-based acceptance decisions;
* infeasibility and repair strategies;
* capacity constraints;
* trade-off between safety and value;
* simulation-based comparison of heuristic performance.

**Limitations**
The experimental setup is based on a small number of generated instances. Therefore, the results should be interpreted as illustrative rather than conclusive. A broader computational experiment with more instances, more variability and repeated simulation runs would be needed to draw stronger conclusions about the relative performance of the heuristics.

