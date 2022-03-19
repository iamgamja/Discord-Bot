function randint(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min)) + min; //최댓값은 제외, 최솟값은 포함
}

exports.run = async ({client, message, Ms}) => {
  try {

    /* idea by @핫덕 hotduck#5554 */ if (Ms[0]==='__숫자__') { await message.reply('<:thronking:914166177226436669>'); return; }

    const n = +Ms[0];
    if (isNaN(n)) {
      await message.reply('`<n>`을 __숫자__로 입력해주세요. `.도움 게임 업다운`으로 자세한 도움말을 확인할 수 있습니다.');
      return
    }

    const target = randint(1, n+1); // n도 포함

    await message.reply('업다운 게임을 시작합니다!');

    let userTry = 0;

    while (true) {
      userTry += 1;
      let userMessage;
      try {
        await message.reply(`\`1\` ~ \`${n}\` 의 숫자 중 하나를 20초 안에 입력해주세요!`);
        const UserMessages = await message.channel.awaitMessages({filter: msg => msg.author.id === message.author.id, max: 1, time: 20*1000, errors: ['time']});
        userMessage = UserMessages.first();
      } catch {
        await message.reply(`시간 초과! 정답은 ${target} 입니다.`);
        return;
      }
      let userNumber = +userMessage.content;
      if (isNaN(userNumber)) {
        await userMessage.reply('숫자가 아닙니다!');
      } else if (userNumber === target) { // 정답
        await userMessage.reply(`정답입니다! 시도 횟수: ${userTry}`);
        break;
      } else if (userNumber > target) { // 다운
        await userMessage.reply('Down');
      } else { // 업
        await userMessage.reply('Up');
      }
    }
    
  } catch (e) { await client.Error(e, message); }
};

exports.help = {
  '<n>': '1부터 <n>까지의 업다운 게임을 진행합니다.'
}
exports.permission = ['All'];
exports.MsLength = [1];
exports.name = ['.게임', '업다운'];
