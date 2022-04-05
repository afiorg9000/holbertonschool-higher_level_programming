#!/usr/bin/node

module.exports = class Rectangle {
  constructor (width, height) {
    if (width > 0 && height > 0) {
      this.width = width;
      this.height = height;
    }
}

print () {
  for (let idx = 0; idx < this.height; idx++) {
    console.log('X'.repeat(this.width));
  }
}
}
