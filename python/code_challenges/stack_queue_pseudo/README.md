## Challenge description




## Link to code

[Code: Stack-Queue-pseudo](/home/wonde/codefellows/code-401/data-structures-and-algorithms/python/code_challenges/stack_queue_pseudo/stack_queue_pseudo.py)

[Test: Stack-Queue-pseudo](/home/wonde/codefellows/code-401/data-structures-and-algorithms/python/tests/test_stack_queue_pseudo.py)

## Unit Tests Required


## Whiteboard

[Whiteboard Image](/home/wonde/codefellows/code-401/data-structures-and-algorithms/python/code_challenges/images/stack-queue-pseudo.jpg)

## approach and efficiency

We used two stacks. All items get pushed and stored on the first stack. Whenever a dequeu needs to happen, we move everything from the first stack to the second and then pop off. Then to keep the correct order, we pop everything back into the first stack.

Big O:

Time: O(n)
Space: O(1)

## Resources and Collaboration

This is done in collaboration with my class mates Daniel Dills, Davve Sok, and Micheal Ryan And Prabin

The following link helped me to visualize the problem

[How to Implement a Queue Using Two Stacks](https://betterprogramming.pub/how-to-implement-a-queue-using-two-stacks-80772242b88c)

