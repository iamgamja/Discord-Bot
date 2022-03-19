const Admins = ['647001590766632966', '725528129648721920', '436071996661563402'];

exports.run = async ({client, message}) => {
  try {

    if (!Admins.includes(message.author.id)) return;

    // todo: 일급 주기 실행
    
  } catch (e) { await client.Error(e, message); }
};

exports.help = {
  '': `일급을 줍니다.\n\n${Admins.map(i => '<@'+i+'>').join(', ')}만 사용할 수 있습니다.`
}
exports.permission = ['RankServer'];
exports.MsLength = [0];
exports.name = ['.일급'];
