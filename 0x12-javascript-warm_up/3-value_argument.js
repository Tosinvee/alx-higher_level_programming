#!/usr/bin/node

if (process.argv[2] !== undefined) {
  const firstArgument = process.argv[2];
  console.log('First argument:' + firstArgument);
} else {
  console.log('No argument');
}
