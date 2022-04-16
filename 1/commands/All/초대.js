const { MessageActionRow, MessageButton } = require('discord.js');

exports.run = async ({client, message}) => {
  try {
    
		const row = new MessageActionRow()
    .addComponents(
      new MessageButton()
        .setLabel('초대하러 가기!')
        .setStyle('LINK')
        .setURL('https://discord.com/oauth2/authorize?&client_id=711729588543160330&scope=bot&permissions=8')
    );

    await message.reply({ components: [row] });

  } catch (e) { await client.Error(e, message); }
};

exports.help = {
  '': '이 봇의 초대링크를 확인합니다.'
}
exports.permission = ['All'];
exports.MsLength = [0];
exports.name = ['.초대'];
