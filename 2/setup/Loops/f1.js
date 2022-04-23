Math.sum = (...arr) => arr.reduce((a,b)=>a+b, 0);

module.exports = async (client) => {
  client._.TongGye.f1 = async () => {
    try { 
  
      let dataNum = {
        user: {  online: 0,  idle: 0,  dnd: 0,  offline: 0  },
        bot:  {  online: 0,  idle: 0,  dnd: 0,  offline: 0  },
      }
  
      client.guilds.cache.get('843811221433352214').members.cache.map(m => {
        dataNum[!m.user.bot ? 'user' : 'bot'][m.presence?.status ? m.presence?.status : 'offline'] += 1;
      });
  
      let data = [
        Math.sum(...Object.values(dataNum.user)), // 유저 합계
        dataNum.user.online,
        dataNum.user.idle,
        dataNum.user.dnd,
        dataNum.user.offline,
        Math.sum(...Object.values(dataNum.bot)), // 봇 합계
        dataNum.bot.online,
        dataNum.bot.idle,
        dataNum.bot.dnd,
        dataNum.bot.offline
      ]
      
      return data;
  
    } catch(e) { await client.Error(e) }
  }
}