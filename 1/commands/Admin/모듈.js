const childProcess = require('child_process');

const exec = (c) => {
  return new Promise((resolve, reject) => {

    const process = childProcess.exec(c);

    process.stdout.on("data", function (data) {
      resolve(data.toString());
    });

    process.stderr.on("data", function (data) {
      reject(data.toString());
    });

  });
}


exports.run = async ({client, message, Ms}) => {
  try {

    await exec(`npm i ${Ms[0]}`);
    await message.reply(`\`${Ms[0]}\`를 성공적으로 불러왔습니다!`);
  
  } catch (e) { await client.Error(e, message); }
};

exports.help = {
  '<모듈 이름>': '<모듈 이름>을 불러옵니다.'
}
exports.permission = ['Admin'];
exports.MsLength = [1];
exports.name = ['.모듈'];
