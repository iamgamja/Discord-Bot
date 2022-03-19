exports.run = async ({client, message}) => {
  try {

    await message.reply('https://discord.com/oauth2/authorize?&client_id=711729588543160330&scope=bot&permissions=8');
    
  } catch (e) { await client.Error(e, message); }
};

exports.help = {
  '': '이 봇의 초대링크를 확인합니다.'
}
exports.permission = ['All'];
exports.MsLength = [0];
exports.name = ['.초대'];
