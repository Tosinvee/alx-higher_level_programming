#!/usr/bin/node

if (process.argv[2] !== undefined) {
  const firstArgument = process.argv[2];
  console.log('First Argument:' + firstArgument);
} else {
  console.log('No argument');
}
