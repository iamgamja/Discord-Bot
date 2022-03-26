function D2Date_(d){return d.setHours(d.getHours()+9),d}
function sameDay(d1, d2) {
  return d1.getFullYear() === d2.getFullYear() &&
    d1.getMonth() === d2.getMonth() &&
    d1.getDate() === d2.getDate();
}

module.exports = async (client) => {
  client._.TongGye.f4 = async () => {
    try {
  
      const event = client.guilds.cache.get('843811221433352214').scheduledEvents.cache.find(e => {
        return e.name.endswith('생일') &&
          sameDay(D2Date_(e.scheduledStartAt), D2Date_(new Date));
      });

      if (!event) {
        client.channels.cache.get('956573678638878730').setName('그리고 아무도 생일이지 않았다');
      } else {
        client.channels.cache.get('956573678638878730').setName(`${event.name.slice(0,-3)} 생일`);
      }

    } catch(e) { await client.Error(e) }
  }
}
