# Python Phase 2 — Conditions to Loops

> **Book:** Fundamentals of Python Programming — Richard L. Halterman  
> **Scope:** Conditional Execution → Iteration  
> **Status:** 🚧 In Progress  
> **Prerequisite:** Python Phase 1 — Fundamentals

---

# 1. Phase 2 Roadmap

## Conditional Execution

- [ ] Boolean expressions
- [ ] `if` statement
- [ ] `if-else` statement
- [ ] Compound Boolean expressions
- [ ] `pass`
- [ ] Floating-point equality
- [ ] Nested conditionals
- [ ] Multi-way decisions: `if-elif-else`
- [ ] Sequential conditionals
- [ ] Conditional expressions
- [ ] Common conditional errors

## Iteration / Loops

- [ ] `while` statement
- [ ] Definite vs indefinite loops
- [ ] `for` statement
- [ ] `range()`
- [ ] Nested loops
- [ ] `break`
- [ ] `continue`
- [ ] `while-else`
- [ ] `for-else`
- [ ] Infinite loops
- [ ] Loop-based problem solving

> **Python note:** Python does not have a native `do-while` statement. A `while True` loop with `break` can be used when the body must execute at least once.

---

# 2. Boolean Expressions

A Boolean expression produces one of two values:

```python
True
False
```

Examples:

```python
age = 21

print(age >= 18)
print(age == 21)
print(age < 10)
```

Output:

```text
True
True
False
```

## Comparison Operators

| Operator | Meaning |
|---|---|
| `==` | Equal to |
| `!=` | Not equal to |
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater than or equal to |
| `<=` | Less than or equal to |

Important:

```python
x = 10      # assignment
x == 10     # comparison
```

---

# 3. `if` Statement

The `if` statement executes a block only when its condition is `True`.

## Syntax

```python
if condition:
    statement
```

Example:

```python
age = 20

if age >= 18:
    print("Adult")
```

## Flow

```text
Condition
   |
   +---- True  → execute block
   |
   +---- False → skip block
```

---

# 4. `if` with User Input

```python
age = int(input("Enter your age: "))

if age >= 18:
    print("You are an adult")
```

The `input()` value is converted to an integer before comparison.

---

# 5. `if-else` Statement

Use `if-else` when there are two possible paths.

## Syntax

```python
if condition:
    statement
else:
    statement
```

Example:

```python
number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

---

# 6. Compound Boolean Expressions

Multiple conditions can be combined using:

```python
and
or
not
```

## `and`

Both conditions must be true.

```python
age = 25

if age >= 18 and age <= 60:
    print("Valid age")
```

## `or`

At least one condition must be true.

```python
day = "Sunday"

if day == "Saturday" or day == "Sunday":
    print("Weekend")
```

## `not`

Reverses a Boolean value.

```python
is_logged_in = False

if not is_logged_in:
    print("Please login")
```

---

# 7. Chained Comparisons

Python supports chained comparisons.

```python
age = 25

if 18 <= age <= 60:
    print("Age is in range")
```

This is equivalent to:

```python
if age >= 18 and age <= 60:
    print("Age is in range")
```

---

# 8. `pass` Statement

`pass` is a placeholder statement.

It does nothing.

```python
age = 20

if age >= 18:
    pass
```

It is useful when a block is intentionally left empty during development.

Example:

```python
if condition:
    pass
else:
    print("Condition was false")
```

---

# 9. Floating-Point Equality

Be careful when comparing floating-point values.

Example:

```python
value = 0.1 + 0.2

print(value)
print(value == 0.3)
```

The result may not behave as expected because floating-point numbers are represented approximately in binary.

A safer approach is to compare with a tolerance.

```python
value = 0.1 + 0.2

if abs(value - 0.3) < 0.000001:
    print("Approximately equal")
```

For normal integer comparisons, direct `==` comparison is straightforward.

---

# 10. Nested Conditionals

A conditional statement inside another conditional statement is called a nested conditional.

Example:

```python
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed")
    else:
        print("ID required")
else:
    print("Not eligible")
```

## Another Example

```python
number = 25

if number >= 0:
    if number == 0:
        print("Zero")
    else:
        print("Positive")
else:
    print("Negative")
```

---

# 11. Multi-Way Decision — `if-elif-else`

When there are multiple possible conditions, use `elif`.

## Syntax

```python
if condition1:
    statement
elif condition2:
    statement
elif condition3:
    statement
else:
    statement
```

Example:

```python
marks = 82

if marks >= 90:
    print("A")
elif marks >= 80:
    print("B")
elif marks >= 70:
    print("C")
elif marks >= 60:
    print("D")
else:
    print("F")
```

Only the first matching branch is executed.

---

# 12. Sequential `if` vs `if-elif`

These are different.

## Separate `if` statements

```python
number = 10

if number > 0:
    print("Positive")

if number < 20:
    print("Less than 20")
```

Both conditions can execute.

## `if-elif`

```python
number = 10

if number > 0:
    print("Positive")
elif number < 20:
    print("Less than 20")
```

Once the first condition is true, the remaining `elif` branches are skipped.

---

# 13. Conditional Expression

Python allows a short one-line conditional expression.

## Syntax

```python
value_if_true if condition else value_if_false
```

Example:

```python
age = 20

result = "Adult" if age >= 18 else "Minor"

print(result)
```

Output:

```text
Adult
```

---

# 14. Common Conditional Errors

## Missing colon

Wrong:

```python
if age >= 18
    print("Adult")
```

Correct:

```python
if age >= 18:
    print("Adult")
```

## Wrong indentation

Wrong:

```python
if age >= 18:
print("Adult")
```

Correct:

```python
if age >= 18:
    print("Adult")
```

## Assignment instead of comparison

Wrong:

```python
if age = 18:
```

Correct:

```python
if age == 18:
```

---

# 15. Condition Practice

## Q1 — Positive / Negative / Zero

Take a number and determine whether it is:

```text
Positive
Negative
Zero
```

## Q2 — Even / Odd

Take an integer and determine whether it is even or odd.

## Q3 — Greatest of Two

Take two numbers and print the greater number.

## Q4 — Greatest of Three

Take three numbers and print the greatest number.

## Q5 — Grade

Take marks and print a grade using `if-elif-else`.

## Q6 — Divisibility

Check whether a number is divisible by both `3` and `5`.

## Q7 — Age Range

Check whether an age is between `18` and `60`.

## Q8 — Nested Condition

Check whether a user is old enough to enter and whether the user has an ID.

---

# 16. What is Iteration?

Iteration means repeatedly executing a block of code.

Python mainly provides:

```python
while
for
```

Loops are useful when the same operation must be performed multiple times.

---

# 17. `while` Statement

A `while` loop repeats while its condition is `True`.

## Syntax

```python
while condition:
    statements
```

Example:

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

Output:

```text
1
2
3
4
5
```

---

# 18. How a `while` Loop Works

```text
Initialize
    ↓
Check condition
    ↓
True? ─── No ──→ Stop
  |
 Yes
  ↓
Execute body
  ↓
Update state
  ↓
Check condition again
```

The update is important because it normally moves the loop toward termination.

---

# 19. Counter-Controlled `while` Loop

A counter-controlled loop keeps track of how many times it has executed.

```python
count = 1

while count <= 10:
    print(count)
    count += 1
```

This prints numbers from `1` through `10`.

---

# 20. Definite vs Indefinite Loops

## Definite Loop

The number of iterations is known or can be determined.

Example:

```python
for i in range(1, 11):
    print(i)
```

## Indefinite Loop

The number of iterations depends on a condition or user input.

Example:

```python
number = int(input("Enter a number: "))

while number != 0:
    print(number)
    number = int(input("Enter another number: "))
```

---

# 21. Accumulator Pattern

An accumulator stores a running result.

Example — sum from 1 to 5:

```python
total = 0
number = 1

while number <= 5:
    total += number
    number += 1

print(total)
```

Output:

```text
15
```

Important pattern:

```python
accumulator = initial_value

while condition:
    accumulator += value
```

---

# 22. Input-Controlled Loop

The loop can continue until the user enters a special value.

Example:

```python
total = 0
number = int(input("Enter number (negative to stop): "))

while number >= 0:
    total += number
    number = int(input("Enter number (negative to stop): "))

print("Total:", total)
```

Here, a negative number acts as a sentinel value.

---

# 23. `for` Statement

The `for` loop iterates over items in a sequence or iterable.

## Syntax

```python
for variable in iterable:
    statements
```

Example:

```python
for number in [1, 2, 3, 4, 5]:
    print(number)
```

---

# 24. `for` with `range()`

`range()` is commonly used for counting.

```python
for i in range(5):
    print(i)
```

Output:

```text
0
1
2
3
4
```

The stop value is excluded.

---

# 25. `range(start, stop)`

```python
for i in range(1, 6):
    print(i)
```

Output:

```text
1
2
3
4
5
```

---

# 26. `range(start, stop, step)`

```python
for i in range(1, 11, 2):
    print(i)
```

Output:

```text
1
3
5
7
9
```

---

# 27. Reverse `range()`

Use a negative step to count backwards.

```python
for i in range(10, 0, -1):
    print(i)
```

Output:

```text
10
9
8
7
6
5
4
3
2
1
```

---

# 28. `for` Loop with a String

Strings are iterable.

```python
word = "Python"

for character in word:
    print(character)
```

Output:

```text
P
y
t
h
o
n
```

---

# 29. Nested Loops

A loop inside another loop is a nested loop.

```python
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)
```

Output:

```text
1 1
1 2
1 3
2 1
2 2
2 3
3 1
3 2
3 3
```

The inner loop completes all of its iterations for every one iteration of the outer loop.

---

# 30. Nested Loop Pattern

## Square

```python
for i in range(4):
    for j in range(4):
        print("*", end=" ")
    print()
```

Output:

```text
* * * *
* * * *
* * * *
* * * *
```

---

# 31. Triangle Pattern

```python
for i in range(1, 6):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()
```

Output:

```text
*
* *
* * *
* * * *
* * * * *
```

---

# 32. `break`

`break` immediately terminates the nearest loop.

```python
for i in range(1, 11):
    if i == 5:
        break
    print(i)
```

Output:

```text
1
2
3
4
```

---

# 33. `continue`

`continue` skips the rest of the current iteration and starts the next iteration.

```python
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
```

Output:

```text
1
2
4
5
```

---

# 34. `break` vs `continue`

| Statement | Effect |
|---|---|
| `break` | Stops the loop |
| `continue` | Skips current iteration |
| `pass` | Does nothing |

---

# 35. `while-else`

Python allows an `else` block with a `while` loop.

The `else` block executes when the loop finishes normally, meaning the loop was not terminated by `break`.

```python
number = 1

while number <= 3:
    print(number)
    number += 1
else:
    print("Loop completed")
```

Output:

```text
1
2
3
Loop completed
```

---

# 36. `for-else`

A `for` loop can also have an `else`.

```python
for i in range(3):
    print(i)
else:
    print("Loop completed")
```

If `break` occurs, the `else` block is skipped.

Example:

```python
for i in range(1, 6):
    if i == 3:
        break
    print(i)
else:
    print("Completed")
```

Output:

```text
1
2
```

---

# 37. Infinite Loops

An infinite loop never reaches a condition that becomes false.

Example:

```python
while True:
    print("Running")
```

This continues indefinitely until interrupted.

A common intentional pattern is:

```python
while True:
    number = int(input("Enter a number: "))

    if number == 0:
        break
```

Here, `break` provides the exit condition.

---

# 38. Avoiding Accidental Infinite Loops

Bad:

```python
count = 1

while count <= 10:
    print(count)
```

`count` never changes.

Correct:

```python
count = 1

while count <= 10:
    print(count)
    count += 1
```

General rule:

> A `while` loop should normally change something that can eventually make its condition false.

---

# 39. Do-While Equivalent in Python

Python has no native `do-while` statement.

When the body must execute at least once, use:

```python
while True:
    # execute body

    if exit_condition:
        break
```

Example:

```python
while True:
    number = int(input("Enter a positive number: "))

    if number > 0:
        break
```

The body runs before the exit condition is checked.

---

# 40. `for` vs `while`

| `for` | `while` |
|---|---|
| Good for iterating over a sequence | Good for condition-controlled repetition |
| Common when the iteration range is known | Common when the number of iterations is unknown |
| Works naturally with `range()` | Requires a condition |
| Can iterate over strings and other iterables | Usually controlled by changing state |

Example:

```python
for i in range(1, 6):
    print(i)
```

Equivalent counting loop:

```python
i = 1

while i <= 5:
    print(i)
    i += 1
```

---

# 41. Loop Practice

## Q9 — Print 1 to 100

Use a `for` loop.

## Q10 — Print Even Numbers

Print all even numbers from `1` to `100`.

## Q11 — Print Odd Numbers

Print all odd numbers from `1` to `100`.

## Q12 — Sum 1 to 100

Calculate the sum of numbers from `1` to `100`.

## Q13 — Multiplication Table

Take a number from the user and print its table from `1` to `10`.

## Q14 — Countdown

Print numbers from `10` down to `1`.

## Q15 — Factorial

Calculate the factorial of a number using a loop.

Example:

```text
5! = 120
```

## Q16 — Sum of Digits

Input:

```text
12345
```

Output:

```text
15
```

## Q17 — Reverse a Number

Input:

```text
12345
```

Output:

```text
54321
```

## Q18 — Count Digits

Input:

```text
123456
```

Output:

```text
6
```

## Q19 — Prime Number

Check whether a number is prime.

## Q20 — Fibonacci Series

Print the first `n` Fibonacci numbers.

Example:

```text
0 1 1 2 3 5 8 13
```

---

# 42. Pattern Practice

## Pattern 1

```text
*
* *
* * *
* * * *
* * * * *
```

## Pattern 2

```text
* * * * *
* * * *
* * *
* *
*
```

## Pattern 3

```text
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
```

## Pattern 4

```text
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
```

---

# 43. Important Problem-Solving Patterns

## Counter

```python
count = 0

while condition:
    count += 1
```

## Accumulator

```python
total = 0

while condition:
    total += value
```

## Sentinel

```python
while value != sentinel:
    ...
```

## Search with `break`

```python
for value in data:
    if value == target:
        break
```

## Skip with `continue`

```python
for value in data:
    if condition:
        continue
    # process value
```

---

# 44. Phase 2 Quick Revision

```text
Boolean Expressions
       ↓
if
       ↓
if-else
       ↓
Compound Conditions
       ↓
Nested if
       ↓
if-elif-else
       ↓
Conditional Expression
       ↓
while
       ↓
for + range()
       ↓
Nested Loops
       ↓
break / continue
       ↓
while-else / for-else
       ↓
Infinite Loops
       ↓
Problem Solving
```

---

# 45. Phase 2 Checklist

## Conditions

- [ ] Boolean expressions
- [ ] Comparison operators
- [ ] `if`
- [ ] `if-else`
- [ ] `and`
- [ ] `or`
- [ ] `not`
- [ ] Chained comparisons
- [ ] `pass`
- [ ] Floating-point comparison
- [ ] Nested `if`
- [ ] `if-elif-else`
- [ ] Sequential conditionals
- [ ] Conditional expressions
- [ ] Conditional errors

## Loops

- [ ] Iteration concept
- [ ] `while`
- [ ] Counter-controlled loops
- [ ] Accumulators
- [ ] Sentinel-controlled loops
- [ ] Definite vs indefinite loops
- [ ] `for`
- [ ] `range()`
- [ ] Step / reverse ranges
- [ ] Iterating over strings
- [ ] Nested loops
- [ ] `break`
- [ ] `continue`
- [ ] `while-else`
- [ ] `for-else`
- [ ] Infinite loops
- [ ] Do-while equivalent

---

# 46. Progress Checkpoint

### Phase 1 — Fundamentals

**Status: ✅ COMPLETED**

Topics:

```text
Comments & Variables
Data Types
Strings
Type Conversion
Input & Output
Operators
```

### Phase 2 — Conditions & Loops

**Status: 🚧 CURRENT PHASE**

Target:

```text
Conditions → Loops → Nested Loops → Problem Solving
```

---

# 47. Phase 2 Completion Target

After completing this phase, you should be able to write programs that:

- Make decisions using conditions.
- Handle multiple conditions.
- Repeat operations using `for`.
- Repeat operations using `while`.
- Control loops using `break` and `continue`.
- Work with counters and accumulators.
- Build nested loops.
- Solve basic number problems.
- Build basic pattern programs.
- Understand and avoid infinite loops.
- Implement do-while-style behavior in Python.

---

# 🚀 Next Phase

After Phase 2:

```text
Phase 3 → Python Data Structures
```

Recommended progression:

```text
Lists
Tuples
Sets
Dictionaries
String/Data-structure problem solving
```

---

## Source Alignment

This phase is organized around the **Conditional Execution** and **Iteration** portions of Richard L. Halterman's *Fundamentals of Python Programming*, including Boolean expressions, conditional statements, nested/multi-way decisions, `while`, `for`, nested loops, `break`, `continue`, loop `else` clauses, and infinite-loop concepts.

The user's supplied Google Drive copy could not be directly read because the Drive viewer required sign-in, so these notes follow the identifiable book structure and Python concepts rather than reproducing the book's text.
