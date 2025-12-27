import random
def game():
    score= random.randint(1,100)
    with open("Hiscore.txt") as f:
        hiscore=int(f.read())
    if(score>hiscore or hiscore==""):
        return score
a=(game())
f=open("Hiscore.txt","w")
f.write(a)
f.close()
