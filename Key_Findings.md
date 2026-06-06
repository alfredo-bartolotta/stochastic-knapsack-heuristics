**Key Findings**

This project analyses a stochastic knapsack problem in which item weights are uncertain. The declared weight is known at the acceptance stage, while the real weight is revealed only afterwards. The results should be interpreted as illustrative because the experiment is based on a limited number of generated instances.



**Acceptance Heuristics**

The conservative heuristic is the safest acceptance strategy. In the analysed instances, it keeps overflow negative, meaning that the knapsack remains below the capacity limit. However, this safety comes at the cost of a lower knapsack value because the heuristic discards many items to maintain a strong safety margin.



The maximum usable capacity heuristic exploits the available capacity better than the conservative heuristic. It accepts more items and can obtain a higher value, but it is more sensitive to weight fluctuations. In some scenarios, this heuristic may still generate infeasible solutions when the realised weights are higher than expected.



The value-based heuristic generally obtains the highest knapsack value among the acceptance heuristics. It prioritizes items with value above the average and therefore selects more valuable combinations. However, this strategy is riskier because it may accept items without maintaining an adequate safety margin against stochastic weight increases.



Overall, the acceptance heuristic comparison highlights a trade-off between safety and value. Conservative choices reduce the risk of infeasibility but may underuse capacity, while value-oriented choices increase the objective value but expose the solution to higher feasibility risk.



**Repair Heuristics**

Repair heuristics are activated when the accepted set of items exceeds the knapsack capacity after the real weights are observed.



The value-based repair and greedy repair heuristics generally provide the best repaired solutions in terms of final objective value. This happens because both strategies tend to preserve the utility of the most important items. The greedy repair removes items with the lowest value-to-weight ratio first, while the value repair removes items with the lowest absolute value first.



The weight-based repair reduces infeasibility by removing the heaviest items first. This can be effective for quickly restoring feasibility, but it may remove items that have high value.



The random repair sometimes obtains results similar to other repair strategies. However, this should not be interpreted as evidence of strong performance. In the analysed instances, the knapsack often contains a small number of items and the overflow can sometimes be fixed by removing only one item. In such cases, even a random removal may lead to a comparable result.



**Main Interpretation**

The results suggest that the value-based acceptance heuristic is attractive when the goal is to maximize knapsack value, but it requires a repair mechanism because it can produce infeasible solutions. The conservative heuristic is useful when avoiding capacity violations is the priority, but it may be too cautious and lead to low value. Among the repair strategies, value-based and greedy repair appear more effective because they use information about item utility, while weight-based and random repair do not fully account for the trade-off between item value and item weight.



**Limitations**

The current experimental setup does not fully highlight the impact of the different heuristics because the number of analysed scenarios is limited. Broader experiments would be needed to obtain more robust conclusions. Future extensions could include:



* increasing the number of simulation runs;
* testing larger item sets;
* comparing different weight distributions;
* evaluating average performance across many random instances;
* measuring feasibility rate, average overflow, average value and runtime;
* storing results in a structured table for further analysis.



The main value of this project is to show how Python can be used to model uncertainty, implement decision heuristics and compare solution behaviour under stochastic weights.

