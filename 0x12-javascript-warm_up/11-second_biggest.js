#!/usr/bin/node
if (!process.argv[2] || !process.argv[3]) {
  console.log(0);
} else {
  const args = process.argv.slice(2);
  const intArgs = args.sort((i, j) => i - j);
  console.log(intArgs[intArgs.length - 2]);
}
