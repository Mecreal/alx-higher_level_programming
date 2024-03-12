#!/usr/bin/node
//  script that prints My number: <first argument converted in integer>
// if the first argument can be converted to an integer

const { argv } = require('node:process');

const number = parseInt(argv[2], 10);
if (isNaN(number)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${number}`);
}
