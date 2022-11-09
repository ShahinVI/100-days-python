#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!");

rand_seed=  int(input("please provide the seed first:"));

nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password_list = [];
password_len = nr_letters+nr_numbers+nr_symbols;

le_list=[];
nu_list=[];
sy_list=[];

#list for letters
for ii in range(0,nr_letters):
  rand_le = random.randint(0,len(letters)-1);
  le_list.append(letters[rand_le]);
print(le_list);


#list for numbers
for jj in range(0,nr_numbers):
  rand_nu = random.randint(0,len(numbers)-1);
  nu_list.append(numbers[rand_nu]);
print(nu_list);


#list for symbols
for rr in range(0,nr_symbols):
  rand_sy = random.randint(0,len(symbols)-1);
  sy_list.append(symbols[rand_sy]);
print(sy_list);

easypassword=le_list+nu_list+sy_list;

#print(easypassword);
easy_string=""
for q in easypassword:
  easy_string+=q;
print("\nthis is easy pass: "+easy_string);

for pp in range(0,password_len):
  rand_hp = random.randint(0,len(easypassword)-1);
  password_list.append(easypassword[rand_hp]);
  easypassword.remove(easypassword[rand_hp]);

#print(password_list);
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P



pass_string=""
for p in password_list:
  pass_string+=p;
print("\nthis is hard pass: "+pass_string);

#################
##another solution
password_list2=[];

#list for letters
for ii in range(0,nr_letters):
  password_list2.append(random.choice(letters));

#list for numbers
for jj in range(0,nr_numbers):
  password_list2.append(random.choice(numbers));

#list for symbols
for rr in range(0,nr_symbols):
  password_list2.append(random.choice(symbols));
#print(password_list2);

easy_string=""
for q in password_list2:
  easy_string+=q;
print("\nthis is easy pass: "+easy_string);

random.shuffle(password_list2);
#print(password_list2);

pass_string="";
for p in password_list2:
  pass_string+=p;
print("\nthis is hard pass: "+pass_string);