// === DATO CHE NON MI RICORDO SE QUESTO CODICE È PIENO DI BUG/FINITO NON ASPETTARTI NULLA E SE VUOI AIUTARMI ===
// === A SISTEMARE IL CODICE SCRIVIMI SU DISCORD: @ninjaecse ===


#include <iostream>
#include <string>
#include <list>
#include <cstdlib>
#include <cwchar>
using namespace std;

#include "olcConsoleGameEngine.h"

class OneLoneCoder_FlappyBird : public olcConsoleGameEngine
{
public:
    OneLoneCoder_FlappyBird()
    {
        m_sAppName = L"Flappy Bird";
    }

private:
    float fBirdPosition = 0.0f;
    float fBirdVelocity = 0.0f;
    float fBirdAcceleration = 0.0f;

    float fGravity = 100.0f;


    float fSectionWidth;
    list<int> listSections;
    float fLevelPosition = 0.0f;

protected:
    virtual bool OnUserCreate()
    {
        listSections = { 0, 0, 0, 0 };
        fSectionWidth = (float)ScreenWidth() / (float)(listSections.size() - 1);
        return true;
    }

    virtual bool OnUserUpdate(float fElapsedTime)
    {
        if (m_keys[VK_SPACE].bPressed && fBirdVelocity >= fGravity / 10.0f)
        {
            fBirdAcceleration = 0.0f;
            fBirdVelocity = -fGravity / 4.0f;
        }
        else
            fBirdAcceleration += fGravity * fElapsedTime;

        if (fBirdAcceleration >= fGravity)
            fBirdAcceleration = fGravity;

        fBirdVelocity += fBirdAcceleration * fElapsedTime;
        fBirdPosition += fBirdVelocity * fElapsedTime;

        fLevelPosition += 14.0f * fElapsedTime;

        if (fLevelPosition > fSectionWidth)
        {
            fLevelPosition -= fSectionWidth;
            listSections.pop_front();
            int i = rand() % (ScreenHeight() - 20);
            if (i < 10) i = 0;
            listSections.push_back(i);
        }

        Fill(0,0, ScreenWidth(), ScreenHeight(), L' ');

        int nSection = 0;
        for (auto s : listSections)
        {
            if (s != 0)
            {
                int x1 = (int)(nSection * fSectionWidth + 10 - fLevelPosition);
                int x2 = (int)(nSection * fSectionWidth + 15 - fLevelPosition);
                int y1 = ScreenHeight() - s;
                int y2 = ScreenHeight();
                int w = x2 - x1;
                int h = y2 - y1;
                if (w > 0 && h > 0)
                    Fill(x1, y1, w, h, L'#');

                int top_y2 = ScreenHeight() - s - 15;
                int top_h = y1 - top_y2;
                if (w > 0 && top_h > 0)
                    Fill(x1, top_y2, w, top_h, L'#');
            }
            nSection++;
        }

        int nBirdX = (int)(ScreenWidth() / 3.0f);

        if (fBirdVelocity > 0.0f)
        {
            DrawString(nBirdX, (int)fBirdPosition + 0, L"\\\\\\");
            DrawString(nBirdX, (int)fBirdPosition + 1, L"\\\\\\=Q");
        }
        else
        {
            DrawString(nBirdX, (int)fBirdPosition + 0, L"///=Q");
            DrawString(nBirdX, (int)fBirdPosition + 1, L"///");
        }

        wchar_t buf[128];
        swprintf(buf, 128, L"Pos: %.1f Vel: %.1f Acc: %.1f", fBirdPosition, fBirdVelocity, fBirdAcceleration);
        DrawString(0, 0, buf);
        swprintf(buf, 128, L"LevelPos: %.1f Sections: %zu", fLevelPosition, listSections.size());
        DrawString(0, 1, buf);

        return true;
    }
};

int main()
{
    OneLoneCoder_FlappyBird game;
    if (game.ConstructConsole(80, 48, 16, 16))
        game.Start();

    return 0;
}
