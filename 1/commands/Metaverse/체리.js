exports.run = async ({message}) => {
  try {

    await message.reply('체바리보');
    
  } catch (e) { await client.Error(e, message); }
};

exports.help = {
  '': '<@767767226131677224> (샷다#4400) 님의 `ㅋ상점 구매`로 만들어졌습니다.'
}
exports.permission = ['Metaverse', 'Talk'];
exports.MsLength = [0];
exports.name = ['체리'];
