const Permission = require('/app/1/data/Permission');

module.exports = async (client) => {
  client.on("messageCreate", async (message) => {
    try {
      
      // 답장핑 끄기 및 기타 message.reply 재정의
      message.reply_ = message.reply;
      message.reply = async (s) => {
        if (typeof s === 'string') { // s가 문자열일때 처리
          if (!s.trim().length) s = '말을 할수 없는 (비어있음)'; // 비어있을때 기본값
          if (s.trim().length > 2000) s = `말을 할수 없는 (너무 긺, ${s.length}글자)` // 너무 길때 기본값
        }
        let inputObj = typeof s === 'string' ? {content: s} : s;
        let sourceObj = {
          allowedMentions: {
            users: [message.author.id],
            repliedUser: false
          }
        }
        let resultObj = Object.assign(inputObj, sourceObj);
        return await message.reply_(resultObj);
      }
  
      // 명령어 감지
      let Ms_ = message.content.split(' '); // 매개변수 목록, 명령어 포함
  
      let cmd = client.commands.find(command => {
        return command.match(message.content, false);
      });
  
      if (!cmd) return; // 커맨드가 감지되지 않음
  
      Ms_ = Ms_.slice(cmd.nameL);
  
      const checkPermissionData = {
        cmd: cmd,
        client: client,
        message: message,
      }
      
      if ( Permission(cmd.permission, checkPermissionData) ) {
        // Ms 생성
        let Ms;
        let my_number = Ms_.length;
        let can_numbers = [...cmd.MsLength]; // 복사
        if (!can_numbers.at(-1)) { // 가능한 수중 가장 큰수가 0, 매개변수가 필요없음
          Ms = [];
        } else if (my_number < can_numbers[0]) { // 가능한 수중 가장 작은수보다도 더 작음, "적음"
          await message.reply(`매개변수가 부족합니다. 최소 ${can_numbers[0]}개의 매개변수가 필요하지만, ${my_number}개의 매개변수가 입력되었습니다. \`.도움 ${cmd.nameSD}\`(으)로 자세한 도움말을 확인할 수 있습니다.`);
          return;
        } else { // 정상적인 상황.
          const final_number = [...can_numbers].reverse().find( i => (i <= my_number) ); // 가능한 수중 주어진 매개변수의 수보다 작은 수중 최댓값. (사용할 매개변수의 수)
          Ms = [ ...Ms_.slice(0, final_number-1), Ms_.slice(final_number-1).join(' ') ];
        }
        
        const inputData = {
          client: client,
          message: message,
          Ms: Ms,
        }
        
        await cmd.run(inputData);
      }
      
    } catch(e) { await client.Error(e, message); }
  });
  
}