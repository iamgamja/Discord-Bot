const Inko = require('inko');
const inko = new Inko();

exports.run = async ({client, message, Ms}) => {
  try {

    await message.reply(inko.en2ko(Ms[0]));
  
  } catch (e) { await client.Error(e, message); }
};

exports.help = {
  '<영타>': '<영타>를 한타로 변환합니다.'
}
exports.permission = ['All'];
exports.MsLength = [1];
exports.name = ['.영한'];
