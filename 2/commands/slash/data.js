const { SlashCommandBuilder } = require('@discordjs/builders');

module.exports = [
  
  new SlashCommandBuilder() // archive
    .setName('archive')
    .setDescription('채널을 아카이브로 보냅니다.')
    .addChannelOption(option =>
      option
        .setName('채널')
        .setDescription('아카이브로 보낼 채널을 선택하세요.')
        .setRequired(true)
    )
  ,
  new SlashCommandBuilder() // ping
    .setName('ping')
    .setDescription('봇의 작동 여부를 확인합니다.')
  ,
  new SlashCommandBuilder() // eval
    .setName('eval')
    .setDescription('js 코드를 실행합니다.')
    .addStringOption(option =>
      option
        .setName('코드')
        .setDescription('실행할 js 코드를 입력해주세요.')
        .setRequired(true)
    )
  ,
  new SlashCommandBuilder() // template
    .setName('template')
    .setDescription('템플릿을 생성/삭제/변경/설정합니다.')
    .addSubcommand(subcommand =>
      subcommand
        .setName('help')
        .setDescription('이 명령어의 도움말을 출력합니다.')
    ).addSubcommand(subcommand =>
      subcommand
        .setName('create')
        .setDescription('새로운 템플릿을 만듭니다.')
        .addStringOption(option =>
          option
            .setName('templatename')
            .setDescription('새로 만들 템플릿의 이름을 입력해주세요.')
            .setRequired(true)
        )
    ).addSubcommand(subcommand =>
      subcommand
        .setName('reset')
        .setDescription('템플릿들을 모두 리셋합니다.')
    ).addSubcommand(subcommand =>
      subcommand
        .setName('apply')
        .setDescription('템플릿을 적용합니다. 다시 되돌리기 위해 먼저 /template default 명령어로 기본값을 지정했는지 확인해주세요.')
        .addStringOption(option =>
          option
            .setName('templatename')
            .setDescription('적용할 템플릿의 이름을 입력해주세요.')
            .setRequired(true)
        )
    ).addSubcommand(subcommand =>
      subcommand
        .setName('default')
        .setDescription('기본 템플릿을 현재 상태로 설정합니다.')
        .addStringOption(option =>
          option
            .setName('templatename')
            .setDescription('설정할 기본 템플릿의 이름을 입력해주세요.')
            .setRequired(true)
        )
    ).addSubcommand(subcommand =>
      subcommand
        .setName('remove')
        .setDescription('템플릿을 삭제합니다.')
        .addStringOption(option =>
          option
            .setName('templatename')
            .setDescription('삭제할 템플릿의 이름을 입력해주세요.')
            .setRequired(true)
        )
    ).addSubcommand(subcommand =>
      subcommand
        .setName('list')
        .setDescription('템플릿 목록을 출력합니다.')
    ).addSubcommandGroup(group => 
      group
        .setName('channel')
        .setDescription('템플릿에 채널을 등록/삭제합니다.')
        .addSubcommand(subcommand =>
          subcommand
            .setName('add')
            .setDescription('템플릿에 채널을 등록합니다.')
            .addStringOption(option =>
              option
                .setName('templatename')
                .setDescription('추가할 템플릿의 이름을 입력해주세요.')
                .setRequired(true)
            ).addChannelOption(option =>
              option
                .setName('채널')
                .setDescription('이름이 바뀔 채널을 입력해주세요.')
                .setRequired(true)
            ).addStringOption(option =>
              option
                .setName('이름')
                .setDescription('바뀔 이름을 입력해주세요.')
                .setRequired(true)
            )
        ).addSubcommand(subcommand =>
          subcommand
            .setName('remove')
            .setDescription('템플릿에 등록된 채널을 삭제합니다.')
            .addStringOption(option =>
              option
                .setName('templatename')
                .setDescription('채널을 삭제할 템플릿의 이름을 입력해주세요.')
                .setRequired(true)
            ).addChannelOption(option =>
              option
                .setName('채널')
                .setDescription('삭제할 채널을 입력해주세요.')
                .setRequired(true)
            )
        ).addSubcommand(subcommand =>
          subcommand
            .setName('list')
            .setDescription('템플릿에 등록된 채널 목록을 출력합니다.')
            .addStringOption(option =>
              option
                .setName('templatename')
                .setDescription('채널 목록을 출력할 템플릿을 입력해주세요.')
                .setRequired(true)
            )
        )
    )
    ,

]
