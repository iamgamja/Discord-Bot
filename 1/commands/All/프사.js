exports.run = async ({client, message, Ms}) => {
  try {

    const userOrMember = (()=>{
      if (Ms[0]) {
        return message.mentions.members.first() || // Case 1: member mention
          message.mentions.users.first() || // Case 2: user mention
          message.guild.members.cache.get(Ms[0].match(/(\d{18})/)?.[1]) || // Case 3: member id
          client.users.cache.get(Ms[0].match(/(\d{18})/)?.[1]) || // Case 4: user id
          message.guild.members.cache.find(u => u.displayName === Ms[0]) || // Case 5: member name
          client.users.cache.find(u => u.username === Ms[0]) || // Case 6: user name
          message.author; // Case 7: wrong input => self
      } else {
        return message.author; // Case 8: no input => self
      }
    })();

    const avatarUrl = userOrMember.displayAvatarURL({
      format: 'png',
      size: 4096,
      dynamic: true
    });


    await message.reply(avatarUrl);
    
  } catch (e) { await client.Error(e, message); }
};

exports.help = {
  '': '자신의 프사를 출력합니다.',
  '<mention | id | name>': '해당하는 유저의 프사를 출력합니다.'
}
exports.permission = ['All'];
exports.MsLength = [0, 1];
exports.name = ['.프사'];
