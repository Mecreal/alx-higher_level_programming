#!/usr/bin/node
// inherit Square from square

const Square5 = require('./4-rectangle');

module.exports = class Square extends Square5 {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c !== undefined) {
      for (let i = 0; i < this.height; i++) {
        console.log(c.repeat(this.height));
      }
    } else {
      super.print();
    }
  }
};
