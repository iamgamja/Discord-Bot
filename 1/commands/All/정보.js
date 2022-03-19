exports.run = async ({client, message}) => {
  try {

    let d=require("discord.js");await message.reply({embeds:[(new d.MessageEmbed).setTitle("open_file_folder 라이브러리").setFields(require("child_process").execSync("npm list",{encoding:"utf-8"}).split("\n").slice(1).map((e,s)=>e.slice(4).split("@")).map((e,s)=>e[1]&&{name:e[0],value:e[1]}).filter(e=>void 0!==e)).setColor(0x55abed)]})
  
  } catch (e) { await client.Error(e, message); }
};

exports.help = {
  '': '이 봇에 대한 정보를 출력합니다.\n\n이 명령어는 <@536517275667267605> (@ppapman1#6448) 님이 만들어줬대요! (약간 수정함)'
}
exports.permission = ['All'];
exports.MsLength = [0];
exports.name = ['.정보'];
