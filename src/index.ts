import  GuildClient  from '@citadel-guilds/sdk';

const guild = new GuildClient({
  name: 'commerce',
  natsPrefix: 'citadel.commerce',
  port: 8422,
});

guild.start();
