## Data centers
- Most software runs today on data centers
- Increasing share of renewable energy sources that power data centers
- The bigger the data centers the higher are advantages through scaling effects. (Large data centers efficency is higher vs distributed computing
)
- _Moore's Law:_ the number of transistors in integrated circuits doubles every two years. 
- _Koomey's Law:_ 50% lower energy consumption unit every 1,5, years; (increased efficiency)

![Tilman Santarius: "Smarte grune Welt?", 2018]()

- _Rebound effect:_ Increasing efficiency advancements are compensated by increasing demand. 
- _Wirth's Law:_ "[..] software is getting slower more rapidly than hardware is becoming faster"

### Hardware measurements
- Methods include to:
    - Use power meters at wall plug sockets
    - Intercept CPU power lines
    - Use specialized development boards/ circuits
- Pro: Precise measurements
- Con: Difficult to break down to individual components or even programs

### Software measurements 
- Intel RAPL as software power meter and basis for most apporaches 
- PowerAPI as high-level software suite to measure consumption on device, process and program level
- DockerCap for power budgeting on container level
- Code execution time measurements for method-level insights
- Pros:
    - Non-intrusive
    - High level of granularity 

- Cons: 
    - Rather inaccurate, since usually based on power model instead of true measurements
    - Overhead of the measuring software itself
    - Dependent on hardware characteristics/ capabilities  
    
## Cache 
_A cache is a high speed data storage layer which stores a subset of data, typically transient in nature, so that future requests for that data are served up faster[..], caching allows you to efficiently reuse previously retrieved or computed data._ (aws.amazon.com)

- Store vs recompute: the trade-off between speed and "up-to-dateness" of data 
- memory is cheaper than computation

- What can be cached? 
    - Resources on the web (images, JS or CSS assets, HTML pages)
    - Result from database queries or API calls
    - Intermediate results within a calculation/ algorithm

- When can things be cached? 
    - Anytime data doesn not change in mean time 
