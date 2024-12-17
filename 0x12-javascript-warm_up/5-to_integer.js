#!/usr/bin/node
// Shebang line to specify the Node.js.

// Access the first argument from the command line
const arg = process.argv[2];

// Convert the argument to an integer
const number = parseInt(arg);

// Check if the conversion resulted in a valid number
if (!isNaN(number)) {
  console.log(`My number: ${number}`); // If valid, print the number
} else {
  console.log('Not a number'); // If not valid, print "Not a number"
}
