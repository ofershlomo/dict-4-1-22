prices={
"apples":10,
"banana":6,
"mango":50,
"nuggies":15,
"cheddar":23
}

ShopCart={
"apples":3,
"mango":4,
"nuggies":6,
}


total=0

for x in ShopCart:
  total+= ShopCart[x]*prices[x]

print("your total is : ", total)