Math.sum = (arr) => arr.reduce((a,b)=>a+b, 0);
Math.middle = (arr) => Math.sum(arr) / arr.length;

const fs = require('fs');
const ffmpeg = require('fluent-ffmpeg');
const ytdl = require('ytdl-core');
const sharp = require('sharp');
const axios = require('axios');

const sleep = s => new Promise(r => setTimeout(r, s));

const FRAME = 3; // 1초에 frame 개의 이미지를 보냅니다.

/**
 * @param {Ascii[]} arr
 * @param {Webhook[]} webhooks
 */
const anim = async (arr, webhooks) => {
  console.log('anim called')
  const h = Math.max( ...arr.map(s => s.trimEnd().split('\n').length) );

  arr = arr.map(c => {
    if (c.split('\n').length < h) {
      c += ( String.fromCharCode(0x3164)+'\n' ).repeat(h-c.split('\n').length);
    }

    if (c.length > 2000) throw Error('2000보다 큰 문자열이 있습니다.');

    return c;
  });

  if (arr.findIndex(x=>!x) !== -1) throw Error(`${arr.findIndex(x=>!x)} 번째 이미지를 보낼 수 없습니다.`);

  for (let i in arr) {
    await sleep(1000/FRAME);
    await webhooks[i%10].send({
      content: arr[i],
      username: '᲼',
      avatarURL: 'http://placehold.it/1/36393f',
    });
  }
}

/**
 * @typedef {String} Ascii - 점자로 구성된 문자열입니다. 하나의 Ascii는 하나의 이미지를 나타냅니다.
 */

/**
 * image의 경로/buffer 를 받아 Ascii로 변환합니다.
 * @param {Object} _1
 * @param {String} _1.axiosInput - 'https://example.com/'
 * @param {Buffer} _1.sharpInput - buffer, '/app/data/...'
 * @param {Object} [_2]
 * @param {Number} [_2.width] - 이미지의 너비입니다.
 * * 한 줄의 글자수와 같지 않음에 주의하세요. 한 줄의 글자수는 약 `width/3` 입니다.
 * @param {Boolean} [_2.isMobile=true] - true일 경우 빈 공간을 U+2800으로, false일 경우 빈 공간을 U+2801로 채웁니다.
 * @returns {Ascii}
 */
const image2ascii = async ({axiosInput=null, sharpInput=null}, {width=null, isMobile=true}={}) => {
  console.log('image2ascii called')
  if (!axiosInput && !sharpInput)
    throw Error(`ERROR: path, buffer 모두 입력되지 않았습니다.`);
  if (axiosInput && sharpInput)
    throw Error(`ERROR: path, buffer 모두 입력되었습니다.`);

  width ??= isMobile ? 70 : 100;
  
  if (!sharpInput) {
    let _buffer = await axios.get(axiosInput, {responseType: 'arraybuffer'});  
    sharpInput = Buffer.from(_buffer.data, 'binary');
  }

  let img = await sharp(sharpInput, {})
  .flatten({ background: { r: 255, g: 255, b: 255 } })
  .resize(width)
  .grayscale()
  .raw()
  .toBuffer();
  
  let lightScales_ = [...img];

  // let middleScale = ( Math.min(...lightScales_) + Math.max(...lightScales_) ) / 2;
  let middleScale = Math.middle([0, 255]); // 평균값

  let lightScales = []; // 2차원
  while (lightScales_.length) {
    lightScales.push( lightScales_.splice(0, width) );
  }

  // 칸채우기
  switch (lightScales.length % 5) {
    case 0: // 1줄 지워야함
      lightScales.splice(-1, 1); // 마지막 1개 지움
      break;
    case 1: // 1줄 남음 (3줄 채워서 4줄 맞추기)
      lightScales.push( new Array(width).fill(255) );
    case 2: // 2줄 남음 (2줄 채워서 4줄 맞추기)
      lightScales.push( new Array(width).fill(255) );
    case 3: // 3줄 남음 (1줄 채워서 4줄 맞추기)
      lightScales.push( new Array(width).fill(255) );
    // case 4: 딱 맞음.
  }
  switch (width % 3) {
    case 0: // 1칸 지워야함
      lightScales = lightScales.map( arr => arr.slice(0, -1) );
      break;
    case 1: // 1칸 남음 (1칸 채워서 2칸 맞추기)
      lightScales = lightScales.map( arr => arr.concat(255) );
    // case 2: 딱 맞음.
  }

  // 2중 for문으로 점자 생성.
  let w,h;
  [w, h] = [lightScales[0].length, lightScales.length];

  let asciis = '';
  for (let y=0; y<h; y+=5) {
    for (let x=0; x<w; x+=3) {
      /*
        0 3
        1 4
        2 5
        6 7
      */

      let nowUnicodeNum = 0x2800;
      if (middleScale < lightScales[y+0][x+0]) nowUnicodeNum += 2** 0;
      if (middleScale < lightScales[y+1][x+0]) nowUnicodeNum += 2** 1;
      if (middleScale < lightScales[y+2][x+0]) nowUnicodeNum += 2** 2;
      if (middleScale < lightScales[y+0][x+1]) nowUnicodeNum += 2** 3;
      if (middleScale < lightScales[y+1][x+1]) nowUnicodeNum += 2** 4;
      if (middleScale < lightScales[y+2][x+1]) nowUnicodeNum += 2** 5;
      if (middleScale < lightScales[y+3][x+0]) nowUnicodeNum += 2** 6;
      if (middleScale < lightScales[y+3][x+1]) nowUnicodeNum += 2** 7;

      if (!isMobile && nowUnicodeNum === 0x2800) {
        nowUnicodeNum += 1;
      }

      asciis += String.fromCharCode(nowUnicodeNum);
    }
    asciis += '\n';
  }

  return asciis;
}

/**
 * youtube 동영상 링크를 받아서 Ascii 문자열들을 반환합니다.
 * @param {String} youtubeURL 
 * @param {Number} length - 변환할 영상의 길이입니다. 초단위로 입력하세요.
 * @param {Object} [_1]
 * @param {Number} [_1.width] - 영상의 너비입니다.
 * * 한 줄의 글자수와 같지 않음에 주의하세요. 한 줄의 글자수는 약 `width/3` 입니다.
 * @param {Boolean} [_1.isMobile=true] - true일 경우 빈 공간을 U+2800으로, false일 경우 빈 공간을 U+2801로 채웁니다.
 * @returns {Ascii[]}
 */
const youtube2ascii = async (youtubeURL, length, {width=null, isMobile=true}={}) => {
  console.log('youtube2ascii called')
  width ??= isMobile ? 70 : 100;

  const videoPromise = new Promise((resolve, reject) => {
    
    const videoDir = `/app/data/tmp/${Date.now()}_video.mp4`;
    
    const output = fs.createWriteStream(videoDir);
    output.on('finish', () => resolve(videoDir));
    output.on('error', reject);
    
    ytdl(youtubeURL, { format: 'mp4' }).pipe(output);
    
  });
  const videoDir = await videoPromise;

  
  const dir = `/app/data/tmp/${Date.now()}`;
  fs.mkdirSync(dir);

  // dir 경로에 0.1초단위로 캡쳐한 이미지를 생성함.
  const capture1sec = (sec) => {
    console.log('capture1sec called')
    return new Promise((resolve, reject) => {

      const imageCount = Math.round( Math.min(length-sec, 1)*FRAME ); // 1초 이상 남아있으면 FRAME 만큼 캡쳐, 아니면 남은만큼만 캡쳐

      ffmpeg(videoDir)
      .on('error', reject)
      .on('end', resolve)
      .screenshots({
        timestamps: [...new Array(imageCount).keys()].map(x => sec+x/FRAME), // [ i+0/FRAME(=i), i+1/FRAME, ... ]
        filename: `${sec.toString().padStart(4, '0')}_image%000i.png`,
        folder: dir
      });

    });
  }
  for (let i=0; i<length; i+=1) {
    // i초부터 i+1초까지
    await capture1sec(i);
  }
  
  const asciis = await Promise.all(
    fs.readdirSync(dir) // [ 'image1.png', ... ]
    .map(  f => `${dir}/${f}`  ) // [ '/app/.../image1.png', ... ]
    .map(  async (d) => await image2ascii({sharpInput: d}, {isMobile: isMobile})  ) // [ Promise<String>, ... ]
  ); // [ <String>, ... ]

  return asciis;
}


exports.run = async ({client, message, Ms}) => {
  try {

    let isMobile;

    if (Ms[0] === '모바일') {
      isMobile = true;
    } else if (Ms[0] === '데스크탑') {
      isMobile = false;
    } else {
      await message.reply('올바르지 않은 <플랫폼>입니다. `.도움 재생`으로 자세한 도움말을 확인할 수 있습니다.');
      return;
    }

    if (!message.channel.permissionsFor(client.user.id).has('MANAGE_WEBHOOKS')) {
      await message.reply('`웹후크 관리하기` 권한이 없습니다.');
      return;
    }

    await message.reply('Loading...');

    // webhook 생성
    let webhooks = [...(await message.channel.fetchWebhooks()).values()];
    let myWebhooks = [];
    const n = 10 - webhooks.length;
    for (let i=0; i<n; i++) {
      const webhook = await message.channel.createWebhook('frame');
      webhooks.push(webhook);
      myWebhooks.push(webhook);
    }

    // 재생
    const asciis = await youtube2ascii(Ms[1], Ms[2], {isMobile: isMobile});
    await anim(asciis, webhooks);

    // 생성한 webhook 제거
    for (const webhook of myWebhooks) {
      await webhook.delete();
    }

    await message.reply('재생이 완료되었습니다!');
    
  } catch (e) { await client.Error(e, message); }
};

exports.help = {
  '<플랫폼> <유튜브 영상 링크> <길이>': '<유튜브 영상 링크> 의 `0초~<길이>초` 를 현재 채널에서 __재생__합니다.\n\n<플랫폼>은 `모바일`, `데스크탑`중 하나여야 합니다.\n<플랫폼>은 크기와 빈칸에 영향을 끼칩니다.\n\n**도배가 될 수 있습니다. 주의해주세요.**\n\n> `웹후크 관리하기` 권한이 있어야 사용할 수 있습니다.'
}
exports.permission = ['All'];
exports.MsLength = [3];
exports.name = ['.재생'];
