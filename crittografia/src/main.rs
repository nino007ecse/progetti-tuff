use clap::{Parser, Subcommand};
use std::fs;

mod crypto;
mod stego;

#[derive(Parser)]
#[command(name = "crypto_stego")]
#[command(about = "Tool di crittografia fatto da ninja", long_about = None)]
struct Cli {
    #[command(subcommand)]
    command: Commands,
}

#[derive(Subcommand)]
enum Commands {

    Encode {
        #[arg(short, long)]
        image: String,
        #[arg(short, long)]
        message: String,
        #[arg(short, long)]
        password: String,
        #[arg(short, long)]
        output: String,
    },

    Decode {
        #[arg(short, long)]
        image: String,
        #[arg(short, long)]
        password: String,
    },
}

fn main() {
    let cli = Cli::parse();

    match &cli.command {
        Commands::Encode { image, message, password, output } => {
            println!("Cifratura del messaggio in corso...");
            match crypto::encrypt_data(message.as_bytes(), password) {
                Ok(encrypted_bytes) => {
                    println!("Inserimento del codice nell'immagine...");
                    match stego::hide_payload(image, &encrypted_bytes, output) {
                        Ok(_) => println!("Successo! Immagine salvata in: {}", output),
                        Err(e) => eprintln!("Errore steganografia: {}", e),
                    }
                }
                Err(e) => eprintln!("Errore crittografia: {}", e),
            }
        }
        Commands::Decode { image, password } => {
            println!("Analisi dell'immagine...");
            match stego::extract_payload(image) {
                Ok(encrypted_bytes) => {
                    println!("Tentativo di decifratura...");
                    match crypto::decrypt_data(&encrypted_bytes, password) {
                        Ok(decrypted_bytes) => {
                            match String::from_utf8(decrypted_bytes) {
                                Ok(msg) => println!("Messaggio Segreto Trovato:\n {}", msg),
                                Err(_) => eprintln!("I dati decifrati non sono testo valido."),
                            }
                        }
                        Err(_) => eprintln!("Password errata o dati corrotti!"),
                    }
                }
                Err(e) => eprintln!("Errore estrazione: {}", e),
            }
        }
    }
}