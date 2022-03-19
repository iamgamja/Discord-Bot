module.exports = async (client) => {
  client.on("ready", async () => {
    try {
      
      await client.log('<@!526889025894875158>', client.user.tag, 'online!');
      
    } catch (e) { await client.Error(e); }
  });
}
