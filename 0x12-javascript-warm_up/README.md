# Project: 0x12 JavaScript Warm Up

This project includes a series of JavaScript scripting tasks to practice basic concepts.

## Table of Contents

1. [First Constant, First Print](#first-constant-first-print)
2. [3 Languages](#3-languages)
3. [Arguments](#arguments)
4. [Value of My Argument](#value-of-my-argument)
5. [Create a Sentence](#create-a-sentence)
6. [An Integer](#an-integer)
7. [Loop to Languages](#loop-to-languages)
8. [I Love C](#i-love-c)
9. [Square](#square)
10. [Add](#add)
11. [Factorial](#factorial)
12. [Second Biggest!](#second-biggest)
13. [Object](#object)
14. [Add File](#add-file)

---

### First Constant, First Print

- **Task**: Write a script that prints "JavaScript is amazing".
- **Details**:
  - Constant variable `myVar` with the value "JavaScript is amazing".
  - Use `console.log(...)` for printing.
- **Constraints**: Do not use `var`.
- **File**: `0-javascript_is_amazing.js`

### 3 Languages

- **Task**: Script to print three lines about different programming languages.
- **Output**:
  - First line: “C is fun”
  - Second line: “Python is cool”
  - Third line: “JavaScript is amazing”
- **Constraints**: Use `console.log(...)`, and do not use `var`.
- **File**: `1-multi_languages.js`

### Arguments

- **Task**: Print messages based on the number of arguments passed.
- **Output**:
  - No arguments: “No argument”
  - One argument: “Argument found”
  - More than one: “Arguments found”
- **Reference**: `process.argv`
- **Constraints**: Use `console.log(...)`, and do not use `var`.
- **File**: `2-arguments.js`

### Value of My Argument

- **Task**: Print the first argument passed to the script.
- **Output**: "No argument" if none are passed.
- **Constraints**: Use `console.log(...)`, do not use `var` or `length`.
- **File**: `3-value_argument.js`

### Create a Sentence

- **Task**: Script that prints two arguments in a specific format.
- **Output**:
  - Format: “<arg1> is <arg2>”
  - Handle cases with missing arguments.
- **Constraints**: Use `console.log(...)`, do not use `var`.
- **File**: `4-concat.js`

### An Integer

- **Task**: Print "My number: <arg>" if the argument can be converted to an integer.
- **Output**: "Not a number" if the argument cannot be converted.
- **Constraints**: Use `console.log(...)`, do not use `var` or `try/catch`.
- **File**: `5-to_integer.js`

### Loop to Languages

- **Task**: Use an array and loop to print lines about languages.
- **Output**:
  - “C is fun”
  - “Python is cool”
  - “JavaScript is amazing”
- **Constraints**: Use `console.log(...)`, no `var`, no `if/else`, only one `console.log` in the loop.
- **File**: `6-multi_languages_loop.js`

### I Love C

- **Task**: Print “C is fun” x times, where x is the first script argument.
- **Output**: “Missing number of occurrences” if x can't be converted to an integer.
- **Constraints**: Use `console.log(...)`, no `var`, only two `console.log`.
- **File**: `7-multi_c.js`

### Square

- **Task**: Print a square using the `X` character.
- **Details**: The first argument is the square's size.
- **Output**: “Missing size” if the size can't be converted to an integer.
- **Constraints**: Use `console.log(...)`, no `var`.
- **File**: `8-square.js`

### Add

- **Task**: Print the addition of 2 integers.
- **Function**: `function add(a, b)`
- **Output**: Handles cases with missing or non-integer arguments.
- **Constraints**: Use `console.log(...)`, no `var`.
- **File**: `9-add.js`

### Factorial

- **Task**: Compute and print a factorial.
- **Details**: Handle NaN and infinity cases.
- **Constraints**: Recursive function, `console.log(...)`, no `var`.
- **File**: `10-factorial.js`

### Second Biggest!

- **Task**: Find the second biggest integer in arguments.
- **Output**: 
  - 0 if no or one argument.
  - Second largest number otherwise.
- **Constraints**: Use `console.log(...)`, no `var`.
- **File**: `11-second_biggest.js`

### Object

- **Task**: Update script to change a value in an object.
- **Details**: Replace value 12 with 89.
- **Constraints**: No `var`.
- **File**: `12-object.js`

### Add File

- **Task**: Write a function that returns the addition of 2 integers.
- **Details**: Function must be visible from outside and named `add`.
- **Constraints**: No `var`.
- **Usage Example**: `const add = require('./13-add').add;`
- **File**: `13-add.js`

