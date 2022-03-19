/**
 * Code by: Spotky1004
 * Edit: iamgamja
 */
let string2base65536, base655362string;
(async () => {
  const base65536 = await import('base65536');
  const encode = base65536.encode;
  const decode = base65536.decode;

  const textEncoder = new TextEncoder();
  const textDecoder = new TextDecoder("utf-8");

  const string2base65536 = (s) => encode(textEncoder.encode(s));
  const base655362string = (b) => textDecoder.decode(new Uint8Array(decode(b)));
  return [string2base65536, base655362string];
})().then(r => {
  [string2base65536, base655362string] = r;
});

module.exports = async (client) => {
  try {

    client.db = {};

    client.db.getMessages = async () => {
      return [
        await client.channels.cache.get('893633209261244416').messages.fetch('893715021467619370'),
        await client.channels.cache.get('893633209261244416').messages.fetch('894122020143505449'),
        await client.channels.cache.get('893633209261244416').messages.fetch('894122043262529537'),
        await client.channels.cache.get('893633209261244416').messages.fetch('894122045611311125'),
        await client.channels.cache.get('893633209261244416').messages.fetch('894122064947052565'),
      ];
    }

    client.db.get = async () => {
      let Messages = await client.db.getMessages();
      let base65536Content = Messages.map(x => x.content !== 'null' ? x.content : '').join(''); // 전부 합치기
      let stringContent = base655362string(base65536Content);
      return JSON.parse(stringContent);
    }

    client.db.set = async (obj) => {
      let Messages = await client.db.getMessages();
      let stringContent = JSON.stringify(obj);
      let base65536Content = string2base65536(stringContent);
      for (let i=0; i<5; i++) {
        await Messages[i].edit(
          base65536Content.slice(i*2000, (i+1)*2000) ? // 2000자씩 쪼개기
          base65536Content.slice(i*2000, (i+1)*2000) : // 있으면(''이 아니면) 그대로 입력
          'null'                                       // 아니면(''이 맞으면) null을 입력
        )
      }
    }

    client.db.add = async (keys, value) => { // ( ['first', 'second'], 1) => data.first.second = 1;
      let data = await client.db.get();
      let data_ = data; // copy

      for (let key of keys.slice(0, -1)) {// 마지막 key는 제외하고 반복
        data_ = data_[key]; // a.b.c...
      }
      data_[keys.at(-1)] = value; // 마지막 key를 사용
      await client.db.set(data);
    }

    client.db.remove = async (keys) => { // ( ['first', 'second'] ) => REMOVE `data.first.second`
      let data = await client.db.get();
      let data_ = data; // copy

      for (let key of keys.slice(0, -1)) {// 마지막 key는 제외하고 반복
        data_ = data_[key]; // a.b.c...
      }
      delete data_[keys.at(-1)]; // 마지막 key를 사용
      await client.db.set(data);
    }

    client.db.init = async () => { // db를 {}로 초기화한다.
      await client.db.set({});
    }

  } catch (e) { await client.Error(e) }
}
