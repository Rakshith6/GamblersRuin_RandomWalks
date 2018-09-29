# GamblersRuin_RandomWalks
Simulating gamblers ruin in a game of roulette using random walks.

The gambler starts with money in hand. He decides to bet 1 dollar on either red or black for every spin of the roulette. If he wins on that spin he wins a dollar and on the contrary he loses the dollar. He stops playing when he runs out of money or when he reaches a goal money. He repeats this a number of times to determine the odds of winning the goal amount.

In this code, gambler starts with 100$ and stops playing when he reaches 0$ or 150$. The code runs a number of episodes to determine the odds of winning. It also compares the results to the true probability calculated using a recursive formula (http://web.mit.edu/neboat/Public/6.042/randomwalks.pdf)
