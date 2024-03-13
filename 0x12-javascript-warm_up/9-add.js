#!/usr/bin/node
// add two numbers

const { argv } = require('node:process');

const n1 = parseInt(argv[2], 10);
const n2 = parseInt(argv[3], 10);

console.log(n1 + n2);
