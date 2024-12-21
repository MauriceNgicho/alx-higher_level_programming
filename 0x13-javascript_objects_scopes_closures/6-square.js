#!/usr/bin/node
const prevSquare = require('./5-square.js');

class Square extends prevSquare {
  charPrint (c) {
    const char = c || 'x';
    for (let i = 0; i < this.height; i++) {
      console.log(char.repeat(this.width));
    }
  }
}

module.exports = Square;
