using System.Net;
using System.Text.RegularExpressions;

class Site
{
    public string Url { get; init; } = "";
    public string[] NotFound { get; init; } = Array.Empty<string>();
}

class Program
{
    static readonly List<Site> Sites = new()
    {
        new() { Url = "https://github.com/{u}", NotFound = ["Not Found"] },
        new() { Url = "https://gitlab.com/{u}", NotFound = ["The page you're looking for doesn't exist"] },
        new() { Url = "https://www.reddit.com/user/{u}/", NotFound = ["Sorry, nobody on Reddit goes by that name"] },
        new() { Url = "https://medium.com/@{u}", NotFound = ["Page not found"] },
        new() { Url = "https://dev.to/{u}", NotFound = ["404"] },
        new() { Url = "https://keybase.io/{u}", NotFound = ["Page not found"] },
        new() { Url = "https://www.twitch.tv/{u}", NotFound = ["Sorry. Unless you've got a time machine"] },
        new() { Url = "https://steamcommunity.com/id/{u}", NotFound = ["The specified profile could not be found"] },
        new() { Url = "https://www.pinterest.com/{u}/", NotFound = ["Sorry! We couldn't find that page"] },
        new() { Url = "https://{u}.tumblr.com/", NotFound = ["There's nothing here"] },
        new() { Url = "https://soundcloud.com/{u}", NotFound = ["We can't find that user"] },
        new() { Url = "https://codepen.io/{u}", NotFound = ["Page Not Found"] },
        new() { Url = "https://hackerone.com/{u}", NotFound = ["Page not found"] },
        new() { Url = "https://pastebin.com/u/{u}", NotFound = ["User not found"] },
        new() { Url = "https://replit.com/@{u}", NotFound = ["404"] },
        new() { Url = "https://www.npmjs.com/~{u}", NotFound = ["Page Not Found"] },
        new() { Url = "https://pypi.org/user/{u}/", NotFound = ["404 Not Found"] },
        new() { Url = "https://hub.docker.com/u/{u}", NotFound = ["Page not found"] },
        new() { Url = "https://en.wikipedia.org/wiki/User:{u}", NotFound = ["does not exist"] },
        new() { Url = "https://www.flickr.com/people/{u}/", NotFound = ["Page Not Found"] },
        new() { Url = "https://gravatar.com/{u}", NotFound = ["Page not found"] },
        new() { Url = "https://www.patreon.com/{u}", NotFound = ["Page not found"] },
        new() { Url = "https://ko-fi.com/{u}", NotFound = ["Page not found"] },
        new() { Url = "https://buymeacoffee.com/{u}", NotFound = ["Page not found"] },
        new() { Url = "https://linktr.ee/{u}", NotFound = ["Page not found"] },
        new() { Url = "https://about.me/{u}", NotFound = ["Page not found"] },
        new() { Url = "https://disqus.com/by/{u}/", NotFound = ["We couldn't find"] },
        new() { Url = "https://www.behance.net/{u}", NotFound = ["Page Not Found"] },
        new() { Url = "https://dribbble.com/{u}", NotFound = ["Page not found"] },
        new() { Url = "https://vimeo.com/{u}", NotFound = ["Sorry, we couldn't find"] },
        new() { Url = "https://www.mixcloud.com/{u}/", NotFound = ["Page not found"] },
        new() { Url = "https://bandcamp.com/{u}", NotFound = ["Sorry, that page doesn't exist"] },
        new() { Url = "https://www.last.fm/user/{u}", NotFound = ["Page not found"] },
        new() { Url = "https://letterboxd.com/{u}/", NotFound = ["Page not found"] },
        new() { Url = "https://www.goodreads.com/{u}", NotFound = ["Page not found"] },
        new() { Url = "https://www.kaggle.com/{u}", NotFound = ["404"] },
        new() { Url = "https://huggingface.co/{u}", NotFound = ["404"] },
        new() { Url = "https://stackoverflow.com/users/{u}", NotFound = ["Page not found"] },
        new() { Url = "https://stackexchange.com/users/{u}", NotFound = ["Page not found"] },
        new() { Url = "https://sourceforge.net/u/{u}/profile/", NotFound = ["404"] },
        new() { Url = "https://bitbucket.org/{u}/", NotFound = ["Page not found"] },
        new() { Url = "https://gitea.com/{u}", NotFound = ["Page Not Found"] },
        new() { Url = "https://codeberg.org/{u}", NotFound = ["Page Not Found"] },
        new() { Url = "https://archive.org/details/@{u}", NotFound = ["Page not found"] },
        new() { Url = "https://myanimelist.net/profile/{u}", NotFound = ["404"] },
        new() { Url = "https://anilist.co/user/{u}/", NotFound = ["Page Not Found"] },
        new() { Url = "https://www.chess.com/member/{u}", NotFound = ["Not Found"] },
        new() { Url = "https://lichess.org/@/{u}", NotFound = ["404"] },
        new() { Url = "https://www.speedrun.com/users/{u}", NotFound = ["404"] },
        new() { Url = "https://scratch.mit.edu/users/{u}/", NotFound = ["404"] },
        new() { Url = "https://itch.io/profile/{u}", NotFound = ["not found"] },
        new() { Url = "https://gamejolt.com/@{u}", NotFound = ["404"] },
        new() { Url = "https://modrinth.com/user/{u}", NotFound = ["404"] },
        new() { Url = "https://www.spigotmc.org/members/{u}/", NotFound = ["The specified member cannot be found"] },
        new() { Url = "https://unsplash.com/@{u}", NotFound = ["Page not found"] },
        new() { Url = "https://www.deviantart.com/{u}", NotFound = ["Page Not Found"] },
        new() { Url = "https://www.artstation.com/{u}", NotFound = ["Page not found"] },
        new() { Url = "https://500px.com/p/{u}", NotFound = ["Page not found"] },
        new() { Url = "https://imgur.com/user/{u}", NotFound = ["Page Not Found"] },
        new() { Url = "https://giphy.com/{u}", NotFound = ["Page not found"] },
        new() { Url = "https://tenor.com/users/{u}", NotFound = ["Page not found"] },
        new() { Url = "https://www.producthunt.com/@{u}", NotFound = ["Page not found"] },
        new() { Url = "https://www.fiverr.com/{u}", NotFound = ["Page not found"] },
        new() { Url = "https://www.freelancer.com/u/{u}", NotFound = ["Page not found"] },
        new() { Url = "https://www.researchgate.net/profile/{u}", NotFound = ["Page not found"] },
        new() { Url = "https://www.instructables.com/member/{u}/", NotFound = ["404"] },
        new() { Url = "https://hackaday.io/{u}", NotFound = ["404"] },
        new() { Url = "https://lobste.rs/~{u}", NotFound = ["No such user"] },
        new() { Url = "https://news.ycombinator.com/user?id={u}", NotFound = ["No such user"] }
    };

    static readonly HttpClient Client = CreateClient();

    static HttpClient CreateClient()
    {
        var handler = new HttpClientHandler
        {
            AutomaticDecompression =
                DecompressionMethods.GZip |
                DecompressionMethods.Deflate |
                DecompressionMethods.Brotli,

            AllowAutoRedirect = true
        };

        var client = new HttpClient(handler)
        {
            Timeout = TimeSpan.FromSeconds(8)
        };

        client.DefaultRequestHeaders.UserAgent.ParseAdd(
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) " +
            "AppleWebKit/537.36 (KHTML, like Gecko) " +
            "Chrome/131.0 Safari/537.36"
        );

        return client;
    }

    static async Task Main()
    {
        while (true)
        {
            Console.Write("* ");

            string? username = Console.ReadLine()?.Trim();

            if (string.IsNullOrWhiteSpace(username))
                continue;

            if (!Regex.IsMatch(
                username,
                @"^[a-zA-Z0-9._-]{1,64}$"))
            {
                continue;
            }

            using var semaphore = new SemaphoreSlim(8);

            var tasks = Sites.Select(async site =>
            {
                await semaphore.WaitAsync();

                try
                {
                    bool exists = await CheckSite(site, username);

                    if (exists)
                    {
                        string profileUrl =
                            site.Url.Replace(
                                "{u}",
                                Uri.EscapeDataString(username)
                            );

                        lock (Console.Out)
                        {
                            Console.ForegroundColor =
                                ConsoleColor.Green;

                            Console.WriteLine(
                                $"[+] {profileUrl}"
                            );

                            Console.ResetColor();
                        }
                    }
                }
                finally
                {
                    semaphore.Release();
                }
            });

            await Task.WhenAll(tasks);
        }
    }

    static async Task<bool> CheckSite(
        Site site,
        string username)
    {
        string url = site.Url.Replace(
            "{u}",
            Uri.EscapeDataString(username)
        );

        try
        {
            using var request =
                new HttpRequestMessage(
                    HttpMethod.Get,
                    url
                );

            using var response =
                await Client.SendAsync(
                    request,
                    HttpCompletionOption.ResponseHeadersRead
                );

            if (response.StatusCode ==
                    HttpStatusCode.NotFound ||
                response.StatusCode ==
                    HttpStatusCode.Gone)
            {
                return false;
            }

            if (!response.IsSuccessStatusCode)
                return false;

            string body =
                await response.Content.ReadAsStringAsync();

            if (string.IsNullOrWhiteSpace(body))
                return false;

            foreach (string marker in site.NotFound)
            {
                if (body.Contains(
                    marker,
                    StringComparison.OrdinalIgnoreCase))
                {
                    return false;
                }
            }

            return true;
        }
        catch
        {
            return false;
        }
    }
}
