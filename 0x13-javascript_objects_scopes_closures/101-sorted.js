#!/usr/bin/node
const dict = require('./101-data').dict;

// Create the new dictionary
const newDict = {};

for (const [userId, occurrence] of Object.entries(dict)) {
  if (!newDict[occurrence]) {
    newDict[occurrence] = [];
  }
  newDict[occurrence].push(userId);
}

// Print the new dictionary
console.log(newDict);
