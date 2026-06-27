# dovete creare un file webhooks.txt dove mettete SOLO i link dei webhooks dalla APP DI DISCORD
# dovete creare un file messages.txt dove mettete i messaggi da inviare

import requests
import time
import os
from colorama import init, Fore, Style

init(autoreset=True)

def send_webhook(webhook_url, message):
    try:
        data = {"content": message, "tts": False}
        response = requests.post(webhook_url, json=data)
        if response.status_code == 204:
            return True, "OK"
        else:
            return False, f"Error {response.status_code}"
    except Exception as e:
        return False, f"Error: {str(e)[:30]}"

def read_webhooks(filename):
    webhooks = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if line and not line.startswith('#'):
                    if line.startswith('https://discord.com/api/webhooks/') or line.startswith('https://discordapp.com/api/webhooks/'):
                        webhooks.append(line)
        return webhooks
    except FileNotFoundError:
        print(f"{Fore.RED}File {filename} not found")
        return None
    except Exception as e:
        print(f"{Fore.RED}Error reading file: {str(e)}")
        return None

def read_messages(filename):
    messages = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if line and not line.startswith('#'):
                    messages.append(line)
        return messages
    except FileNotFoundError:
        print(f"{Fore.RED}File {filename} not found")
        return None
    except Exception as e:
        print(f"{Fore.RED}Error reading file: {str(e)}")
        return None

def spam_all_webhooks_messages(webhooks_file='webhooks.txt', messages_file='messages.txt', delay=0, shuffle=False):
    webhooks = read_webhooks(webhooks_file)
    if not webhooks:
        print(f"{Fore.RED}No webhooks found")
        return
    
    messages = read_messages(messages_file)
    if not messages:
        print(f"{Fore.RED}No messages found")
        return
    
    if shuffle:
        import random
        random.shuffle(messages)
        random.shuffle(webhooks)
    
    total = len(webhooks) * len(messages)
    success = 0
    failed = 0
    counter = 0
    
    print(f"\n{Fore.CYAN}Webhooks: {len(webhooks)}")
    print(f"{Fore.CYAN}Messages: {len(messages)}")
    print(f"{Fore.CYAN}Total sends: {total}")
    if delay > 0:
        print(f"{Fore.CYAN}Delay: {delay}s")
    print(f"{Fore.CYAN}{'-'*50}\n")
    
    for w_idx, webhook in enumerate(webhooks, 1):
        print(f"\n{Fore.YELLOW}Webhook {w_idx}/{len(webhooks)}")
        
        for m_idx, message in enumerate(messages, 1):
            counter += 1
            print(f"{Fore.WHITE}[{counter}/{total}] ", end="")
            print(f"{Fore.CYAN}Msg {m_idx}/{len(messages)}: ", end="")
            print(f"{Fore.WHITE}{message[:40]}{'...' if len(message) > 40 else ''}")
            
            ok, result = send_webhook(webhook, message)
            
            if ok:
                success += 1
                print(f"  {Fore.GREEN}[OK]")
            else:
                failed += 1
                print(f"  {Fore.RED}[FAIL] {result}")
            
            if delay > 0 and counter < total:
                time.sleep(delay)
    
    print(f"\n{Fore.CYAN}{'-'*50}")
    print(f"{Fore.GREEN}Success: {success}/{total}")
    print(f"{Fore.RED}Failed: {failed}/{total}")
    print(f"{Fore.CYAN}{'-'*50}")

def show_files_content():
    print(f"\n{Fore.CYAN}{'='*50}")
    print(f"{Fore.CYAN}FILES CONTENT")
    print(f"{Fore.CYAN}{'='*50}")
    
    if os.path.exists('webhooks.txt'):
        print(f"\n{Fore.GREEN}webhooks.txt:")
        with open('webhooks.txt', 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for i, line in enumerate(lines, 1):
                line = line.strip()
                if line:
                    print(f"{Fore.WHITE}{i}. {line}")
    else:
        print(f"{Fore.RED}webhooks.txt not found")
    
    if os.path.exists('messages.txt'):
        print(f"\n{Fore.GREEN}messages.txt:")
        with open('messages.txt', 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for i, line in enumerate(lines, 1):
                line = line.strip()
                if line:
                    print(f"{Fore.WHITE}{i}. {line}")
    else:
        print(f"{Fore.RED}messages.txt not found")

def create_files():
    if not os.path.exists('webhooks.txt'):
        with open('webhooks.txt', 'w', encoding='utf-8') as f:
            f.write("https://discord.com/api/webhooks/ID/TOKEN\n")
        print(f"{Fore.GREEN}Created webhooks.txt")
    
    if not os.path.exists('messages.txt'):
        with open('messages.txt', 'w', encoding='utf-8') as f:
            f.write("Hello from webhook\n")
            f.write("Test message 2\n")
            f.write("Message 3\n")
        print(f"{Fore.GREEN}Created messages.txt")

def main():
    print(Fore.MAGENTA + "="*50)
    print(Fore.MAGENTA + "   DISCORD WEBHOOK SPAMMER   ")
    print(Fore.MAGENTA + "="*50)
    print(Fore.YELLOW + "Use only on your own webhooks\n")
    
    create_files()
    
    try:
        print(f"{Fore.CYAN}Options:")
        print(f"{Fore.CYAN}1. Show files content")
        print(f"{Fore.CYAN}2. Start spamming")
        print(f"{Fore.CYAN}3. Exit")
        
        choice = input(f"{Fore.CYAN}\nChoice (1-3): ").strip()
        
        if choice == "1":
            show_files_content()
            return
        
        if choice == "3":
            print(f"{Fore.MAGENTA}Goodbye")
            return
        
        if choice == "2":
            webhooks = read_webhooks('webhooks.txt')
            messages = read_messages('messages.txt')
            
            if not webhooks:
                print(f"{Fore.RED}No webhooks found in webhooks.txt")
                print(f"{Fore.YELLOW}Make sure you have a valid URL like:")
                print(f"{Fore.YELLOW}https://discord.com/api/webhooks/123456789/ABCDEFGHIJKLMNOP")
                return
            
            if not messages:
                print(f"{Fore.RED}No messages found in messages.txt")
                print(f"{Fore.YELLOW}Add some messages to messages.txt")
                return
            
            print(f"{Fore.GREEN}Found {len(webhooks)} webhooks and {len(messages)} messages")
            print(f"{Fore.CYAN}Total sends: {len(webhooks) * len(messages)}")
            
            delay = input(f"{Fore.CYAN}Delay between sends (seconds, 0 for none): ").strip()
            delay = float(delay) if delay else 0
            
            shuffle = input(f"{Fore.CYAN}Shuffle order? (y/n): ").strip().lower()
            shuffle = shuffle == 'y'
            
            spam_all_webhooks_messages('webhooks.txt', 'messages.txt', delay, shuffle)
        else:
            print(f"{Fore.RED}Invalid choice")
            
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}Stopped by user")
    except Exception as e:
        print(f"{Fore.RED}Error: {str(e)}")
    
    print(f"\n{Fore.MAGENTA}Goodbye")

if __name__ == "__main__":
    main()
