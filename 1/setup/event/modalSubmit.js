module.exports = async (client) => {
  client.on('modalSubmit', async (modal) => {
    try {

      if (modal.customId === 'loginModal'){
        const id = modal.getTextInputValue('idTextInput');
        const password = modal.getTextInputValue('passwordTextInput');
        await modal.reply(`로그인에 성공하였스빈다!(아님)\n아이디: \`${id.length>100 ? id.slice(0,100)+'...' : id}\`\n비밀번호: \`${password.length>100 ? password.slice(0,100)+'...' : password}\``)
      }  

    } catch (e) { await client.Error(e); }
  })
}
