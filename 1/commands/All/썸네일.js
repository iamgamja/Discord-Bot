const Youtube = require('youtube-node');
const youtube = new Youtube();
youtube.setKey(process.env.DEVELOPER_KEY);
// youtube.addParam('type', 'video');

/** @async */
const search = (word, limit) => {
  return new Promise((resolve, reject) => {
    youtube.search(word, limit, {type: 'video'}, function(err, result) {
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

    const item = result.items[0];
    
    const title = item.snippet.title;
    const thumbnail1 = Object.values(item.snippet.thumbnails).sort((a,b) => {
      return a.width-b.width;
    }).at(-1).url;
    const id = item.id.videoId;
    const thumbnail2 = `https://i.ytimg.com/vi/${id}/original.jpg`;

    await message.reply(`${title}\n${thumbnail1}\n${thumbnail2}`);
    
  } catch (e) { await client.Error(e, message); }
};

exports.help = {
  '<검색어>': '검색된 영상의 썸네일을 출력합니다.'
}
exports.permission = ['All'];
exports.MsLength = [1];
exports.name = ['.썸네일'];
