#!/usr/bin/node

// Define a function that executes another function x times
exports.callMeMoby = function (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
};
