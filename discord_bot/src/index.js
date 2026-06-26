require('dotenv').config();
const { Client, GatewayIntentBits, Collection, Events } = require('discord.js');
const fs = require('fs');
const path = require('path');

const client = new Client({ intents: [GatewayIntentBits.Guilds] });

client.commands = new Collection();

const commandsPath = path.join(__dirname, 'commands');
const commandFiles = fs.readdirSync(commandsPath).filter(file => file.endsWith('.js'));

for (const file of commandFiles) {
    const filePath = path.join(commandsPath, file);
    const command = require(filePath);
    
    if ('data' in command && 'execute' in command) {
        client.commands.set(command.data.name, command);
    } else {
        console.log(`[AVVISO] Il comando in ${filePath} non ha le proprietà "data" o "execute".`);
    }
}

client.once(Events.ClientReady, readyClient => {
    console.log(`Loggato come ${readyClient.user.tag}`);
});

client.on(Events.InteractionCreate, async interaction => {
    if (!interaction.isChatInputCommand()) return;

    const command = interaction.client.commands.get(interaction.commandName);

    if (!command) {
        console.error(`Nessun comando corrispondente a ${interaction.commandName} trovato.`);
        return;
    }

    try {
        await command.execute(interaction);
    } catch (error) {
        console.error(error);
        if (interaction.replied || interaction.deferred) {
            await interaction.followUp({ content: 'Si è verificato un errore durante l\'esecuzione del comando!', ephemeral: true });
        } else {
            await interaction.reply({ content: 'Si è verificato un errore durante l\'esecuzione del comando!', ephemeral: true });
        }
    }
});

client.login(process.env.DISCORD_TOKEN);