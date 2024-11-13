#include <string>
#include <map>

void BiodataKu(const std::string& nama, const std::string& jenisKelamin, const std::string& email) {
    std::cout << "BIODATAKU" << std::endl;
    std::cout << ": " << nama << std::endl;
    std::cout << ": " << jenisKelamin << std::endl;
    std::cout << ": " << email << std::endl;
}

void BiodataAyahKu(const std::string& nama, const std::string& pekerjaan, const std::string& email) {
    std::cout << "BIODATA AYAHKU" << std::endl;
    std::cout << ": " << nama << std::endl;
    std::cout << ": " << email << std::endl;
    std::cout << ": " << pekerjaan << std::endl;
}

void BiodataIbuku(const std::string& nama, const std::string& pekerjaan, const std::string& email) {
    std::cout << "BIODATA IBUKU" << std::endl;
    std::cout << ": " << nama << std::endl;
    std::cout << ": " << email << std::endl;
    std::cout << ": " << pekerjaan << std::endl;
}

int main() {
    std::string myName = "Pinky";
    std::string myGender = "Perempuan";
    std::string myEmail = "pinky@gmail.com";

    std::string fatherName = "Adi";
    std::string fatherJob = "guru";
    std::string fatherEmail = "adi@gmail.com";

    std::string motherName = "anisah";
    std::string motherJob = "guru";
    std::string motherEmail = "anisah@gmail.com";

    BiodataKu(myName, myGender, myEmail);
    BiodataAyahKu(fatherName, fatherJob, fatherEmail);
    BiodataIbuku(motherName, motherJob, motherEmail);

    return 0;
}