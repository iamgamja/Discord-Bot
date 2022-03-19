module.exports = async (client) => {
  client.log = async (...s) => {
    await client.log_('892688468453523487', ...s);
  }

  client.log_ = async (c, ...s) => {
    let logmsg = s.join('\n');
    console.log(logmsg.slice(0, 2000));
    await client.channels.cache.get(c).send(logmsg.slice(0, 2000));
    
    if (logmsg.slice(2000)) {
      await client.log(logmsg.slice(2000));
    }
  }
}