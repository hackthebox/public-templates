![img](assets/banner.png)

<img src='assets/htb.png' style='zoom: 80%;' align=left /> <font size='10'><Challenge_Name></font>

1<sup>st</sup> August 2023

Prepared By: `<author_name>`

Challenge Author(s): `<author_name>`

Difficulty: <font color='orange'>Medium</font>

<br><br>

***NOTE : The headings with `(!)` should be necessarily included in your writeup while the ones with `(*)` are optional and should be included only if there is a need to. Of course, you can modify the content of each section accordingly. We just provide some boilerplate text.***

# Synopsis (!)

- Briefly explain what the user must do to solve this challenge.

## Description (!)

- ...

## Skills Required (!)

- Python
- Researching Skills
- C/C++
- Know how to use common RE tools (i.e. Ghidra, IDA)
- ...

## Skills Learned (!)

- Learn how SQLi works.
- Learn how to unpack executables.
- Learn how to solve linear systems of equations.
- ...

# Enumeration (!)

## Analyzing the source code (*)

- Explain what source files you are provided with when you unzip the challenge zip file.

Analyze the source files as much as you can so it is clear what the challenge is about.

...

If we look at `source.py`, we can see that our goal is:

- Specify the goal of the challenge (i.e. where the flag is and how it can be accessed)
- ...

The basic workflow of the script is as follows:

1. Method `test()` is called which then calls `test1()`
2. `test1()` creates an object of the `XXX` class which initializes `YYY`.
3. ...

A little summary of all the interesting things we have found out so far:

1. The PHP query handler does not use prepared statements.
2. The RSA modulo is generated with a non-standard way.
3. ...

# Solution (!)

## Finding the vulnerability (*)

Explain where the vulnerability is. Be as detailed as possible so there are no logical gaps as to how you figured out the vulnerability and how you will proceed to the solution.

## Exploitation (!)

### Connecting to the server (*)

Here is some boilerplate code for connecting to a docker-based challenge:

```python
if __name__ == "__main__":
    r = remote("0.0.0.0", 1337)
    pwn()
```

Let us consider our attack scenario.

1. ...
2. ...
3. ...

The attack explained above can be implemented with the following code:

```python
def important_function_that_does_something(param1, param2):
    <function_body>
```

### Getting the flag (!)

A final summary of all that was said above:

1.
2.

This recap can be represented by code using `pwn()` function:

```python
def pwn():
    pass
```

Avoid writing any function body here. Make sure you have written them under `Exploitation` or `Finding the vulnerability` sections.