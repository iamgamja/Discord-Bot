module.exports = async (client) => {
  client.Error = async (e, message=null) => {
    await client.log('ERROR!(<@!526889025894875158>)...', '```js', '<name>', e.name, '<message>', e.message, '<stack>', e.stack, '```');
    if (message) client.log('`in`', message.guild.name, message.channel.name, message.url);
  }
}