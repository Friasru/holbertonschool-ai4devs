## Bug 1 – bug1.py
**Intended Behavior**: Return the last n items of a list.
**Issue Type**: Off-by-one error.
**Notes**: Fails when n is bigger than the list length, which causes an IndexError.

## Bug 2 – bug2.js
**Intended Behavior**: Add up the prices of items in a cart.
**Issue Type**: Logical error.
**Notes**: Loop goes one step too far and one price is a string, which produces NaN.

## Bug 3 – bug3.py
**Intended Behavior**: Add an item to a basket and return it.
**Issue Type**: Runtime and logical error.
**Notes**: Using a mutable default argument makes the basket stay between calls.

## Bug 4 – bug4.c
**Intended Behavior**: Compute and print the square of a number.
**Issue Type**: Syntax error + pointer misuse.
**Notes**: Missing semicolon breaks the compilation and the pointer is never initialized.
