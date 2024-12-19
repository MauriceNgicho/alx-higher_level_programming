#!/usr/bin/node
// Shebang to specify the Node.js interpreter

// Function to compute factorial recursively
function factorial (n) {
  if (isNaN(n) || n <= 0) {
    return 1; // Base case: factorial of NaN or 0 is 1
  }
  return n * factorial(n - 1);
}

// Parse the first argument as an integer
const num = parseInt(process.argv[2]);

// Compute and print the factorial
console.log(factorial(num));
