#!/usr/bin/node
// inherit Square from Rectangle

import Rectangle from './4-rectangle';

export default class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}
