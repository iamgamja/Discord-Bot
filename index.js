const spawn = require("child_process").spawn;

const process1 = spawn("node", ["/app/1/index.js"]);
const process2 = spawn("node", ["/app/2/index.js"]);


process1.stdout.on("data", function (data) {
  console.log(data.toString());
});
process2.stdout.on("data", function (data) {
  console.log(data.toString());
});


process1.stderr.on("data", function (data) {
  console.error(data.toString());
});
process2.stderr.on("data", function (data) {
  console.error(data.toString());
});

console.log('start');
