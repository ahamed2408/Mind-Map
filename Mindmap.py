class Mindmap:
    
    #initializing Variables
    def __init__(self):
	    self.l=[]    
	    self.x=0

    #Function to insert the values to the cards
    def insert(self):

        for i in range(self.x):
            m=[]
            for j in range(self.x):
                sm=[]
                name=input("Enter name")
                reveal=opencl=notim=0
                sm.append(name)
                sm.append(opencl)
                sm.append(notim)
                sm.append(reveal)
                m.append(sm)
            self.l.append(m)
        print("The Matrix is: \n",self.l)

    #Function to Reveal the cards    
    def reveal_card(self):    
        rounds=0
        counts=0
        out=(self.x*2)//2
        while True:
            if(counts==out):
                break
            rounds+=1
            print("Round",rounds)
            a,b=map(int,input("User: ").split(","))
            a-=1
            b-=1
            self.l[a][b][2]+=1

            if(self.l[a][b][3]==1):
                print("Already Revealed")
            else:
                print("Output: Reveal",self.l[a][b][0])
               # l[a][b][1]=1
                    
            c,d=map(int,input("User: ").split(","))
            c-=1
            d-=1
            while(a==c and b==d):
                print("Can't open same card\n<Another chance for second card>")
                c,d=map(int,input("User: ").split(","))
                c-=1
                d-=1
            if(self.l[c][d][3]==1):
                print("Already Revealed")
            else:
                print("Output: Reveal",self.l[c][d][0])
            
            self.l[c][d][2]+=1
            if(self.l[a][b][0]==self.l[c][d][0]):
                self.l[a][b][3]=1
                self.l[c][d][3]=1
                print("Output:Good Job!")
                counts+=1
                if(counts==out):
                    break
            else:
                print("Output: Closing both cards")
            if(self.l[a][b][2]==4 or self.l[c][d][2]==4 ):
                print("output:Game over")
                break
            print("\n")



# Main Function
# Object of the class Mindmap
mindmap = Mindmap()

while True:
    print("\nEnter the size of Matrix.Example Input: 2 2(for 2x2 matrix)")
    i,j=map(int,input().split(" "))
    if(i==j and i%2==0):
        mindmap.x=i
        break
    else:    
        print("Wrong Size Input")    
print("Next step")
mindmap.insert()
mindmap.reveal_card()
print("End of program. Press any key to continue.")
input()
   


    
   

        
    

