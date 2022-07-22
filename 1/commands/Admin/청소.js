exports.run = async ({client, message, Ms}) => {
  try {

    const n = +Ms[0];

    for (let i=0; i<n; i+=100) {
      let fetched = await message.channel.messages.fetch({limit: i+100<n ? 100 : n-i});
      await message.channel.bulkDelete(fetched);
    }

  } catch (e) { await client.Error(e, message); }
};

exports.help = {
  '<n>': '<n>개의 메시지를 지웁니다.'
}
exports.permission = ['Admin'];
exports.MsLength = [1];
exports.name = ['.청소'];
