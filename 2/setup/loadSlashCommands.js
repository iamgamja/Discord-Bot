module.exports = async (client) => {
  try {

    const { REST } = require('@discordjs/rest');
    const { Routes } = require('discord-api-types/v9');

    const clientId = '874557216928186409';
    const guildId = '843811221433352214';

    const rest = new REST({ version: '9' }).setToken(process.env.TOKEN2);

    const slashCommands = [];
    const slashCommandfile = require('/app/2/commands/slash/data.js');

    for (const cmd of slashCommandfile) {
      slashCommands.push(cmd.toJSON());
    }

    await rest.put(
      Routes.applicationGuildCommands(clientId, guildId),
      { body: slashCommands },
    );

  } catch (e) { await client.Error(e) }
}