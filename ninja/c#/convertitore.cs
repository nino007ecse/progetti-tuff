using System;

class Program
{
    static void Main(string [] args)
    {
        Console.Write("Inserisci un'età umana: ");

        string input = Console.ReadLine();
        int etaUmana;

        if (int.TryParse(input, out etaUmana))
        {
            int etaCanina;

            if (etaUmana <= 0)
            {
                Console.WriteLine("L'età deve essere maggiore di 0");
                return;
            }
            else if (etaUmana == 1)
            {
                etaCanina = 15;
            }
            else if (etaUmana == 2)
            {
                etaCanina = 24;
            }
            else
            {
                etaCanina = 24 + ((etaUmana - 2)* 5);
            }
            Console.WriteLine($"In età canina equivalgono a circa: {etaCanina} anni!");
        }
        else
        {
            Console.WriteLine("Devi inserire un numero valido!");
        }
    }
}
