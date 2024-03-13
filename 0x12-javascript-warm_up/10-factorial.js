#!/usr/bin/node
// facorial

const { argv } = require('node:process');

const n1 = parseInt(argv[2], 10);

function facorial (n) {
  if ((isNaN(n)) || (n === 1)) {
    return 1;
  } else {
    return n * facorial(n - 1);
  }
}

console.log(facorial(n1));
