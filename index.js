const spawn = require("child_process").spawn;

const process1 = spawn("node", ["/app/1/index.js"]);
const process2 = spawn("node", ["/app/2/index.js"]);
const process3 = spawn("python", ["/app/3/index.py"]);


process1.stdout.on("data", function (data) {
  console.log(data.toString());
});
process2.stdout.on("data", function (data) {
  console.log(data.toString());
});
process3.stdout.on("data", function (data) {
  console.log(data.toString());
});


process1.stderr.on("data", function (data) {
  console.error(data.toString());
  throw Error('kill');
});
process2.stderr.on("data", function (data) {
  console.error(data.toString());
  throw Error('kill');
});
process3.stderr.on("data", function (data) {
  console.error(data.toString());
  throw Error('kill');
});

console.log('start');
