# Project: 0x13 JavaScript Objects, Scopes and Closures

## Task Descriptions

### 0. Rectangle #0
- **Objective**: Write an empty class `Rectangle` that defines a rectangle.
- **Requirements**: 
  - Use class notation for defining the class.
- **File**: `0-rectangle.js`

### 1. Rectangle #1
- **Objective**: Enhance `Rectangle` class to define a rectangle.
- **Requirements**: 
  - Constructor must take 2 arguments `w` and `h`.
  - Initialize `width` with `w` and `height` with `h`.
- **File**: `1-rectangle.js`

### 2. Rectangle #2
- **Objective**: Further enhance the `Rectangle` class.
- **Requirements**: 
  - Same as previous, plus:
  - Create an empty object if `w` or `h` is 0 or not a positive integer.
- **File**: `2-rectangle.js`

### 3. Rectangle #3
- **Objective**: Add a method to `Rectangle` class.
- **Requirements**: 
  - Same as previous, plus:
  - Instance method `print()` that prints the rectangle using the character `X`.
- **File**: `3-rectangle.js`

### 4. Rectangle #4
- **Objective**: Add more methods to `Rectangle` class.
- **Requirements**: 
  - Same as previous, plus:
  - Instance method `rotate()` to exchange `width` and `height`.
  - Instance method `double()` to multiply `width` and `height` by 2.
- **File**: `4-rectangle.js`

### 5. Square #0
- **Objective**: Define a class `Square` that inherits from `Rectangle`.
- **Requirements**: 
  - Use class notation and `extends`.
  - Constructor takes 1 argument: `size`.
  - Call `Rectangle` constructor with `size`.
- **File**: `5-square.js`

### 6. Square #1
- **Objective**: Enhance the `Square` class.
- **Requirements**: 
  - Inherits from `Square` of `5-square.js`.
  - Instance method `charPrint(c)` to print the square using character `c`. If `c` is undefined, use `X`.
- **File**: `6-square.js`

### 7. Occurrences
- **Objective**: Write a function to count occurrences in a list.
- **Prototype**: `exports.nbOccurences = function (list, searchElement)`
- **File**: `7-occurrences.js`

### 8. Esrever
- **Objective**: Write a function to reverse a list.
- **Prototype**: `exports.esrever = function (list)`
- **Restriction**: Do not use the built-in `reverse` method.
- **File**: `8-esrever.js`

### 9. Log me
- **Objective**: Write a function that logs arguments.
- **Prototype**: `exports.logMe = function (item)`
- **Format**: `<number of arguments already printed>: <current argument value>`
- **File**: `9-logme.js`

### 10. Number conversion
- **Objective**: Write a function to convert numbers from base 10.
- **Prototype**: `exports.converter = function (base)`
- **Restrictions**: 
  - No file imports.
  - No declaration of new variables (var, let, etc.).
- **File**: `10-converter.js`

