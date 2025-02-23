import os
import pywhatkit

def result(file_name):
    res = {}
    with open(file_name, 'r') as a:
        for line in a:
            user, bot = line.strip().split('|')
            res[user] = bot
    return res

conres = ''

print('Hai..I am your chatbot please select an option to know about our institution..',
      'enter department to know ',  sep='\n')

conres += 'bot: Hai..I am your chatbot please select an option to know about our institution........enter department to know    '
response = input().lower()
conres += "You: " + response + '     '
if response=='department':
    aa=open("department.txt")
    b=aa.read()
    c=b.split('\n')
    for i in range(8):
        if c[i].startswith(str(i)):
            d=c[i].split(str(i))
    print("Here is the information!!!","Please select further options")
    conres+="bot: Here is the information!!! Please select further options     "
    for j in range(0,len(c),5):
        print(c[j])
    for i in range(len(c)):
        response1=str(input('enter any of the above question or stop to exit')).strip().lower()
        conres+='bot: enter any of the above question or stop to exit        '+ "You:"+response1+'      '
        if response1 in c:
            t=c.index(response1)
            for i in range(1,5):
                r=c[int(t)+i]
                print(r)
                conres+=r+'     '
        if response1 == 'stop':
            response2 = input("Do you want to chat with bot?? Type Yes or No")
            conres += "bot: Do you want to chat with bot?? Type Yes or No" + '      ' + 'You:' + response2 + '       '
            
            if response2.lower() == 'yes':
                res = result('responses.txt')
                print(res)
                print("bot: Hi! I'm your chatbot. Ask me something or say 'bye' to exit.")
                
                while True:
                    user = input("You:").strip().lower()
                    conres += 'You:' + user + '   '
                    
                    if user == 'bye':
                        print("bot: Goodbye!")
                        conres += "bot: Goodbye!"
                        break
                    if user in res:
                        bot = res[user]
                        print("bot:", bot)
                        conres += 'bot:' + bot + '   '
                    else:
                        print("bot: I'm sorry, I don't understand that.")
                        conres += "bot: I'm sorry, I don't understand that." + '   '
                break
            else:
                break
print(conres)
finalres = conres.split('   ')
lines = []

for k in finalres:
    if ':' in k:
       sender, message = k.split(':',1)
       lines.append(f"{sender}:{message}")

output_msg = '\n'.join(lines)
print(output_msg)

mob_no = input("enter the mobile number to send the conversation:")
mob_no = "+91" + mob_no
pywhatkit.sendwhatmsg_instantly(mob_no, output_msg)
aa.close()
