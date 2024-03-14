#!/usr/bin/node
// inherit Square from square

module.exports = class Square extends require('./4-rectangle') {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c !== undefined && c != null) {
      for (let i = 0; i < this.height; i++) {
        console.log(c.repeat(this.height));
      }
    } else {
      this.print();
    }
  }
};
