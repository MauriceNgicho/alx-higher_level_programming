#!/usr/bin/node
// A Node.js interpreter

// Retrieve the first argument and convert it to an integer
const size = parseInt(process.argv[2]);

// Check if size is a valid integer
if (isNaN(size)) {
	console.log('Missing size');
}	else if (size > 0) {
	// Loop to construct and print each row of the square
	for (let i = 0; i < size; i++) {
		console.log('X'.repeat(size));
	}
}

