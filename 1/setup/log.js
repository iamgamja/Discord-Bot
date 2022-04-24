module.exports = async (client) => {
  client.log = async (...s) => {
    return await client.log_('883236535854571590', ...s);
  }

  client.log_ = async (c, ...s) => {
    let logmsg = s.join('\n');
    console.log(logmsg.slice(0, 2000));
    const msg1 = await client.channels.cache.get(c).send(logmsg.slice(0, 2000));
    
    if (logmsg.slice(2000)) {
      const msg2 = await client.log(logmsg.slice(2000));
      return [msg1, ...msg2];
    }
    return [msg1];
  }
}
