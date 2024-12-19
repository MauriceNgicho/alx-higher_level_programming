#!/usr/bin/node

// A function that increments a number and calls another function
exports.addMeMaybe = function (number, theFunction) {
  theFunction(number + 1);
};
