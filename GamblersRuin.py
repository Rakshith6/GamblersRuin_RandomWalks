
# Random walk of gamblers money to show Gambler Ruin in roulette
# Gambler tries to achieve a goal money by betting one dollar every spin in roulette
# What is the probability that the gambler is not ruined i.e. gambler doesnt run out of money?
# Run simulations of several episodes and count proportion of episodes in which the gambler is not ruined! Each episode ends when the gambler is ruined or when he achieves goal money.

import numpy as np

class Gambler():
    def __init__(self):
        self.initial_money=100
        self.current_money=self.initial_money
        self.goal_money=self.initial_money+50
        self.bets_won=0

    def update_money(self,outcome):
        self.current_money+=outcome
        if outcome==1:
            self.bets_won+=1

        if self.current_money==self.goal_money or self.current_money==0:
            result=self.current_money/self.goal_money
            return True,result
        else:
            return False,0


class Roulette():
    def __init__(self):
        self.win_prob=18/38

    def play_roulette(self):
        fate=np.random.random_sample()
        if fate<self.win_prob:
            outcome=1
        else:
            outcome=-1

        return outcome


episodes=100000
finished_episodes=np.arange(int(episodes/10),episodes,int(episodes/10))

gambler = Gambler()
roulette = Roulette()

episode_wins=0
episode_spins=np.zeros(episodes)
episode_betswon=np.zeros(episodes)

for i in range(episodes):
    if i in finished_episodes:
        print('Completed {} episodes'.format(i))

    end = False
    gambler.__init__()
    spins=0
    while end==False:
        outcome=roulette.play_roulette()
        end,result=gambler.update_money(outcome)
        spins+=1
    episode_wins+=result
    episode_spins[i]=spins
    episode_betswon[i]=gambler.bets_won

print('The probability of winning from simulation of {} episodes is {}'.format(episodes,episode_wins/episodes))
# print('The average number of roulette spins per episode is: ', np.mean(episode_spins))

# Reference : http://web.mit.edu/neboat/Public/6.042/randomwalks.pdf
# Using recursive relation we can obtain true probability of achieving the goal amount using the formula shown below
p=roulette.win_prob
T=gambler.goal_money
n=gambler.initial_money
true_probability=(((1-p)/p)**n-1)/(((1-p)/p)**T-1)
print("The true probability of winning is {}".format(true_probability))


