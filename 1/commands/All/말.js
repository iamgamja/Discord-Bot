exports.run = async ({client, message, Ms}) => {
  try {

    await message.reply(Ms[0]);
    
  } catch (e) { await client.Error(e, message); }
};

exports.help = {
  '<할말>': '<할말>을 말합니다.'
}
exports.permission = ['All'];
exports.MsLength = [1];
exports.name = ['.말'];
