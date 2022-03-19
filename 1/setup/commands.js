const Discord = require('discord.js');
const fs = require('fs');
const Inko = require('inko');
const inko = new Inko();

module.exports = async (client) => {
  client.commands = new Discord.Collection();

  for (const folder of fs.readdirSync('/app/1/commands')) {
    for (const file of fs.readdirSync(`/app/1/commands/${folder}`)) {
      const cmd = require(`/app/1/commands/${folder}/${file}`);
      const setCmd = {
        run: cmd.run,
        help: cmd.help,
        permission: cmd.permission,
        MsLength: cmd.MsLength,
        name: [...cmd.name], // [ '.게임', '업다운' ]
        nameS: [...cmd.name].join(' '), // '.게임 업다운'
        nameSD: [...cmd.name].join(' ').startsWith('.') ? [...cmd.name].join(' ').slice(1) : [...cmd.name].join(' '), // '게임 업다운'
        nameL: [...cmd.name].length, // 2
        match(s, allowWithoutPrefix) {
          const userStr = s.split(' ').slice(0, this.nameL).join(' ');
          return allowWithoutPrefix ?
            inko.ko2en(this.nameS) === inko.ko2en(userStr) || inko.ko2en(this.nameSD) === inko.ko2en(userStr) :
            inko.ko2en(this.nameS) === inko.ko2en(userStr);
        }
      }
      client.commands.set(cmd.name.join(' '), setCmd);
    }
  }
}