// Minimal stub of olcConsoleGameEngine to allow compilation of examples
#ifndef OLC_CONSOLE_GAME_ENGINE_H
#define OLC_CONSOLE_GAME_ENGINE_H

#include <string>
#include <iostream>
#include <vector>
#include <chrono>
#include <thread>
#include <unistd.h>
#include <termios.h>
#include <sys/select.h>

#define VK_SPACE 0x20

struct sKey { bool bPressed = false; };

class olcConsoleGameEngine {
public:
    std::wstring m_sAppName;
    sKey m_keys[256];
    int m_nScreenWidth = 80;
    int m_nScreenHeight = 48;
    std::vector<wchar_t> m_bufScreen;

    virtual ~olcConsoleGameEngine() = default;
    virtual bool OnUserCreate() { return true; }
    virtual bool OnUserUpdate(float) { return true; }

    bool ConstructConsole(int w, int h, int /*px*/, int /*py*/)
    {
        m_nScreenWidth = w;
        m_nScreenHeight = h;
        m_bufScreen.assign(m_nScreenWidth * m_nScreenHeight, L' ');
        return true;
    }

    void Start()
    {
        if (!OnUserCreate()) return;
        std::cout << "\x1b[2J"; // clear screen
        std::cout << "\x1b[?25l"; // hide cursor
        if (m_bufScreen.empty()) m_bufScreen.assign(m_nScreenWidth * m_nScreenHeight, L' ');
        std::string instr = "Press SPACE to start, Q to quit";
        std::cout << instr << std::endl;

        struct termios oldt, newt;
        tcgetattr(STDIN_FILENO, &oldt);
        newt = oldt;
        newt.c_lflag &= ~(ICANON | ECHO);
        tcsetattr(STDIN_FILENO, TCSANOW, &newt);

        auto last = std::chrono::high_resolution_clock::now();
        bool running = true;
        while (running)
        {
            fd_set set;
            FD_ZERO(&set);
            FD_SET(STDIN_FILENO, &set);
            struct timeval tv = {0, 0};
            int rv = select(STDIN_FILENO + 1, &set, nullptr, nullptr, &tv);
            if (rv > 0)
            {
                char c;
                if (read(STDIN_FILENO, &c, 1) > 0)
                {
                    if (c == 'q' || c == 'Q') break;
                    m_keys[VK_SPACE].bPressed = (c == ' ');
                }
            }

            auto now = std::chrono::high_resolution_clock::now();
            std::chrono::duration<float> elapsed = now - last;
            last = now;

            std::fill(m_bufScreen.begin(), m_bufScreen.end(), L' ');

            running = OnUserUpdate(elapsed.count());

            for (int i = 0; i < 256; i++) if (i != VK_SPACE) m_keys[i].bPressed = false;
            m_keys[VK_SPACE].bPressed = false;

            std::cout << "\x1b[H";
            for (int y = 0; y < m_nScreenHeight; y++)
            {
                for (int x = 0; x < m_nScreenWidth; x++)
                {
                    wchar_t wc = m_bufScreen[y * m_nScreenWidth + x];
                    char c = (char)(wc == 0 ? ' ' : (wc > 127 ? '?' : wc));
                    std::cout << c;
                }
                std::cout << '\n';
            }
            std::cout << std::flush;

            std::this_thread::sleep_for(std::chrono::milliseconds(16));
        }

        tcsetattr(STDIN_FILENO, TCSANOW, &oldt);
        std::cout << "\x1b[?25h"; // show cursor
    }

    void Fill(int x, int y, int w, int h, wchar_t c)
    {
        if (w <= 0 || h <= 0) return;
        for (int iy = 0; iy < h; iy++)
        {
            int py = y + iy;
            if (py < 0 || py >= m_nScreenHeight) continue;
            for (int ix = 0; ix < w; ix++)
            {
                int px = x + ix;
                if (px < 0 || px >= m_nScreenWidth) continue;
                m_bufScreen[py * m_nScreenWidth + px] = c;
            }
        }
    }

    int ScreenWidth() { return m_nScreenWidth; }
    int ScreenHeight() { return m_nScreenHeight; }

    void DrawString(int x, int y, const wchar_t* s)
    {
        if (s == nullptr) return;
        int px = x;
        int py = y;
        while (*s)
        {
            if (*s == L'\n') { py++; px = x; s++; continue; }
            if (py >= 0 && py < m_nScreenHeight && px >= 0 && px < m_nScreenWidth)
                m_bufScreen[py * m_nScreenWidth + px] = *s;
            px++; s++;
        }
    }
};

#endif // OLC_CONSOLE_GAME_ENGINE_H
