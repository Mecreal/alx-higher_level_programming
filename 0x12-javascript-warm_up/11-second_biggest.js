#!/usr/bin/node
// Search the second biggest

const { argv } = require('node:process');

if (argv.length <= 3) {
  console.log(0);
} else {
  const l = argv.sort();
  console.log(l.reverse()[1]);
}
