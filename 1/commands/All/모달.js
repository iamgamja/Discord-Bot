const { MessageActionRow, MessageButton } = require('discord.js');

exports.run = async ({client, message}) => {
  try {

    const row = new MessageActionRow()
      .addComponents(
        new MessageButton()
          .setCustomId('modalButton')
          .setLabel('버튼튼')
          .setStyle('PRIMARY'),
      );

    await message.reply({
      content: "버튼 를 클릭해보세요",
      components: [row],
    });

  } catch (e) { await client.Error(e, message); }
};

exports.help = {
  '': '모달창을 만듭니다.\n로그인하는컨셉임!'
}
exports.permission = ['All'];
exports.MsLength = [0];
exports.name = ['.모달'];
