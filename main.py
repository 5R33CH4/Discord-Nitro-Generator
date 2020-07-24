import random, string
print("\nᴅɪsᴄᴏʀᴅ ɴɪᴛʀᴏ ɢᴇɴᴇʀᴀᴛᴏʀ")
print("Note: Only Use This for testing purposes.")
print("by Quantum Pirate#1011\n")
amount = int(input('Amount of nitro codes to generate: '))
value = 1
while value <= amount:
    code = "https://discord.gift/" + ('').join(random.choices(string.ascii_letters + string.digits, k=16))
    f = open('Codes.txt', "a+")
    f.write(f'{code}\n')
    f.close()
    print(f'[GENERATED] {code}')
    value += 1
