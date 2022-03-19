function Date_(){const d=new Date;return d.setHours(d.getHours()+9),d}

// 통계 ㅌ이머
let timer;

module.exports = async (client) => {
  client.on("ready", async () => {
    try {
  
      // 통계 ㅌ이머 만들기
      const now = Date_();
      const now1 = now.getMinutes();
      const now2 = now.getSeconds();
      const leftTime = 60*60*1000 - (now1*60*1000) - (now2*1000) + 1*60*1000; // 정각까지 남은 시간+1분(밀리초 단위)
      setTimeout(async function() {
        try {
          await client.TongGye();
          timer = setInterval(async function() {
            try {
              await client.TongGye();
            } catch(e) { await client.Error(e) }
          }, 60*60*1000); // 1시간마다 client.TongGye 실행
        } catch(e) { await client.Error(e) }
      }, leftTime);
  
  
      client.user.setActivity("헊");
      client.log('<@!526889025894875158>', 'online!');
  
    } catch (e) { await client.Error(e) }
  });
}