const data = {
  All() {
    return true;
  },
  Admin({message}) {
    const Admins = ['526889025894875158', '415830047539331072', '357504806358614035', '536517275667267605', '559305027211100161', '723335189555707976'];
    return Admins.includes(message.author.id);
  },
  RankServer({message}) {
    return message.guildId === '766932314973929522';
  },
  Metaverse({message}) {
    return message.guildId === '743101101401964647';
  },
  Talk({cmd, message}) {
    return cmd.nameS === message.content;
  }
}

module.exports = (arr, checkPermissionData) => arr.every(s => data[s](checkPermissionData));