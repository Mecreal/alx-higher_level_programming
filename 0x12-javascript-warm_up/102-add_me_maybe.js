#!/usr/bin/node
// function that increments and calls a function.

function addMeMaybe (x, theFunction) {
  theFunction(x + 1);
}

module.exports = { addMeMaybe };
