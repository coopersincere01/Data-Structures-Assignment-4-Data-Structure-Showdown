# Question 18: Keep Last X Values
# Track the last 3 items in a stream of values.
# Older values should be removed automatically.
# Input: Add [1, 2, 3, 4, 5]
# Output: [3, 4, 5]

from collections import deque


class LastValues:
    def __init__(self):
        self.values = deque(maxlen=3)

    def add(self, value):
        self.values.append(value)

    def get_values(self):
        return list(self.values)


# Test 1: More than 3 values
tracker = LastValues()
tracker.add(1)
tracker.add(2)
tracker.add(3)
tracker.add(4)
tracker.add(5)

print(tracker.get_values())  # Expected: [3, 4, 5]


# Test 2: Empty tracker
empty_tracker = LastValues()
print(empty_tracker.get_values())  # Expected: []


# Test 3: Fewer than 3 values
small_tracker = LastValues()
small_tracker.add(10)
small_tracker.add(20)

print(small_tracker.get_values())  # Expected: [10, 20]

"""
For the timed challenge I chose to use a deque because the problem required keeping only the last three values that were added. A deque made sense because it works well when adding and removing values from the ends of a collection. I also used maxlen=3 so that once a fourth value was added the oldest value would automatically be removed. This kept the solution simple instead of having to manually check the size and remove an item every time.

The 30 minute time limit definitely affected how I approached the problem. Once the timer started I felt more pressure to make a decision quickly instead of spending too much time thinking through every possible option. I focused on finding a structure that matched the problem directly and getting a working version completed first. After that, I tested it with the example from the prompt, an empty tracker, and a tracker with fewer than three values.

One trade-off I made was using Python's built-in deque instead of creating my own queue structure. Under the time limit I felt that using a structure that already handled the behavior I needed was more reliable and gave me more time to test my solution. I also kept the tracker fixed at three values because that was what the prompt specifically required. Overall, the challenge showed me that the time pressure makes choosing the right structure early much more important.
"""