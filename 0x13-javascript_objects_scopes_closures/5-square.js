#!/usr/bin/node
const Rectangle = require('./4-rectangle.js');

class Square extends Rectangle {
  constructor (size) {
    super(size, size); // width and height will be equal to size.
  }
}

module.exports = Square;
