exports.run = async ({client, message}) => {
  try {

    await message.reply(`<@!${message.author.id}> (${client.ws.ping}ms)`);
    
  } catch (e) { await client.Error(e, message); }
};

exports.help = {
  '': '핑을 합니다(?).'
}
exports.permission =['All'];
exports.MsLength = [0];
exports.name = ['.핑'];
