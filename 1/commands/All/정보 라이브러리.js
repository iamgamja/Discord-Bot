exports.run = async ({client, message}) => {
  try {

    let d=require("discord.js");await message.reply({embeds:[(new d.MessageEmbed).setTitle("open_file_folder 라이브러리").setFields(require("child_process").execSync("npm list",{encoding:"utf-8"}).split("\n").slice(1).filter(x=>x).map(e=>e.slice(4).split(/(?<!^)@/)).map(e=>({name:e[0],value:e[1]}))).setColor(0x55abed)]})
  
  } catch (e) { await client.Error(e, message); }
};

exports.help = {
  '': '이 봇이 사용하는 라이브러리에 대한 정보를 출력합니다.\n\nCode by @ppapman1#6448 (<@536517275667267605>), edited.'
}
exports.permission = ['All'];
exports.MsLength = [0];
exports.name = ['.정보', '라이브러리'];
