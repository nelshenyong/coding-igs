#include <iostream>

int main()
{
    int alas, sisi1, sisi2, tinggi, hasil_luas, hasil_keliling;
    std::cout << "Masukkan nilai alas: ";
    std::cin >> alas;
    std::cout << "Masukkan nilai Sisi 1: ";
    std::cin >> sisi1;
    std::cout << "Masukkan nilai Sisi 2: ";
    std::cin >> sisi2;
    std::cout << "Masukkan nilai Tinggi: ";
    std::cin >> tinggi;

    hasil_keliling = alas + sisi1 + sisi2;
    std::cout << "Hasil keliling dari " << alas << " + " << sisi1 << " + " << sisi2 << " = " << hasil_keliling << std::endl;

    hasil_luas = 2 * (alas + tinggi);
    std::cout << "Hasil luas dari 2 * (" << alas << " + " << tinggi << ") = " << hasil_luas << std::endl;

    return 0;
}