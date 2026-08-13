using System;
using System.Net.Http;
using System.Text;
using System.Threading.Tasks;

namespace multitool
{
    internal class Program
    {
        static async Task Main(string[] args)
        {
            Console.Title = "> made by @blcklarper";

            banner();
            menu();

            ConsoleKeyInfo input = Console.ReadKey(true);

            switch (input.KeyChar)
            {
                case 'a':
                    await webhookMessage();
                    break;

                case 'e':
                    return;
            }

            Console.WriteLine("\nPress any key to continue...");
            Console.ReadKey();
        }

        static void banner()
        {
            Console.WriteLine(@"
 ███▄ ▄███▓ █    ██  ██▓  ▄▄▄█████▓ ██▓▄▄▄█████▓ ▒█████   ▒█████   ██▓    
▓██▒▀█▀ ██▒ ██  ▓██▒▓██▒  ▓  ██▒ ▓▒▓██▒▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒    
▓██    ▓██░▓██  ▒██░▒██░  ▒ ▓██░ ▒░▒██▒▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    
▒██    ▒██ ▓▓█  ░██░▒██░  ░ ▓██▓ ░ ░██░░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░    
▒██▒   ░██▒▒▒█████▓ ░██████▒▒██▒ ░ ░██░  ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒
░ ▒░   ░  ░░▒▓▒ ▒ ▒ ░ ▒░▓  ░▒ ░░   ░▓    ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░
░  ░      ░░░▒░ ░ ░ ░ ░ ▒  ░  ░     ▒ ░    ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░
░      ░    ░░░ ░ ░   ░ ░   ░       ▒ ░  ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   
       ░      ░         ░  ░        ░               ░ ░      ░ ░      ░  ░
");
        }

        static void menu()
        {
            Console.WriteLine("\nto exit jst type e");
            Console.WriteLine("a. send webhook message");
            Console.Write("\n> ");
        }

        static async Task webhookMessage()
        {
            Console.Clear();

            Console.Write("webhook url : ");
            string webhook = Console.ReadLine();

            Console.Write("message : ");
            string message = Console.ReadLine();

            string json = $"{{\"content\":\"{message.Replace("\\", "\\\\").Replace("\"", "\\\"")}\"}}";

            using (HttpClient client = new HttpClient())
            using (HttpContent content = new StringContent(json, Encoding.UTF8, "application/json"))
            {
                HttpResponseMessage response = await client.PostAsync(webhook, content);

                Console.WriteLine(response.IsSuccessStatusCode
                    ? "\ndone"
                    : $"\n error : {(int)response.StatusCode} {response.StatusCode}");
            }
        }
    }
}