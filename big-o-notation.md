# The Big-O-Notation

## What is the Big-O-Notation and how does it matter? 

In simple terms, the Big O notation describes the complexity of your code using algebraic terms.

__Wikipedia’s definition:__ “Big O notation is a mathematical notation that describes the limiting behavior of a function when the argument tends towards a particular value or infinity. It is a member of a family of notations invented by Paul Bachmann, Edmund Landau, and others, collectively called Bachmann–Landau notation or asymptotic notation.” 

__Complexity Analogy:__ Once upon a time there was an Indian king who wanted to reward a wise man for his excellence. The wise man asked for nothing but some wheat that would fill up a chess board.

![](https://www.freecodecamp.org/news/content/images/2021/06/0_em0jJ2rgj-ZapCef.jpg)

But here were his rules: in the first tile he wants 1 grain of wheat, then 2 on the second tile, then 4 on the next one…each tile on the chess board needed to be filled by double the amount of grains as the previous one. The naïve king agreed without hesitation, thinking it would be a trivial demand to fulfill, until he actually went on and tried it…

So how many grains of wheat does the king owe the wise man? We know that a chess board has 8 squares by 8 squares, which totals 64 tiles, so the final tile should have 2⁶⁴ grains of wheat. If you do a calculation online, you will end up getting 1.8446744*10¹⁹, that is about 18 followed by 18 zeroes. Assuming that each grain of wheat weights 0.01 grams, that gives us 184,467,440,737 tons of wheat. And 184 billion tons is quite a lot, isn’t it?

The numbers grow quite fast later for exponential growth don’t they? The same logic goes for computer algorithms. If the required efforts to accomplish a task grow exponentially with respect to the input size, it can end up becoming enormously large.

![](https://www.freecodecamp.org/news/content/images/2021/06/0_cyqWw3UxODl-wqJi.jpg)