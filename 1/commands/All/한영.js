const Inko = require('inko');
const inko = new Inko();

exports.run = async ({client, message, Ms}) => {
  try {

    await message.reply(inko.ko2en(Ms[0]));
    
  } catch (e) { await client.Error(e, message); }
};

exports.help = {
  '<한타>': '<한타>를 영타로 변환합니다.'
}
exports.permission = ['All'];
exports.MsLength = [1];
exports.name = ['.한영'];
