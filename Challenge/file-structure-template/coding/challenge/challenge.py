import random

"""
This array of integers defines the input sizes for each test case.
The test cases should get increasingly larger, with the first test case being the smallest.
The last test case should be the largest.
"""
INPUT_SIZES = [
  5,      # test 0
  10,     # test 1
  20,     # test 2
  50,     # test 3
  100,    # test 4 
  500,    # test 5
  1_000,  # test 6
  2_000,  # test 7
  5_000,  # test 8
  10_000, # test 9
]

"""
The following global variables are required by the coding template.
Do not change their names or types
"""

# Question count is the number of test cases.
QUESTION_COUNT = len(INPUT_SIZES)
"""
LAST_VISIBLE_TEST_IDX :: the index of the last test case that will be visible to the user.

The remaining test cases will be hidden.
This is usually set to 4 for a 10 test case challenge.
"""
LAST_VISIBLE_TEST_IDX = 4
"""
These two variables define the time limit for each test case (in seconds).

- TIME_LIMIT_SEC :: the time limit for interpreted code (python),
- TIME_LIMIT_COMPILED_SEC :: the time limit for compiled code (rust, c++, etc).

We require two solvers to ensure that the challenge is solvable in both interpreted and compiled languages,
and to make sure it is equally challenging for both in terms of time.
One global time limit would favor compiled languages, as they are generally faster.
These time limits are used to make sure very inefficient solutions are not accepted.
They can be reconfigured by the htb team if needed.
"""
TIME_LIMIT_SEC = 5
TIME_LIMIT_COMPILED_SEC = 3

"""
This function generates a question and an answer for a given test index.
Do not change the name of this function.
"""
def gen_question(test_idx):
  # use the INPUT_SIZES array to determine the length of the input for this test case
  length = INPUT_SIZES[test_idx]

  # generate the question and answer
  MIN, MAX = -10_000, 10_000
  num1 = random.randint(MIN, MAX)
  num2 = random.randint(MIN, MAX)
  target = num1 + num2

  nums = [num1, num2]

  while len(nums) < length:
    candidate = random.randint(MIN, MAX)
    if target - candidate not in nums:
      nums.append(candidate)
  
  random.shuffle(nums)

  question = str(target) + " " + str(length) + "\n"
  question += " ".join([str(x) for x in nums])
  answer = f"{num1} {num2}" if num1 < num2 else f"{num2} {num1}"

  # return the question and answer
  return question, answer