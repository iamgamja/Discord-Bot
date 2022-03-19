const { MessageEmbed } = require('discord.js');

const Inko = require('inko');
const inko = new Inko();

const Permission = require('/app/1/data/Permission');

const colors = '36393f b7e6aa ffffff 1f1e33 fece51 37fe3a cafe24 ad0fa1 accede abcdef fedcba c0ffee 0ff1ce f01ded ffae63 a1d76b'.split(' ');
const randomColor = () => '#' + colors[Math.floor(Math.random()*colors.length)];

exports.run = async ({client, message, Ms}) => {
  try {

    const embed = new MessageEmbed()
    .setTitle('도움말!')
    .setColor(randomColor());
    
    if (Ms[0]) { // 명령어의 자세한 도움말
      const cmd = client.commands.find(command => {
        return command.match(Ms[0], true);
      });
      if (cmd) { // 명령어가 있음

        const checkPermissionData = {
          cmd: cmd,
          client: client,
          message: message,
        }

        if ( Permission(cmd.permission, checkPermissionData) ) { // 권한 있음
          embed.setDescription(`\`${cmd.nameSD}\`의 자세한 도움말입니다!`);
          embed.addFields(
            ...Object.entries(cmd.help) // [['매개변수', '설명'], ...]
              .sort((a,b) => a[0].length - b[0].length) // [['매개변수', '설명'], ...] (정렬됨)
              .map(a => ({name: `${cmd.nameS} ${a[0]}`, value: a[1]}))
          );
        } else { // 권한 없음
          embed.setDescription(`\`${cmd.nameSD}\`의 자세한 도움말을 볼 권한이 없습니다.`);
        }

      } else { // 명령어가 없음
        embed.setDescription(`\`${Ms[0]}\`(이)라는 명령어를 찾을 수 없습니다.`);
      }
    } else { // 기본 도움말

      const checkPermissionData = {
        // cmd: cmd,
        client: client,
        message: message,
      }

      embed.setDescription('`.도움 <명령어>`로 자세한 도움말을 확인할수 있습니다!');
      /* if (Permission(['All'], checkPermissionData)) */  embed.addField('명령어 목록:',                client.commands.filter(c => c.permission.includes('All'))       .map(c => '`'+c.nameSD+'`').join(' '));
      if (Permission(['Admin'], checkPermissionData))      embed.addField('관리자 전용 명령어 목록:',    client.commands.filter(c => c.permission.includes('Admin'))     .map(c => '`'+c.nameSD+'`').join(' '));
      if (Permission(['RankServer'], checkPermissionData)) embed.addField('랭크 서버 전용 명령어 목록:', client.commands.filter(c => c.permission.includes('RankServer')).map(c => '`'+c.nameSD+'`').join(' '));
      if (Permission(['Metaverse'], checkPermissionData))  embed.addField('메타버스 전용 명령어 목록:',  client.commands.filter(c => c.permission.includes('Metaverse')) .map(c => '`'+c.nameSD+'`').join(' '));
      /* if (Permission(['Talk'], checkPermissionData)) */ // embed.addField('대화 명령어 목록:', client.commands.filter(c => c.permission.includes('Talk')).map(c => '`'+c.nameSD+'`').join(' '));
      
    }

    await message.reply({embeds: [embed]});
  
  } catch (e) { await client.Error(e, message); }
};

exports.help = {
  '': '도움말을 확인합니다.',
  '<명령어>': '<명령어>의 자세한 도움말을 확인합니다.'
}
exports.permission = ['All'];
exports.MsLength = [0, 1];
exports.name = ['.도움'];
