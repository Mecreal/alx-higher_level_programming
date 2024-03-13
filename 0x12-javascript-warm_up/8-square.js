#!/usr/bin/node
// a squar of argv2 times #

const { argv } = require('node:process');

const number = parseInt(argv[2], 10);
if (isNaN(number)) {
  console.log('Missing size');
} else if (number > 0) {
  for (let i = 0; i < number; i++) {
      console.log('X'.repeat(number));
  }
}
