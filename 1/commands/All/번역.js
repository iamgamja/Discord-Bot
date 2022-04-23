const https = require('https');

const clientid = process.env.translation_client_id;
const clientsecret = process.env.translation_client_secret;

async function post({url, headers, data}) {
  const dataString = JSON.stringify(data);

  const options = {
    method: 'POST',
    headers: headers,
    timeout: 1000
  }

  return new Promise((resolve, reject) => {
    const req = https.request(url, options, (res) => {
      if (res.statusCode < 200 || res.statusCode > 299) {
        return reject(new Error(`HTTP status code ${res.statusCode}`));
      }

      const body = [];
      res.on('data', (chunk) => body.push(chunk));
      res.on('end', () => {
        const resString = Buffer.concat(body).toString();
        resolve(resString);
      });
    });

    req.on('error', (err) => {
      reject(err);
    });

    req.on('timeout', () => {
      req.destroy();
      reject(new Error('Request time out'));
    });

    req.write(dataString);
    req.end();
  });
}

exports.run = async ({client, message, Ms}) => {
  try {

    const { langCode } = JSON.parse(
      await post({
        url: 'https://openapi.naver.com/v1/papago/detectLangs',
        headers: {
          'X-Naver-Client-Id': clientid,
          'X-Naver-Client-Secret': clientsecret
        },
        data: {
          query : Ms[0]
        }
      })
    );

    const { message: { result: { translatedText: result } } } = JSON.parse(
      await post({
        url: 'https://openapi.naver.com/v1/papago/n2mt',
        headers: {
          'X-Naver-Client-Id': clientid,
          'X-Naver-Client-Secret': clientsecret
        },
        data: {
          text: Ms[0],
          source: langCode,
          target: langCode === 'ko' ? 'en' : 'ko'
        }
      })
    );

    await message.reply(result);

  } catch (e) { await client.Error(e, message); }
};

exports.help = {
  '<영어>': '<영어>를 한국어로 번역합니다.',
  '<한국어>': '<한국어>를 영어로 번역합니다.'
}
exports.permission = ['All'];
exports.MsLength = [1];
exports.name = ['.번역'];
