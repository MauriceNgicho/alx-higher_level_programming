#!/usr/bin/node
// Shebang line to specify the Node.js interpreter for Unix-like environments

// Access the command-line arguments using `process.argv`
// The first two elements are: 
//   process.argv[0] -> Path to the Node.js binary
//   process.argv[1] -> Path to the script
const args = process.argv.slice(2);

// Check the number of arguments provided and print the corresponding message
if (args.length === 0) {
  console.log('No argument'); // If no arguments are passed
} else if (args.length === 1) {
  console.log('Argument found'); // If one argument is passed
} else {
  console.log('Arguments found'); // If more than one argument is passed
}
