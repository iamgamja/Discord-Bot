const fs = require('fs');
fs.RF=(e=>new Promise((f,i)=>{fs.readFile(e,"utf8",function(e,n){e?i(e):f(n)})}));

module.exports = async (client) => {
  client.on("interactionCreate", async (interaction) => {
    try {
  
      if (!interaction.isCommand()) return;
  
      switch (interaction.commandName) {
        case 'archive':
          if (!interaction.member.roles.cache.some(role => role.id === '843811717786894366')) return; // 관리자가아니면 실행하지 않음.
          let channel = interaction.options.getChannel('채널');
          await channel.setParent('843817967312568321');
          await channel.lockPermissions();
          await interaction.reply(`<@${interaction.user.id}>, <#${channel.id}>을(를) 아카이브로 옮겼습니다.`);
          break;
        case 'ping':
          await interaction.reply('pong!')
          break;
        case 'eval':
          await interaction.deferReply();
          try {
  
            const run_msg = `async (client) => { \n ${interaction.options.getString('코드')} \n }`;
            const result_func = eval(run_msg);
            const result = await result_func(client);
            await interaction.editReply(''+ result);
  
          } catch (e) { await client.Error(e) }
          break;
        case 'template':
          if (!interaction.member.roles.cache.some(role => role.id === '843811717786894366')) return; // 관리자가아니면 실행하지 않음.
          await interaction.deferReply();
          let isSubcommandGroup;
          try {
            interaction.options.getSubcommandGroup();
            isSubcommandGroup = true;
          } catch {
            isSubcommandGroup = false;
          }
          if (!isSubcommandGroup) { // sub command group이 없을 경우
            switch (interaction.options.getSubcommand()) {
              case 'help': {
                const helpMsg = await fs.RF('/app/2/data/helpMsg.txt');
                await interaction.editReply(helpMsg);
                break;
              } case 'create': {
                await client.db.add(['template', interaction.options.getString('templatename')], {});
                await interaction.editReply(`\`${interaction.options.getString('templatename')}\` 템플릿을 생성했습니다.`)
                break;
              } case 'apply': {
                let data = ( await client.db.get() ).template[interaction.options.getString('templatename')];
                for (let channelId in data) {
                  try {
                    await client.channels.cache.get(channelId).setName(data[channelId], `${interaction.options.getString('templatename')} 템플릿 적용`);
                  } catch { async (e) => await interaction.followUp(`<#${channelId}> 채널의 이름을 바꾸는데 실패했습니다`) }
                }
                await interaction.editReply(`\`${interaction.options.getString('templatename')}\` 템플릿의 적용이 완료되었습니다!`);
                break;
              } case 'default': {
                let data = {};
                await client.guilds.cache.get('843811221433352214').channels.cache.forEach(channel => {data[channel.id] = channel.name});
                await client.db.add(['template', interaction.options.getString('templatename')], data);
                await interaction.editReply(`\`${interaction.options.getString('templatename')}\` 템플릿의 설정이 완료되었습니다.`);
                break;
              } case 'reset': {
                await client.db.init();
                await interaction.editReply('템플릿을 초기화했습니다.');
                break;
              } case 'remove': {
                await client.db.remove(['template', interaction.options.getString('templatename')]);
                await interaction.editReply(`\`${interaction.options.getString('templatename')}\` 템플릿을 삭제했습니다.`)
                break;
              } case 'list': {
                let data = Object.keys(( await client.db.get() ).template).join('\n');
                let result = `템플릿 목록:\n${data}`;
                await interaction.editReply(result);
                break;
              }
            }
          } else { // sub command group이 있을 경우
            switch (interaction.options.getSubcommandGroup()) {
              case 'channel': {
                switch (interaction.options.getSubcommand()) {
                  case 'add': {
                    await client.db.add(['template', interaction.options.getString('templatename'), interaction.options.getChannel('채널').id], interaction.options.getString('이름') )
                    await interaction.editReply(`\`${interaction.options.getString('templatename')}\` 템플릿에 <#${interaction.options.getChannel('채널').id}> -> \`${interaction.options.getString('이름')}\`을(를) 등록했습니다.`)
                    break;
                  } case 'remove': {
                    await client.db.remove(['template', interaction.options.getString('templatename'), interaction.options.getChannel('채널').id])
                    await interaction.editReply(`\`${interaction.options.getString('templatename')}\` 템플릿에서 <#${interaction.options.getChannel('채널').id}>을(를) 삭제했습니다.`)
                    break;
                  } case 'list': {
                    let data = ( await client.db.get() ).template[interaction.options.getString('templatename')];
                    let result = `\`${interaction.options.getString('templatename')}\` 템플릿의 채널 목록:\n`;
                    for (let channelId in data) {
                      if ((result+`<#${channelId}> -> \`${data[channelId]}\`\n`).length > 2000) {
                        await interaction.followUp(result);
                        result = '';
                      }
                      result += `<#${channelId}> -> \`${data[channelId]}\`\n`;
                    }
                    if (result) await interaction.followUp(result);
                  }
                }
              }
            }
          }
        break;
      }
    } catch (e) { await client.Error(e) }
  });
}