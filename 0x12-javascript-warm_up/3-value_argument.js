#!/usr/bin/node
// Shebang line to specify the Node.js interpreter for Unix-like environments

const arg = process.argv[2];

// Check if an argument exists at index 2
if (arg === undefined) {
  console.log('No argument'); // Print this if no arguments are passed
} else {
  console.log(arg); // Print the first argument
}
