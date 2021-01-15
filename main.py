from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)    

def caesar(textInput, shiftInput, directionInput):
      shiftAlphabet = alphabet[shiftInput:] + alphabet[:shiftInput]
      textInput = list(textInput)

      if shiftInput > len(shiftAlphabet) - 1:
        print("Error: Shift out of range")
      else:
        chiper_text = ""
        for i in textInput:
          if directionInput == "encode":
            if i in alphabet:
              chiper_text += shiftAlphabet[alphabet.index(i)] 
          elif directionInput == "decode":
            if i in shiftAlphabet:
              chiper_text += alphabet[shiftAlphabet.index(i)]
      print(f"Result {chiper_text}")

#loop the app
should_continue = True
while should_continue: 
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  caesar(textInput = text, shiftInput = shift, directionInput = direction)

  continue_app = input("Exit the app? Y / N ? ")
  continue_app.lower()
  if continue_app == "y":
    should_continue = False