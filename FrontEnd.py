from tkinter import *
from PIL import Image,ImageTk
import pandas as pd
import joblib
root = Tk()

def resize_image(width,height,image_path):
    image = Image.open(image_path)
    image = image.resize((width,height))
    return  image
root.title("Logistic Regression")
root.geometry("700x500")
image_path = "D:/internship/Project/images.png"
resize_image = resize_image(700,500,image_path)

model= joblib.load("Churn.joblib")

def FetchExited():

    lst = ["CreditScore","Geography","Gender","Age","Tenure","Balance","NumOfProducts","HasCrCard","IsActiveMember","EstimatedSalary"]
    ents = [en1,en2,en3,en4,en5,en6,en7,en8,en9,en10]
    abc = [e.get() for e in ents]

    abc_converted = [
        int(abc[0]),
        abc[1],
        abc[2],
        int(abc[3]),
        int(abc[4]),
        float(abc[5]),
        int(abc[6]),
        int(abc[7]),
        int(abc[8]),
        float(abc[9])
    ]
    dict_data = {col: [val] for col, val in zip(lst, abc_converted)}
    dict_df = pd.DataFrame(dict_data)

    # Make prediction
    Exit = model.predict(dict_df)
    Exited.config(text=f"Churn Prediction: {Exit[0]}")


photo = ImageTk.PhotoImage(resize_image)
background_label = Label(root, image=photo)
background_label.image = photo
background_label.place(relwidth=1, relheight=1)

root.resizable(width=False, height= False)
# root.minsize(200,200)
# root.maxsize(600,600)
header = Label(root,text="BANK CUSTOMER CHURN PREDICTION",
               font=("Cambria",20,"bold"),
               background="Black",foreground="White")
header.place(x = 90,y=10)
CreditScore = Label(root,text="CreditScore",
                  font=("Cambria",10),
                    background="Black",foreground="White")
CreditScore.place(x=10,y=60)
Geography = Label(root,text="Geography",
                  font=("Cambria",10),
                  background="Black",foreground="White")
Geography.place(x=10,y=100)
Gender = Label(root,text="Gender",
                  font=("Cambria",10),
               background="Black",foreground="White")
Gender.place(x=10,y=140)
Age = Label(root,text="Age",
                  font=("Cambria",10),
            background="Black",foreground="White")
Age.place(x=10,y=180)
Tenure = Label(root,text="Tenure",
                  font=("Cambria",10),
               background="Black",foreground="White")
Tenure.place(x=10,y=220)
Balance = Label(root,text="Balance",
                  font=("Cambria",10),
                background="Black",foreground="White")
Balance.place(x=10,y=260)
NumOfProducts = Label(root,text="Products",
                  font=("Cambria",10),
                background="Black",foreground="White")
NumOfProducts.place(x=10,y=300)
HasCrCard = Label(root,text="HasCrCard",
                  font=("Cambria",10),
                  background="Black",foreground="White")
HasCrCard.place(x=250,y=60)
IsActiveMember = Label(root,text="Member",
                  font=("Cambria",10),
                background="Black",foreground="White")
IsActiveMember.place(x=250,y=100)
EstimatedSalary = Label(root,text="Salary",
                  font=("Cambria",10),
                    background="Black",foreground="White")
EstimatedSalary.place(x=250,y=140)
Exited = Label(root,text=" ",
               font=("Cambria",10),
               background="Black",foreground="White")
Exited.place(x=100,y=340)
PlaceHolder = "id"
en1 = Entry(root,width=10,
            font=("Cambria", 10))
en1.insert(0,PlaceHolder)
en1.config(fg="grey")

en1.place(x=90,y=60)
en2 = Entry(root,width=10,
            font=("Cambria", 10))
P1 = "0 to 2"
en2.insert(0,P1)
en2.config(fg="grey")
en2.place(x=90,y=100)
en3 = Entry(root,width=10,
            font=("Cambria", 10))
P2 = "0 or 1"
en3.insert(0,P2)
en3.config(fg="grey")
en3.place(x=90,y=140)
en4 = Entry(root,width=10,
            font=("Cambria", 10))
P3 = "Age"
en4.insert(0,P3)
en4.config(fg="grey")
en4.place(x=90,y=180)
en5 = Entry(root,width=10,
            font=("Cambria", 10))
P4 = "0 to 10"
en5.insert(0,P4)
en5.config(fg="grey")
en5.place(x=90,y=220)
en6 = Entry(root,width=10,
            font=("Cambria", 10))
P5 = "Balance"
en6.insert(0,P5)
en6.config(fg="grey")
en6.place(x=90,y=260)
en7 = Entry(root,width=10,
            font=("Cambria", 10))
P6 = "1.0 to 4.0"
en7.insert(0,P6)
en7.config(fg="grey")
en7.place(x=90,y=300)
en8 = Entry(root,width=10,
            font=("Cambria", 10))
P7 = "0.1 or 0.0"
en8.insert(0,P7)
en8.config(fg="grey")
en8.place(x=310,y=60)
en9 = Entry(root,width=10,
            font=("Cambria", 10))
P8 = "1.0 or 0.0"
en9.insert(0,P8)
en9.config(fg="grey")
en9.place(x=310,y=100)
en10 = Entry(root,width=10,
             font=("Cambria", 10))
P9 ="Salary"
en10.insert(0,P9)
en10.config(fg="grey")
en10.place(x=310,y=140)

btn = Button(root,text="Submit",
             font=("Cambria",10),
             command=FetchExited,
             background="Black",
             foreground="white")
btn.place(x=310,y=280)
root.mainloop()