const RankUpChannels = ['766932314973929527', '783516524685688842', '871400280854523905'];

exports.run = async ({client, message}) => {
  try {

    if (!RankUpChannels.includes(message.channelId)) return;

    // todo: 랭크업 실행
    
  } catch (e) { await client.Error(e, message); }
};

exports.help = {
  '': `랭크업을 할 수 있습니다.\n\n${RankUpChannels.map(i => '<#'+i+'>').join(', ')} 에서만 사용할 수 있습니다.`
}
exports.permission = ['RankServer'];
exports.MsLength = [0];
exports.name = ['ㅇ'];
