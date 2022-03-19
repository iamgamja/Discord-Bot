exports.run = async () => {
  setTimeout( ()=>{throw '봇죽이기'} )
};

exports.help = {
  '': '봇을 죽입니다!'
}
exports.permission = ['Admin'];
exports.MsLength = [0];
exports.name = ['.kill'];
