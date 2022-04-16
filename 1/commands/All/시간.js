exports.run = async ({client, message}) => {
  try {

    await message.reply(`현재 시간은 <t:${Math.round(Date.now()/1000)}:F> 입니다.`);
    
  } catch (e) { await client.Error(e, message); }
};

exports.help = {
  '': '현재 시간을 출력합니다.'
}
exports.permission = ['All'];
exports.MsLength = [0];
exports.name = ['.시간'];
