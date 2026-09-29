# Python — Phase 1: Fundamentals

> **Status:** ✅ Completed
> **Language:** Python
> **Phase:** 1 — Fundamentals
> **Goal:** Python ke basic programming concepts ko strong karna.

---

# 📚 Phase 1 Topics

* [x] 1. Comments and Variables
* [x] 2. Data Types
* [x] 3. Strings and Type Conversion
* [x] 4. Input and Output
* [x] 5. Operators

---

# 1. Comments and Variables

## 1.1 Comments

Comments code ko explain karne ke liye use hote hain.

Python comments ko execute nahi karta.

### Single-line Comment

```python
# This is a comment
print("Hello Python")
```

### Example

```python
# Store user's name
name = "Het"

print(name)
```

---

## 1.2 Variables

Variable ek container/reference hai jisme hum data store karte hain.

```python
name = "Het"
age = 21
salary = 25000
```

Yaha:

```text
name   → "Het"
age    → 21
salary → 25000
```

### Example

```python
name = "Het"
age = 21

print(name)
print(age)
```

Output:

```text
Het
21
```

---

## 1.3 Variable Naming Rules

Valid:

```python
name = "Het"
age = 21
user_name = "Het"
totalMarks = 90
_marks = 100
```

Invalid:

```python
# 1name = "Het"       ❌
# user-name = "Het"   ❌
# class = "Python"    ❌
```

### Rules

1. Variable number se start nahi ho sakta.
2. Variable me spaces nahi hone chahiye.
3. `_` allowed hai.
4. Python keywords variable names nahi ho sakte.
5. Python case-sensitive hai.

```python
name = "Het"
Name = "Patel"

print(name)
print(Name)
```

`name` aur `Name` different variables hain.

---

## 1.4 Multiple Variable Assignment

```python
name, age, city = "Het", 21, "Surat"

print(name)
print(age)
print(city)
```

---

## 1.5 Same Value to Multiple Variables

```python
x = y = z = 100

print(x)
print(y)
print(z)
```

---

# 2. Data Types

Python me data ke different types hote hain.

Main basic data types:

```text
int
float
complex
str
bool
NoneType
```

---

## 2.1 Integer — int

Whole numbers ko integer kehte hain.

```python
age = 21
marks = 95
temperature = -5
```

Check type:

```python
age = 21

print(type(age))
```

Output:

```text
<class 'int'>
```

---

## 2.2 Float — float

Decimal numbers ko float kehte hain.

```python
price = 99.99
percentage = 85.5
height = 5.8
```

```python
print(type(price))
```

Output:

```text
<class 'float'>
```

---

## 2.3 Complex — complex

Complex number me real aur imaginary part hota hai.

```python
x = 3 + 4j

print(x)
print(type(x))
```

Output:

```text
(3+4j)
<class 'complex'>
```

---

## 2.4 String — str

Text ko string kehte hain.

```python
name = "Het"
language = 'Python'
```

Dono valid hain:

```python
name = "Het"
name = 'Het'
```

---

## 2.5 Boolean — bool

Boolean ke sirf do values hote hain:

```text
True
False
```

Example:

```python
is_logged_in = True
is_admin = False

print(is_logged_in)
print(type(is_logged_in))
```

---

## 2.6 NoneType

`None` ka matlab hai currently koi value nahi hai.

```python
result = None

print(result)
print(type(result))
```

Output:

```text
None
<class 'NoneType'>
```

---

## 2.7 type()

Kisi variable ka data type check karne ke liye `type()` use karte hain.

```python
name = "Het"
age = 21
salary = 25000.50
is_student = True

print(type(name))
print(type(age))
print(type(salary))
print(type(is_student))
```

---

# 3. Strings and Type Conversion

# 3.1 String Basics

String text ka collection hota hai.

```python
name = "Het Patel"

print(name)
```

---

## 3.2 String Concatenation

Do strings ko `+` se combine kar sakte hain.

```python
first_name = "Het"
last_name = "Patel"

full_name = first_name + " " + last_name

print(full_name)
```

Output:

```text
Het Patel
```

---

## 3.3 String Repetition

`*` se string repeat kar sakte hain.

```python
text = "Python "

print(text * 3)
```

Output:

```text
Python Python Python
```

---

## 3.4 String Indexing

String ka har character ek index par hota hai.

```python
name = "Python"
```

Index:

```text
 P  y  t  h  o  n
 0  1  2  3  4  5
```

Example:

```python
name = "Python"

print(name[0])
print(name[1])
print(name[5])
```

Output:

```text
P
y
n
```

---

## 3.5 Negative Indexing

Negative indexing last character se start hoti hai.

```text
 P  y  t  h  o  n
-6 -5 -4 -3 -2 -1
```

Example:

```python
name = "Python"

print(name[-1])
print(name[-2])
```

Output:

```text
n
o
```

---

## 3.6 String Slicing

Syntax:

```python
string[start:end]
```

Example:

```python
name = "Python"

print(name[0:3])
```

Output:

```text
Pyt
```

`end` index include nahi hota.

---

### Slicing Examples

```python
name = "Python"

print(name[:3])
print(name[2:])
print(name[:])
```

Output:

```text
Pyt
thon
Python
```

---

## 3.7 String Length

`len()` string ki length return karta hai.

```python
name = "Python"

print(len(name))
```

Output:

```text
6
```

---

# 3.8 Important String Methods

## upper()

```python
name = "python"

print(name.upper())
```

Output:

```text
PYTHON
```

---

## lower()

```python
name = "PYTHON"

print(name.lower())
```

Output:

```text
python
```

---

## strip()

Starting aur ending ke unnecessary spaces remove karta hai.

```python
name = "   Het   "

print(name.strip())
```

Output:

```text
Het
```

---

## replace()

```python
text = "I love Java"

print(text.replace("Java", "Python"))
```

Output:

```text
I love Python
```

---

## split()

String ko list me convert karta hai.

```python
text = "Python Java JavaScript"

result = text.split()

print(result)
```

Output:

```text
['Python', 'Java', 'JavaScript']
```

---

## startswith()

```python
text = "Python"

print(text.startswith("Py"))
```

Output:

```text
True
```

---

## endswith()

```python
text = "Python"

print(text.endswith("on"))
```

Output:

```text
True
```

---

# 3.9 Type Conversion

Type conversion ka matlab ek data type ko dusre data type me convert karna.

Common functions:

```text
int()
float()
str()
bool()
```

---

## String → Integer

```python
age = "21"

age = int(age)

print(age)
print(type(age))
```

---

## Integer → Float

```python
num = 10

num = float(num)

print(num)
```

Output:

```text
10.0
```

---

## Integer → String

```python
age = 21

age = str(age)

print(age)
print(type(age))
```

---

## Float → Integer

```python
price = 99.99

price = int(price)

print(price)
```

Output:

```text
99
```

Decimal part remove ho jata hai.

---

## String → Float

```python
price = "99.99"

price = float(price)

print(price)
```

---

## Value → Boolean

```python
print(bool(1))
print(bool(0))
```

Output:

```text
True
False
```

Generally:

```text
0       → False
""      → False
None    → False
```

Non-empty/non-zero values generally `True` hoti hain.

---

# 4. Input and Output

# 4.1 print()

Output display karne ke liye `print()` use hota hai.

```python
print("Hello World")
```

Multiple values:

```python
name = "Het"
age = 21

print(name, age)
```

---

## 4.2 Multiple print()

```python
print("Hello")
print("Python")
```

Output:

```text
Hello
Python
```

---

# 4.3 input()

User se data lene ke liye `input()` use hota hai.

```python
name = input("Enter your name: ")

print(name)
```

Example:

```text
Enter your name: Het
Het
```

### Important

`input()` by default **string return karta hai**.

```python
age = input("Enter age: ")

print(type(age))
```

Even if user enters:

```text
21
```

type hoga:

```text
<class 'str'>
```

---

# 4.4 Integer Input

Agar integer input chahiye:

```python
age = int(input("Enter your age: "))

print(age)
print(type(age))
```

---

# 4.5 Float Input

```python
price = float(input("Enter price: "))

print(price)
```

---

# 4.6 User Input Example

```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))

print("Name:", name)
print("Age:", age)
```

---

# 4.7 f-string

Dynamic output ke liye f-string useful hai.

```python
name = "Het"
age = 21

print(f"My name is {name} and I am {age} years old.")
```

Output:

```text
My name is Het and I am 21 years old.
```

---

# 5. Operators

Operators values par operations perform karte hain.

Main operator categories:

```text
1. Arithmetic Operators
2. Assignment Operators
3. Comparison Operators
4. Logical Operators
5. Membership Operators
6. Identity Operators
```

---

# 5.1 Arithmetic Operators

Arithmetic operators:

| Operator | Meaning        |
| -------- | -------------- |
| `+`      | Addition       |
| `-`      | Subtraction    |
| `*`      | Multiplication |
| `/`      | Division       |
| `//`     | Floor Division |
| `%`      | Modulus        |
| `**`     | Exponent       |

---

## Addition

```python
a = 10
b = 5

print(a + b)
```

Output:

```text
15
```

---

## Subtraction

```python
print(a - b)
```

Output:

```text
5
```

---

## Multiplication

```python
print(a * b)
```

Output:

```text
50
```

---

## Division

```python
print(a / b)
```

Output:

```text
2.0
```

Python `/` generally float result deta hai.

---

## Floor Division

```python
print(10 // 3)
```

Output:

```text
3
```

---

## Modulus

Remainder find karne ke liye `%` use hota hai.

```python
print(10 % 3)
```

Output:

```text
1
```

---

## Exponent

Power ke liye `**` use hota hai.

```python
print(2 ** 3)
```

Output:

```text
8
```

---

# 5.2 Assignment Operators

Basic assignment:

```python
x = 10
```

Compound assignment operators:

```text
+=
-=
*=
/=
%=
**=
//=
```

Examples:

```python
x = 10

x += 5
print(x)
```

Output:

```text
15
```

---

```python
x = 10

x -= 3

print(x)
```

Output:

```text
7
```

---

```python
x = 10

x *= 2

print(x)
```

Output:

```text
20
```

---

# 5.3 Comparison Operators

Comparison ka result always Boolean hota hai:

```text
True
False
```

Operators:

```text
==
!=
>
<
>=
<=
```

---

## Equal

```python
print(10 == 10)
```

Output:

```text
True
```

---

## Not Equal

```python
print(10 != 5)
```

Output:

```text
True
```

---

## Greater Than

```python
print(10 > 5)
```

Output:

```text
True
```

---

## Less Than

```python
print(5 < 10)
```

Output:

```text
True
```

---

## Greater Than or Equal

```python
print(10 >= 10)
```

Output:

```text
True
```

---

## Less Than or Equal

```python
print(5 <= 10)
```

Output:

```text
True
```

---

# 5.4 Logical Operators

Python ke logical operators:

```text
and
or
not
```

---

## and

Dono conditions true honi chahiye.

```python
age = 21

print(age >= 18 and age <= 30)
```

Output:

```text
True
```

Truth concept:

```text
True  and True  → True
True  and False → False
False and True  → False
False and False → False
```

---

## or

At least ek condition true honi chahiye.

```python
age = 17

print(age < 18 or age > 60)
```

Output:

```text
True
```

---

## not

Boolean result ko reverse karta hai.

```python
is_logged_in = True

print(not is_logged_in)
```

Output:

```text
False
```

---

# 5.5 Membership Operators

Membership operators check karte hain ki koi value collection/string ke andar exist karti hai ya nahi.

Operators:

```text
in
not in
```

Example:

```python
name = "Python"

print("P" in name)
```

Output:

```text
True
```

---

```python
name = "Python"

print("z" not in name)
```

Output:

```text
True
```

---

# 5.6 Identity Operators

Identity operators check karte hain ki do references same object ko refer kar rahe hain ya nahi.

Operators:

```text
is
is not
```

Example:

```python
x = None

print(x is None)
```

Output:

```text
True
```

### Important

`==` aur `is` same nahi hain.

```text
==  → values compare karta hai
is  → object identity compare karta hai
```

---

# 5.7 Operator Precedence

Python expressions ko ek specific order me evaluate karta hai.

Basic order:

```text
1. ()
2. **
3. *, /, //, %
4. +, -
5. Comparison
6. not
7. and
8. or
```

Example:

```python
result = 10 + 5 * 2

print(result)
```

Output:

```text
20
```

Because multiplication pehle hota hai:

```text
5 * 2 = 10
10 + 10 = 20
```

Parentheses use karke order change kar sakte hain:

```python
result = (10 + 5) * 2

print(result)
```

Output:

```text
30
```

---

# 🧠 Important Concepts to Remember

## `=` vs `==`

```python
x = 10
```

`=` → value assign karta hai.

```python
x == 10
```

`==` → values compare karta hai.

---

## `/` vs `//`

```python
10 / 3
```

Output:

```text
3.3333333333333335
```

```python
10 // 3
```

Output:

```text
3
```

---

## `%`

```python
10 % 3
```

Output:

```text
1
```

Remainder deta hai.

---

## `input()`

```python
age = input("Enter age: ")
```

`age` string hoga.

Integer chahiye:

```python
age = int(input("Enter age: "))
```

---

# 🧪 Phase 1 Practice

## Basic Questions

### Q1. Create three variables

Create:

```text
name
age
city
```

and print them.

---

### Q2. Data Type

Find the type of:

```python
name = "Het"
age = 21
salary = 25000.50
is_student = True
```

---

### Q3. Type Conversion

Convert:

```text
"100" → int
100 → float
100 → string
99.99 → int
```

---

### Q4. User Input

Take:

```text
name
age
city
```

from user and print them.

---

### Q5. Calculator

Take two numbers from user and calculate:

```text
Addition
Subtraction
Multiplication
Division
Modulus
```

---

### Q6. Rectangle

Take:

```text
length
width
```

Calculate:

```text
Area
Perimeter
```

Formula:

```text
Area = length × width

Perimeter = 2 × (length + width)
```

---

### Q7. Average

Take three numbers and calculate their average.

```text
average = (a + b + c) / 3
```

---

### Q8. Check Even/Odd

Take a number and use `%` to understand whether it is even or odd.

> `if/else` implementation will be covered in the next phase.

---

### Q9. Comparison

Given:

```python
a = 20
b = 10
```

Find the result of:

```python
a > b
a < b
a == b
a != b
a >= b
a <= b
```

---

### Q10. Logical Operators

Given:

```python
age = 25
```

Understand the result of:

```python
age >= 18 and age <= 60
age < 18 or age > 60
not(age >= 18)
```

---

# 💻 Mini Project — Basic Calculator

```python
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)
print("Modulus:", num1 % num2)
```

---

# 🎯 Interview / Viva Questions

## Q1. What is a variable?

A variable is a name/reference used to store or refer to a value in Python.

---

## Q2. Is Python dynamically typed?

Yes.

Python me variable ka type explicitly declare karna required nahi hai.

```python
age = 21
```

Python automatically identifies it as `int`.

---

## Q3. What does input() return?

`input()` always returns a string.

```python
age = input("Enter age: ")
```

Even if user enters `21`, its type is `str`.

---

## Q4. Difference between `=` and `==`?

```text
=   → Assignment
==  → Comparison
```

---

## Q5. Difference between `/` and `//`?

```text
/  → Normal division
// → Floor division
```

---

## Q6. What does `%` do?

`%` returns the remainder of a division.

```python
10 % 3
```

Result:

```text
1
```

---

## Q7. What is type conversion?

Converting one data type into another.

Example:

```python
age = int("21")
```

---

## Q8. What is a Boolean?

Boolean represents either:

```text
True
False
```

---

## Q9. What is string slicing?

String ke ek specific portion ko extract karna.

```python
text = "Python"

print(text[0:3])
```

Output:

```text
Pyt
```

---

# 🔥 Phase 1 Quick Revision

```text
Comments
   ↓
Variables
   ↓
Data Types
   ↓
Strings
   ↓
Type Conversion
   ↓
Input
   ↓
Output
   ↓
Operators
```

---

# ✅ Phase 1 Completion Checklist

* [x] Comments
* [x] Variables
* [x] Variable Naming
* [x] Multiple Assignment
* [x] int
* [x] float
* [x] complex
* [x] str
* [x] bool
* [x] None
* [x] type()
* [x] String indexing
* [x] Negative indexing
* [x] String slicing
* [x] String methods
* [x] String concatenation
* [x] `len()`
* [x] Type conversion
* [x] `int()`
* [x] `float()`
* [x] `str()`
* [x] `bool()`
* [x] `print()`
* [x] `input()`
* [x] f-string
* [x] Arithmetic operators
* [x] Assignment operators
* [x] Comparison operators
* [x] Logical operators
* [x] Membership operators
* [x] Identity operators
* [x] Operator precedence

---

# 📊 Progress Checkpoint

**Phase:** 1
**Status:** ✅ Completed

**Main Topics Completed:** 5/5

```text
1. Comments & Variables       ✅
2. Data Types                 ✅
3. Strings & Type Conversion  ✅
4. Input & Output             ✅
5. Operators                  ✅
```

### Next Phase

# 🚀 Phase 2 — Conditional Statements & Loops

Planned topics:

```text
1. if
2. if-else
3. if-elif-else
4. Nested if
5. Logical conditions
6. for loop
7. while loop
8. break
9. continue
10. pass
11. Nested loops
12. Pattern problems
```

> **Phase 1 complete. Next starting point: Phase 2 — Conditional Statements.**
