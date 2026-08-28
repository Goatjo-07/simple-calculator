# simple-calculator
A simple calculator built in Python as my first project.

## Code Explanation
- `float()` for inputs: I used `float()` so the calculator can handle both whole numbers and decimals, not just integers.  
- `if/elif/else` structure: This makes the program easy to read and ensures only one branch runs:
  - `if`: checks the first condition.  
  - `elif`: checks other possible operations one by one.  
  - `else`: catches invalid inputs so the program won’t break.  
- Division by zero check: I added `if num2 != 0` to prevent crashes and give a clear error message.  
- Error messages: Instead of letting Python throw confusing errors, I return friendly messages like `"Error: Division by zero"` or `"Error: Invalid operation"`.  
