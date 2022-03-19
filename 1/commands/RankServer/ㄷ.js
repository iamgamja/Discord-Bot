const BettingChannels = ['784228694940057640', '794146499034480661'];

exports.run = async ({client, message}) => {
  try {

    if (!BettingChannels.includes(message.channelId)) return;

    // todo: 랭크업 실행
    
  } catch (e) { await client.Error(e, message); }
};

exports.help = {
  '': `도박을 할 수 있습니다.\n\n${BettingChannels.map(i => '<#'+i+'>').join(', ')} 에서 사용할 수 있습니다.`
}
exports.permission = ['RankServer'];
exports.MsLength = [0];
exports.name = ['ㄷ'];
