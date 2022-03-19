const Admins = ['647001590766632966', '725528129648721920', '436071996661563402'];

exports.run = async ({client, message, Ms}) => {
  try {

    if (!Admins.includes(message.author.id)) return;

    const n = +Ms[0];
    const members = message.mentions.members;
    members.forEach(async (member) => {
      // todo: 랭크 지급
    })
    
  } catch (e) { await client.Error(e, message); }
};

exports.help = {
  '<n> <멘션1> <멘션2> ...': `멘션된 유저들에게 n만큼 랭크를 지급합니다. (n은 음수일수도 있습니다.)\n\n${Admins.map(i => '<@'+i+'>').join(', ')}만 사용할 수 있습니다.`
}
exports.permission = ['RankServer'];
exports.MsLength = [2]; // Ms[1]은 message.mentions로 대체되어 사용되지 않음.
exports.name = ['.지급'];
