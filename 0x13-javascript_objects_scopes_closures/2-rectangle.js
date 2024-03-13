#!/usr/bin/node
// a class Rectangle that defines a rectangle

module.exports = class Rectangle {
	constructor (w, h) {
    if(w <= 0 || isNaN(w) || h <= 0 || isNaN(h)) {

    } else {
      this.width = w;
      this.height = h;
    }
  }
};
