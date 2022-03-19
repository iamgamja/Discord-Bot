Math.sum = (arr) => arr.reduce((a,b)=>a+b, 0);
Math.middle = (arr) => Math.sum(arr) / arr.length;

const Discord = require('discord.js');
const {WebhookClient, MessageEmbed} = require('discord.js');
const fs = require('fs');
const Inko = require('inko');
const inko = new Inko();
const canvas = require('canvas');
const request = require('request');
const sharp = require('sharp');
const axios = require('axios');
// const base65536 = await import('base65536');
const chartJs = require('chart.js-image');
const ytdl = require('ytdl-core');
const ffmpeg = require('fluent-ffmpeg');

const sleep = s => new Promise(r => setTimeout(r, s));

let $_; // last result.

exports.run = async ({client, message, Ms}) => {
  try {

    const run_msg = `async (client, message, Ms) => { \n ${Ms[0]} \n }`;
    const result_func = eval(run_msg);
    const result = await result_func(client, message, Ms);
    $_ = result;
    await message.reply(''+ result);

  } catch (e) { await client.Error(e, message); }
};

exports.help = {
  '<코드>': '<코드>를 실행합니다.'
}
exports.permission = ['Admin'];
exports.MsLength = [1];
exports.name = ['.코드'];
