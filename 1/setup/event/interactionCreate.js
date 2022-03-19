const { Modal, TextInputComponent, showModal } = require('discord-modals') // Now we extract the showModal method

const modal = new Modal()
  .setCustomId('loginModal')
  .setTitle('로그인')
  .addComponents(
    new TextInputComponent()
      .setCustomId('idTextInput')
      .setLabel('아이디:')
      .setStyle('SHORT')
      .setMinLength(2)
      .setMaxLength(2000)
      .setPlaceholder('아이디를 입력해주세요.')
      .setRequired(true)
  ).addComponents(
    new TextInputComponent()
      .setCustomId('passwordTextInput')
      .setLabel('비밀번호:')
      .setStyle('SHORT')
      .setMinLength(8)
      .setMaxLength(2000)
      .setPlaceholder('비밀번호를 입력해주세요.')
      .setRequired(true)
  );

module.exports = async (client) => {
  client.on('interactionCreate', async (interaction) => {
    try {
      
      if (interaction.isButton()) {
        if (interaction.customId === 'modalButton') {
          showModal(modal, {
            client: client,
            interaction: interaction
          });
        }
      }
      
    } catch (e) { await client.Error(e); }
    
  });
}
