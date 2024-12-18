#!/usr/bin/node
// A Node.js interpreter

// An add function
function add(a, b) {
	return a + b;
}

// Perse the first and second args as integers
const a = parseInt(process.argv[2]);
const b = parseInt(process.argv[3]);

// Print result
console.log(add(a, b));
