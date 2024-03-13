#!/usr/bin/node
// execute x time te function theFunction

function callMeMoby (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
}

module.exports = { callMeMoby };
