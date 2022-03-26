function D2Date_(d){return d.setHours(d.getHours()+9),d}

module.exports = async (client) => {
  client._.TongGye.f4 = async () => {
    try {
  
      const event = client.guilds.cache.get('843811221433352214').scheduledEvents.cache.find(e => {
        return e.name.endswith('생일') &&
          D2Date_(e.scheduledStartAt).toDateString() === D2Date_(new Date()).toDateString();
      });

      if (!event) {
        client.channels.cache.get('956573678638878730').setName('그리고 아무도 생일이지 않았다');
      } else {
        client.channels.cache.get('956573678638878730').setName(`event.name.slice(0,-3) 생일`);
      }

    } catch(e) { await client.Error(e) }
  }
}
