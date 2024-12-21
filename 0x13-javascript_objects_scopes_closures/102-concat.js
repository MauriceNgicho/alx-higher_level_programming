#!/usr/bin/node
const fs = require('fs');

// Retrieve command-line arguments
const [,, fileA, fileB, fileC] = process.argv;

try {
  // Read content from fileA and fileB
  const dataA = fs.readFileSync(fileA, 'utf-8');
  const dataB = fs.readFileSync(fileB, 'utf-8');

  // Concatenate and write to fileC
  fs.writeFileSync(fileC, dataA + dataB);
} catch (error) {
  console.error(`Error: ${error.message}`);
}
