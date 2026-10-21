from tkinter import *
root=Tk()
root.title('Calculator')
root.geometry('390x500+500+100')
buttons=[['1','2','3','AC','log'],['4','5','6','+','-'],['7','8','9','*','/'],['+/-','0','.','=','^']]
text=Entry(root,width=60,justify='right')
text.grid(row=0,columnspan=5,pady=10,ipady=15)
def bclick(x):
    text.insert(END,x)
for r,br in enumerate(buttons,start=1):
    for c,b in enumerate(br):
        Button(root,text=b,padx=5,width=8,height=5,fg='black',bg='aliceblue',command=lambda x=b:bclick(x)).grid(row=r,column=c)
root.mainloop()