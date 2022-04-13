# Power Consumption
- _1970 - 1990:_ "IPAT formula" by Ehrlich & Ehrlich considered interactions between technology and ecology: 

Ecological Impact = Population x Affluence x Technology

- _1990 - today:_ J. Huber extended the formula. Consensus today: 

Ecological Impact = Population x _Efficiency_ x _Consistency_ x _Sufficiency_

__Efficiency:__ 
- Good/ Resource consumption
- High output (more computation), small input (say less electrical energy) 
- How to optimize resource consumption of technology? 
- today's economical model


__Consistency:__
- Nature pollution/ Resource consumption
- How much of our 1 unit of consumption, polute the environment? 
- How can technology be non-pollutive resp. climate positive? 
- circular economy: existing goods are shared 

__Sufficiency:__
- Good/ capita
- How much technology do we need? 
- degrowth/ post-growth economy 


||Efficiency| Consistency (circular economy)| Sufficiency (degrowth)|
|-|-|-|-|
|Solutions | More computing performance, virtualisation| Reuse software, maintain open source software; Share resources; Use renewable energy sources in data centers| Use less; don't use if its not necessary|
|Barriers|Rebound effect & Wirth's law|Proprietary business models| Low acceptance rate|

- Energy = Power x Time 
- Strong correlation between execution time and energy efficiency, but it is not the same
- Reasons: I/O, memory access, CPU idle,.. 

### Technology Choice
- Programming language, frameworks, libraries
- Compiled languages tend to be faster than interpreted ones
- Common trade-off: efficiency vs. developer productivity 
- Choose according your demand 
- Consider: 
    - Use case
    - Team skills
    - Non-functional requirements, e.g. expected system load
    - Project size

## Energy Effciency
- For data ceners, e.g.:
    PUE = Total Facility Energy /IT Equipment Energy

- Energy[J] = Power[W] x Time[s]
- W = J/s
- Energy Eff. = # computations/ Joule 

|Hardware | Software | Analytically|
|-|-|-|
|Using hardware power meters and specialized development boards| Using software-defined power meters, meterics collection hooks inside programs and different heuristics| For instance through breaking down programs into individual CPU instructions

