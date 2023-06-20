from tkinter import * 
import pandas as pd


root=Tk()
root.title("Project")



# main frame 
f1=Frame(root, height=1000, width=1500, highlightbackground="blue", highlightthickness=4, padx=10, pady=10)
f1.propagate(0)



f1.pack()
#Title 
kkk=Label(f1, bg="white",fg="indigo", height=3, width=65, text="Welcome to the Flood Relief Camp Interface", font=("Caladea",30,"bold","underline"))
kkk.place(x=0, y=0)

img1=Canvas(f1, height=145, width=200, bg="white")
file1=PhotoImage(file="logo.gif")
img1.create_image(100,75,image=file1)
img1.place(x=0,y=0)




img2=Canvas(f1, height=145, width=295, bg="white")
file2=PhotoImage(file="nature.gif")
img2.create_image(125,100, image=file2)
img2.place(x=1150,y=0)

#frame 1
f1_frame1=LabelFrame(f1, height=600, width=700, padx=10, pady=10, text="Virtual Donation Box", font=("Caladea",20,"underline"))
f1_frame1.place(x=0, y=170, height=600, width=700)
f1_frame1.propagate(0)

img3=Canvas(f1_frame1, height=200, width=678, bg="white")
file3=PhotoImage(file="donation1.gif")
img3.create_image(340,100,image=file3)
img3.place(x=0, y=350)


b1=Button(f1_frame1,text="Confirm Payment", height=1, width=22, bg="blue",fg="white", activebackground="white", activeforeground="green",font=("Caladea",15,"bold"))
b2=Button(f1_frame1, text="Click to pay through \n Debit /Credit card", height=2, width=30, bg="blue",fg="white", activebackground="white", activeforeground="green",font=("Caladea",12,"bold"))



l1=Label(f1_frame1, text="Name: ", font=("Times New Roman",16))
l2=Label(f1_frame1, text="Country:  ", font=("Times New Roman",16))
l3=Label(f1_frame1, text="State:  ", font=("Times New Roman",16))
l4=Label(f1_frame1, text="City:  ", font=("Times New Roman",16))
l5=Label(f1_frame1, text="Pin code: ", font=("Times New Roman",16))
l6=Label(f1_frame1, text="Donation Amount:", font=("Times New Roman",16))
l7=Label(f1_frame1, text="Method of Payment: ", font=("Times New Roman",16))

t1=Text(f1_frame1, height=1,width=50,padx=0) # width=100, padx=10, pady=15)
t2=Text(f1_frame1, height=1,width=50) #width=100, padx=10, pady=15)
t3=Text(f1_frame1, height=1,width=50) #width=100, padx=10, pady=15)
t4=Text(f1_frame1, height=1,width=50) #width=100, padx=10, pady=15)
t5=Text(f1_frame1, height=1,width=50)
t6=Text(f1_frame1, height=1,width=50)
t7=Text(f1_frame1, height=1,width=50)



t1.grid(row=0, column=1,pady=10)#, padx=, pady=15)
t2.grid(row=1, column=1,pady=10)#, padx=10, pady=15)
t3.grid(row=2, column=1,pady=10)#, padx=10, pady=15)
t4.grid(row=3, column=1,pady=10)#, padx=10, pady=15)
t5.grid(row=4, column=1,pady=10)#, padx=10, pady=15)
t6.grid(row=5, column=1,pady=10)#, padx=10, pady=15)
t7.grid(row=6, column=1,pady=10)#, padx=10, pady=15)

l1.grid(row=0, column=0,sticky="E")#, padx=10, pady=15)
l2.grid(row=1, column=0,sticky="E")#, padx=10, pady=15)
l3.grid(row=2, column=0,sticky="E")#, padx=10, pady=15)
l4.grid(row=3, column=0,sticky="E")#, padx=10, pady=15)
l5.grid(row=4, column=0,sticky="E")#, padx=10, pady=15)
l6.grid(row=5, column=0,sticky="E")#, padx=10, pady=15)
l7.grid(row=6, column=0,sticky="E")#, padx=10, pady=15)

b1.place(x=2,y=300, height=50, width=300)
b2.place(x=380, y=300, height=50, width=300)


#The online payment through debit card interface 
def paymentinterface(xyz):
     
    root1=Tk()
    root1.title("Online Payment Interface ")
    fpay=Frame(root1, height=600, width=600, bg="white")
    flabelframe=LabelFrame(fpay, height=450, width=450, text="Enter Details", font=("Caladea",20,"underline"))
    
        
    fl1=Label(flabelframe, text="Debit/Credit Card Number :-", font=("Times New Roman",15))
    fl2=Label(flabelframe, text="Expiry Date (MM/DD):- ",font=("Times New Roman",15))
    fl3=Label(flabelframe, text="CVV / CVC :- ",font=("Times New Roman",15))
    fl4=Label(flabelframe, text="Name as on Card  :-",font=("Times New Roman",15))
    
    e1=Entry(flabelframe, width=67)
    val1=IntVar()
    s1=Spinbox(flabelframe, from_=1 , to=12, textvariable=val1, width=2 )
    
    
    val2=IntVar()
    s2=Spinbox(flabelframe, from_=2021, to=2030, textvariable=val2, width=2)
    
    e3=Entry(flabelframe, show="*")    
    e4=Entry(flabelframe, width=67)
    
    
    fl1.place(x=10,y=20)
    fl2.place(x=10,y=90)
    fl3.place(x=280,y=90)
    fl4.place(x=10,y=150)
    
    e1.place(x=15,y=50,height=30)
    s1.place(x=100,y=120,height=20, width=30)
    s2.place(x=140,y=120, height=20, width=40)
    e3.place(x=350,y=120, height=20, width=70)
    e4.place(x=15,y=175, height=30)
    
    
    def bsubclicked(xyz):
        
        name_var=t1.get(1.0,"end-1c")
        country_var=t2.get(1.0,"end-1c")
        state_var=t3.get(1.0,"end-1c")
        city_var=t4.get(1.0,"end-1c")
        pincode_var=t5.get(1.0,"end-1c")
        donationamount_var=t6.get(1.0,"end-1c")
        methodofpayment_var=t7.get(1.0,"end-1c")
    
        t1.delete("1.0","end")
        t1.delete("1.0","end")
        t2.delete("1.0","end")
        t3.delete("1.0","end")
        t4.delete("1.0","end")
        t5.delete("1.0","end")
        t6.delete("1.0","end")
        t7.delete("1.0","end")
    
        df1=pd.read_excel("List.xlsx")
    

        df1.loc[len(df1.index)]=[name_var,country_var,state_var,city_var, pincode_var, donationamount_var, methodofpayment_var]
   
        df1.to_excel("List.xlsx",index=False)
    
    
        
        
        e1.delete(0, END)
        s1.delete(0, END)
        s2.delete(0, END)        
        e3.delete(0, END)
        e4.delete(0, END)
        
        lble=Label(flabelframe, text="Payment successful, Fill details for more transaction or click Return ", font=("Caladea",11))
        lble.place(x=15, y=350)
    def bsub2clicked(xyz):
        root1.destroy()
        
        
    bsub=Button(flabelframe, height=2, width=15, text="Confirm Payment", font=("Caladea",15,"bold",), bg="green",fg="white", activebackground="blue", activeforeground="white")
    bsub.bind("<Button-1>",bsubclicked)
    
    bsub2=Button(flabelframe, height=2, width=15, text="Return",font=("Caladea",15,"bold",), bg="red",fg="white", activebackground="blue", activeforeground="white")
    bsub2.bind("<Button-1>",bsub2clicked)
    
    bsub.place(x=220, y=250)
    bsub2.place(x=15, y=250)
        
    fpay.propagate(0)
    fpay.pack()
    flabelframe.pack()
    root1.mainloop()

b2.bind("<Button-1>",paymentinterface)


# Confirm payment and store user input 
def confirmpaymentfunction(xyz):
    name_var=t1.get(1.0,"end-1c")
    country_var=t2.get(1.0,"end-1c")
    state_var=t3.get(1.0,"end-1c")
    city_var=t4.get(1.0,"end-1c")
    pincode_var=t5.get(1.0,"end-1c")
    donationamount_var=t6.get(1.0,"end-1c")
    methodofpayment_var=t7.get(1.0,"end-1c")
    
    t1.delete("1.0","end")
    t1.delete("1.0","end")
    t2.delete("1.0","end")
    t3.delete("1.0","end")
    t4.delete("1.0","end")
    t5.delete("1.0","end")
    t6.delete("1.0","end")
    t7.delete("1.0","end")
    
    df1=pd.read_excel("List.xlsx")
    

    df1.loc[len(df1.index)]=[name_var,country_var,state_var,city_var, pincode_var, donationamount_var, methodofpayment_var]
   
    df1.to_excel("List.xlsx",index=False)
    
    
    

b1.bind("<Button-1>",confirmpaymentfunction)



# frame 2
f1_frame2=LabelFrame(f1, height=600, width=700, padx=10, pady=10, text="Recieve Help ", font=("Caladea",20,"underline"))
f1_frame2.place(x=750, y=170)
 
f1_frame2.propagate(0)

img4=Canvas(f1_frame2, height=190, width=300, bg="white")
file4=PhotoImage(file="pic1.gif")
img4.create_image(100,100,image=file4)
img4.place(x=0, y=360)

img5=Canvas(f1_frame2, height=190, width=300, bg="white")
file5=PhotoImage(file="pic2.gif")
img5.create_image(150,100, image=file5)
img5.place(x=370, y=360)



l11=Label(f1_frame2, text="Reciever Name:  ", font=("Times New Roman",15))
l12=Label(f1_frame2, text="Type of help required: ", font=("Times New Roman",15))
l13=Label(f1_frame2, text="Address of reciever : ", font=("Times New Roman",15))


t11=Text(f1_frame2, height=1,width=50 )
t12=Text(f1_frame2, height=4, width=50)


val11=StringVar()
s11=Spinbox(f1_frame2, values=("Goods","Cash","NDRF Personall","Helicopter"), textvariable=val11, width=15, font=("Caladea",12) )



# button functions 

b11=Button(f1_frame2, text="Confirm Goods Recieved ", height=1, width=22, fg="green", bg="white",font=("Caladea",17))
b12=Button(f1_frame2, text="Report Injured", height=1, width=22, activebackground="blue",activeforeground="white", bg="white", fg="green",font=("Caladea",17))
b13=Button(f1_frame2, text="Helicopter Helpline", height=1, width=22, activebackground="blue",activeforeground="white", bg="white", fg="green",font=("Caladea",17))
b14=Button(f1_frame2, text="NDRF Personnal ", height=1, width=22, activebackground="blue",activeforeground="white", bg="white", fg="green",font=("Caladea",17))
b15=Button(f1_frame2, text="Interface Feedback ", height=1, width=22, activebackground="blue",activeforeground="white", bg="white", fg="green",font=("Caladea",17))


#binding and functions 
def reportinjured_func(xyz):
    root2=Tk()
    freport=Frame(root2, height=500, width=500, bg="silver")
    freport.propagate(0)
    
    
    namelabel=Label(freport, text="Enter the name of deceased: ",font=("Caladea",15), bg="silver")
    addlabel=Label(freport, text="Enter the address of the deceased: ",font=("Caladea",15), bg="silver")
    
    thought1=Label(freport, text="We rise by lifting others.... ", font=("Comic Sans MS",18,"italic"), bg="white", fg="blue")
    t1report=Text(freport, height=1,width=50 )
    t2report=Text(freport, height=4, width=50)
    
    b1report=Button(freport, text="Report", bg="red",fg="white", activebackground="orange", activeforeground="white",font=("Caladea",15,"bold"))
    b2report=Button(freport, text="Return", bg="blue",fg="white", activebackground="white", activeforeground="green",font=("Caladea",15,"bold"))
    
    
    namelabel.place(x=30, y=30)
    addlabel.place(x=30, y=100)
    t1report.place(x=30, y=53, height=30)
    t2report.place(x=30, y=123)
    b2report.place(x=30, y=220, width=170)
    b1report.place(x=265, y=220, width=170)
    thought1.place(x=100, y=400)
    
    def reported(xyz):
        
        nameofinjured_var=t1report.get(1.0,"end-1c")
        addressofinjured_var=t2report.get(1.0,"end-1c")
        
        df3=pd.read_excel("List3.xlsx")
        df3.loc[len(df3.index)]=[nameofinjured_var,addressofinjured_var]
        df3.to_excel("List3.xlsx",index=False)
        
        
        t1report.delete("1.0","end")
        t2report.delete("1.0", "end")
        
        reportedlabel=Label(freport, text="Help would reach the mentioned location \n as soon as possible.\n Fill details of other person if any or tap return ",font=("Caladea",15), bg="white")
        
        reportedlabel.place(x=30, y=280)
        
    def returntohomepage(xyz):
        root2.destroy()
    
    b1report.bind("<Button-1>",reported)
    b2report.bind("<Button-1>", returntohomepage)
    
    freport.pack()
    
    root2.mainloop()
b12.bind("<Button-1>",reportinjured_func)



def allthreeservices(xyz):
    
    
    
    
    reciever_name_var=t11.get(1.0,"end-1c")
    help_var=val11.get()
    address_receiver_var=t12.get(1.0,"end-1c")
    df2=pd.read_excel("List2.xlsx")
 
    df2.loc[len(df2.index)]=[reciever_name_var,help_var,address_receiver_var]
    df2.to_excel("List2.xlsx", index=False)
   
    t11.delete("1.0","end")
    t12.delete("1.0","end")
    
        
    root3=Tk()
    root3.title("Acknwoledgement")
    
    fallthree=Frame(root3, height=300, width=300)
    fallthree.propagate(0)
    
    confirmationlabel=Label(fallthree, text="The requested service would be \n provided as soon as possible. \n The interface \n as well the employees \n are dedicated \n to your well being \n HAVE A NICE DAY ",font=("Caladea",14,"bold"))
    confirmationlabel.place(x=10, y=30)
    
    
    def destroyfunc(xyz):
        root3.destroy()
        
    b2allthree=Button(fallthree, text="Return", bg="red",fg="white", activebackground="orange", activeforeground="white",font=("Caladea",15,"bold"))
    b2allthree.bind("<Button-1>", destroyfunc)
    b2allthree.place(x=100, y=200)
    
    
    fallthree.pack()
    root3.mainloop()
b11.bind("<Button-1>",allthreeservices)
b13.bind("<Button-1>",allthreeservices)
b14.bind("<Button-1>",allthreeservices)


def interfacefeedback(xyz):
    root4=Tk()
    root4.title("Feedback")
    feedbackframe=Frame(root4, height=600, width=600, bg="silver")
    feedbackframe.propagate(0)
    
    
    
    feedbackframe.pack()
    t1feedback=Text(feedbackframe)
    l1feedback=Label(feedbackframe, text="Fill your feedback in the box below , We would love to hear your \n feedback and motivate ourselves by learning from it  .", font=("Caladea",15,"bold"), bg="silver", fg="blue")
    
    
    b1feedback=Button(feedbackframe, text="Submit", bg="green",fg="white", activebackground="orange", activeforeground="white",font=("Caladea",15,"bold"))
    b2feedback=Button(feedbackframe, text="Return", bg="red",fg="white", activebackground="white", activeforeground="green",font=("Caladea",15,"bold"))
    
    l1feedback.place(x=0,y=50)
    t1feedback.place(x=100, y=100,height=400, width=400)
    b1feedback.place(x=416, y=500)
    b2feedback.place(x=100, y=500)
    
    def submitfeedback(xyz):
        t1feedback.delete("1.0","end")
        labelsubmited=Label(feedbackframe, text="Thankyou for your valuable feedback. \n Hope these hard times end soon . ",font=("Caladea",15,"bold"), bg="pink", fg="red")
        labelsubmited.place(x=120,y=550)
        
        
    def returnback(xyz):
        root4.destroy()
        
    b1feedback.bind("<Button-1>",submitfeedback)  
    b2feedback.bind("<Button-1>", returnback)
    root4.mainloop()
    
b15.bind("<Button-1>",interfacefeedback)



l11.place(x=50, y=10)
l12.place(x=50, y=45 )
l13.place(x=50, y=90)
t11.place(x=200, y=13 )
t12.place(x=230, y=90)
s11.place(x=250, y=45, height=30)


b11.place(x=50, y=190 ,height=50)
b12.place(x=370, y=190,height=50 )
b13.place(x=50, y=250 ,height=50)
b14.place(x=370, y=250 , height=50)
b15.place(x=200, y=310 ,height=50)

root.mainloop()

