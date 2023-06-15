#!/usr/bin/bash
const multiPrint = Number(process.argv[2]);
if (Number.isNaN(multiPrint)) {
  console.log('Missing number of occurrences');
  process.exit();
}
for (let i = 0; i < multiPrint; i++) {
  console.log('C is fun');
}
