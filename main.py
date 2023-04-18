def login():
  print("Clarance login System")
  print()
  
  while True:
    username=input("What is your username?: ")
    password=input("What is your password?: ")
    print()
    if username=="theo" and password=="baldies4life":
      print("Welcome to ClaranceLTD")
      break
    else:
      print("Whoops! I don't recognize that username or password. Try again!")
      continue

login()