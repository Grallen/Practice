#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Challenge: Burst Balloons Problem (LeetCode #312)
# You are given a List of positive integers nums, where each number represents a balloon with that number written on it. You need to burst all the balloons in an order that maximizes the total coins you collect.
# How Do You Collect Coins?
# When you burst a balloon i, you get coins equal to: coins=nums[left]×nums[i]×nums[right]
# A burst ballooon is removed from the List
# Example:
# Input: [3,1,5,8]
# Output: 167
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Clear the console
print("\033[H\033[J", end="")

test_values = [3,1,5,8]

memo = {}  # Ack! a global!

class PoppableBalloons:
    _balloons = []
    def __init__(self, balloons):
        self._balloons = balloons
    
    def pop(self, i):
        coins = self._balloons[i]
        action = f"{coins}"
        if i-1 >= 0:
            coins *= self._balloons[i-1] # multiply by previous if present
            action = f"{self._balloons[i-1]}*{action}"
        if i+1 < len(self._balloons):
            coins *= self._balloons[i+1] # multiply by next if present
            action = f"{action}*{self._balloons[i+1]}"
        return { "balloons" : (self._balloons[:i] + self._balloons[i + 1:]), "coins": coins, "action": action }

    def tuple(self):
        return tuple(self._balloons)
    
    def iterate(self):
        return enumerate(self._balloons)



def balloon_burst(in_balloons, total = 0):
    balloons = PoppableBalloons(in_balloons)
    key = balloons.tuple()
    if key in memo:
        return total + memo[key]
    best = total
    localbest = 0
    for k, value in balloons.iterate():
        results = balloons.pop(k)
        sub_total = total + results["coins"]
        if len(results["balloons"]) > 0:
            before = sub_total
            sub_total = balloon_burst(results["balloons"], sub_total)
        best = max(best, sub_total)

    memo[key] = best - total
    return best

print(f"{balloon_burst(test_values)}")
