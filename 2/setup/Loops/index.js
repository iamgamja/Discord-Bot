const fs = require('fs');
fs.RF=(e=>new Promise((f,i)=>{fs.readFile(e,"utf8",function(e,n){e?i(e):f(n)})}));
function Date_(){const d=new Date;return d.setHours(d.getHours()+9),d}

const Discord = require("discord.js");

module.exports = async (client) => {
  client.Loops.run = async () => {
    try {
  
      const date = Date_();
      date.setHours(date.getHours()-1);
      const hour = date.getHours(); // (hour) 시부터 (hour+1) 시까지
  
      const A = await client.Loops.f1(); // array, 유저·봇 상태·수
      const B = await client.Loops.f2(); // array, 메시지 수
      const AB = [...A, ...B];               // array
      await client.db.add(['TongGye', 'B', hour], B[0]); // db에 메시지수 넣기
  
      if (hour === 23) {
        client.Loops.f4(); // 생일

        const C = await client._.Loops.f3(); // buffer, 그래프 이미지
        await client.channels.cache.get('920536110382329907').send({ files: [new Discord.MessageAttachment(C, 'chart.png')] });
  
        await client.db.add(['TongGye', 'B'], new Array(24).fill(0)); // 재설정
      }
  
      let sendContent = await fs.RF('/app/2/data/string.txt');
      for (let i in AB)
        sendContent = sendContent.replace(`{${i}}`, AB[i]);
  
      await client.channels.cache.get('920536110382329907').send(sendContent);
  
  
    } catch(e) { await client.Error(e) }
  
  }
}
