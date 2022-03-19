const Discord = require('discord.js');
const intents = new Discord.Intents(0b111111111111111);
const client = new Discord.Client({ intents: intents });

(async ()=>{
  await require('/app/1/setup/commands.js')(client);

  await require('/app/1/setup/log.js')(client);
  await require('/app/1/setup/Error.js')(client);

  // Event
  await require('/app/1/setup/event/ready.js')(client);
  await require('/app/1/setup/event/interactionCreate.js')(client);
  await require('/app/1/setup/event/modalSubmit.js')(client);
  await require('/app/1/setup/event/messageCreate.js')(client);

  client.login(process.env.TOKEN1);
})();
