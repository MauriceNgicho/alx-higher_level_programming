#!/usr/bin/node
const list = require('./100-data').list;

// Print the initial list
console.log(list);

// Compute a new list using map
const newList = list.map((value, index) => value * index);

// Print the new list
console.log(newList);
