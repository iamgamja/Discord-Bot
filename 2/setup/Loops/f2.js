Math.sum = (...arr) => arr.reduce((a,b)=>a+b, 0);

module.exports = async (client) => {
  client.TongGye.f2 = async () => {
    try {
  
      const countMsg = async (channel, lastMsgId=null) => {
        try {
  
          let messages_ = await channel.messages.fetch({limit: 100, before: lastMsgId}, {forse: true}); // 캐시X
          let messages = messages_.filter(m => m.createdTimestamp >= Date.now()-60*60*1000);
  
          if (messages.size === 100) // 더 있을수도 있음
            return 100 + await countMsg(channel, messages.last().id);
          else
            return messages.size;
  
        } catch(e) { await client.Error(e) }
      }
  
      let data = [];
  
      let guild = client.guilds.cache.get('843811221433352214');
      let channels = [...guild.channels.cache.filter(c => c.type === 'GUILD_TEXT').values()];
  
      for (let channel of channels) {
        data.push(  await countMsg(channel)  );
      }
  
      const result = Math.sum(...data);
      return [result];
  
    } catch(e) { await client.Error(e) }
  }
}
