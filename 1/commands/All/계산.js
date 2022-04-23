const w = require('wolfram-alpha').createClient(process.env.wolframalpha_key);

exports.run = async ({client, message, Ms}) => {
  try {

    const result = await w.query(Ms[0]);
    await message.reply(result.at(-1));
    
  } catch (e) { await client.Error(e, message); }
};

exports.help = {
  '<식>': 'WolframAlpha에서 <식>을 계산합니다.'
}
exports.permission = ['All'];
exports.MsLength = [1];
exports.name = ['.계산'];
