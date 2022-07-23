const Discord = require("discord.js");
const intents = new Discord.Intents(0b111111111111111);
const client = new Discord.Client({ intents: intents });

client._ = {};
client.Loops = {};

(async () => {
  await require('/app/2/setup/log.js')(client);
  await require('/app/2/setup/Error.js')(client);

  await require('/app/2/setup/loadSlashCommands.js')(client);
  await require('/app/2/setup/db.js')(client);

  await require('/app/2/setup/Loops/f1.js')(client);
  await require('/app/2/setup/Loops/f2.js')(client);
  await require('/app/2/setup/Loops/f3.js')(client);
  await require('/app/2/setup/Loops/f4.js')(client);
  await require('/app/2/setup/Loops/index.js')(client);

  // Event
  await require('/app/2/setup/event/interactionCreate.js')(client);
  await require('/app/2/setup/event/ready.js')(client);

})();

client.login(process.env.TOKEN2);
