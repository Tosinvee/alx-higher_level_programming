#!/usr/bin/node
const number = Number(process.argv[2]);
function factorial (number) {
  if (number === 0 || Number.isNaN(number)) return 1;
  return number * factorial(number - 1);
}
console.log(factorial(number));
