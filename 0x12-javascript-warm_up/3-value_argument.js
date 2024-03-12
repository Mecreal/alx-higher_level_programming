#!/usr/bin/node
// Script that return all the args

const { argv } = require('node:process');

// print process.argv
argv.forEach((val, index) => {
  if (index > 1) {
    console.log(`${val}`);
  }
});
