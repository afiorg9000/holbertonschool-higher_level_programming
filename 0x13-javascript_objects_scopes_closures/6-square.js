#!/usr/bin/node

module.exports = class Square extends require('./5-square.js') {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let idx = 0; idx < this.height; idx++) {
        console.log(c.repeat(this.width));
      }
    }
  }
};
