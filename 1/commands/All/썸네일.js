const Youtube = require('youtube-node');
const youtube = new Youtube();
youtube.setKey(process.env.DEVELOPER_KEY);
youtube.addParam('type', 'video');

/** @async */
const search = (word, limit) => {
  return new Promise((resolve, reject) => {
    youtube.search(word, limit, function(err, result) {
      if (err)
        reject(err);
      else
        resolve(result);
    });
  });
}

exports.run = async ({client, message, Ms}) => {
  try {

    const result = await search(Ms[0], 1);
    client.log(JSON.stringify(result.items[0].snippet));

    await message.reply('wjfjs');
    
  } catch (e) { await client.Error(e, message); }
};

exports.help = {
  '<link>': '해당하는 영상의 썸네일을 출력합니다.'
}
exports.permission = ['All'];
exports.MsLength = [1];
exports.name = ['.썸네일'];
