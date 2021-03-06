function outCb(data) {
  console.log(data.toString());
}
function errCb(data) {
  console.error(data.toString());
  setTimeout(() => process.exit(0), 1000);
}

const {spawn} = require("child_process");

const process1 = spawn("node", ["/app/1/index.js"]);
process1.stdout.on("data", outCb);
process1.stderr.on("data", errCb);

const process2 = spawn("node", ["/app/2/index.js"]);
process2.stdout.on("data", outCb);
process2.stderr.on("data", errCb);

console.log('start');
