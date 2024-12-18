#!/usr/bin/node
// Shebang to specify the Node.js interpreter

// Extract arguments from the command line
const args = process.argv.slice(2).map(Number);

// Check if there are fewer than two arguments
if (args.length <= 1) {
  console.log(0); // Print 0 if no or only one argument
} else {
  // Sort the array in descending order and get the second biggest
  args.sort((a, b) => b - a);
  console.log(args[1]);
}
