#include <iostream>
#include <string>
#include <cstdlib>
#include <ctime>
#include <fstream>

using namespace std;

// '£' won't print. wonder why?
string char_set1 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!\"$%^&*()-_=+[{]};:'@#~|,<.>/?";
string char_set2 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890";
string char_set3 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
string char_set4 = "abcdefghijklmnopqrstuvwxyz1234567890";
string char_set5 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890";
string char_set6 = "abcdefghijklmnopqrstuvwxyz";
string char_set7 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
string char_set8 = "1234567890";
string char_set9 = "custom set";
string characters = "";

string choose_char()
{
  int char_set = 0;
  cout <<"1. "<<char_set1<<endl<<"2. "<<char_set2<<endl<<"3. "<<char_set3<<endl<<"4. "<<char_set4<<endl<<"5. "<<char_set5<<endl<<"6. "<<char_set6<<endl<<"7. "<<char_set7<<endl<<"8. "<<char_set8<<endl<<"9. "<<char_set9<<endl<<"Choose set of characters 1-9: ";
  cin >> char_set;
  switch(char_set){
  case 1:
    return char_set1;
    break;
  case 2:
    return char_set2;
    break;
  case 3:
      return char_set3;
      break;
  case 4:
      return char_set4;
      break;
  case 5:
      return char_set5;
      break;
  case 6:
      return char_set6;
      break;
  case 7:
      return char_set7;
      break;
  case 8:
      return char_set8;
      break;
  case 9:
      
      cout << "Input Characters to use: ";
      cin >> char_set9;
      return char_set9;
      break;
  default:
      return "[!!] NO CHARACTER SET CHOSEN";
  }
}


void generate(string chars)
{
  ofstream myfile;
  myfile.open("list.txt");
  int char_len = chars.length(); int pass_len; int multi; string password; 
  
  cout << "How long is the password?: ";
  cin >> pass_len;

  cout << "How many passwords?: ";
  cin >> multi;
  
  srand(time(0));
  string passwords[multi];
  
  for(int x=0; x<multi; x++) {
    for(int y=0; y<pass_len; y++) {
      int ran_num = (rand () % char_len);
      string ran_char;
      ran_char = chars[ran_num];
      password += ran_char;
    }
    passwords[x] = password;  
    password = "";
    //cout << passwords[x]<< endl;
    myfile << passwords[x] << endl;
  }
  myfile.close();
}


int main()
{

  string characters = choose_char();
  generate(characters);

}
