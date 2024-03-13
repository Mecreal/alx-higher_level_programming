#!/usr/bin/node
// argv2 times C is fun

const { argv } = require('node:process');

const number = parseInt(argv[2], 10);
if (isNaN(number)) {
  console.log('Missing number of occurrences');
} else if (number > 0) {
  for (let i = 0; i < number; i++) {
    console.log('C is fun');
  }
}
