# codice fatto da : blck/blck67 
# per qualsiasi cosa scrivermi su ds : lasciato
# per aiutarmi nello script scrivermi su ds
# ------------------------------------------------------------------------
# dovete creare un file webhooks.txt dove mettete SOLO i link dei webhooks dalla APP DI DISCORD
# dovete creare un file messages.txt dove mettete i messaggi da inviare

import requests
import time
import os
import random

def send_webhook(webhook_url, message):
    try:
        data = {"content": message, "tts": False}
        response = requests.post(webhook_url, json=data)
        if response.status_code == 204:
            return True
        else:
            return False
    except:
        return False

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
    except:
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
    except:
        return None

def spam_all(webhooks_file='webhooks.txt', messages_file='messages.txt', delay=0):
    webhooks = read_webhooks(webhooks_file)
    if not webhooks:
        print("No webhooks found")
        return
    
    messages = read_messages(messages_file)
    if not messages:
        print("No messages found")
        return
    
    total = len(webhooks) * len(messages)
    success = 0
    failed = 0
    counter = 0
    
    print(f"Webhooks: {len(webhooks)}")
    print(f"Messages: {len(messages)}")
    print(f"Total: {total}")
    if delay > 0:
        print(f"Delay: {delay}s")
    print()
    
    for webhook in webhooks:
        for message in messages:
            counter += 1
            print(f"[{counter}/{total}] Sending: {message[:30]}")
            
            if send_webhook(webhook, message):
                success += 1
                print("  OK")
            else:
                failed += 1
                print("  FAIL")
            
            if delay > 0 and counter < total:
                time.sleep(delay)
    
    print()
    print(f"Success: {success}/{total}")
    print(f"Failed: {failed}/{total}")

def create_files():
    if not os.path.exists('webhooks.txt'):
        with open('webhooks.txt', 'w', encoding='utf-8') as f:
            f.write("https://discord.com/api/webhooks/ID/TOKEN\n")
        print("Created webhooks.txt")
    
    if not os.path.exists('messages.txt'):
        with open('messages.txt', 'w', encoding='utf-8') as f:
            f.write("Hello from webhook\n")
            f.write("Test message 2\n")
            f.write("Message 3\n")
        print("Created messages.txt")

def main():
    create_files()
    
    webhooks = read_webhooks('webhooks.txt')
    messages = read_messages('messages.txt')
    
    if not webhooks:
        print("Add webhooks to webhooks.txt")
        return
    
    if not messages:
        print("Add messages to messages.txt")
        return
    
    print(f"Found {len(webhooks)} webhooks and {len(messages)} messages")
    print(f"Total sends: {len(webhooks) * len(messages)}")
    
    delay = input("Delay (seconds, 0 for none): ").strip()
    delay = float(delay) if delay else 0
    
    spam_all('webhooks.txt', 'messages.txt', delay)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nStopped")
