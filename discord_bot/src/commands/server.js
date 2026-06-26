const { SlashCommandBuilder, EmbedBuilder } = require('discord.js');

module.exports = {
    data: new SlashCommandBuilder()
        .setName('server')
        .setDescription('Mostra informazioni dettagliate su questo server.'),
    async execute(interaction) {
        const { guild } = interaction;

        const embed = new EmbedBuilder()
            .setTitle(`Info su ${guild.name}`)
            .setColor('#f48333')
            .setThumbnail(guild.iconURL({ dynamic: true }))
            .addFields(
                { name: 'Membri Totali', value: `${guild.memberCount}`, inline: true },
                { name: 'Creato il', value: `<t:${Math.floor(guild.createdTimestamp / 1000)}:R>`, inline: true }
            );

        await interaction.reply({ embeds: [embed] });
    },
};