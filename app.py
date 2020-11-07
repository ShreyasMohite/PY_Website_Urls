from tkinter import *
from urllib.request import urlopen
from bs4 import BeautifulSoup
import tkinter.messagebox
import threading



class Website_url:
    def __init__(self,root):
        self.root=root
        self.root.title("Website Url")
        self.root.iconbitmap("logo591.ico")
        self.root.geometry("500x400")
        self.root.resizable(0,0)

        url=StringVar()



        def on_enter1(e):
            but_scrape['background']="black"
            but_scrape['foreground']="cyan"
            
            

        def on_leave1(e):
            but_scrape['background']="SystemButtonFace"
            but_scrape['foreground']="SystemButtonText"


        def on_enter2(e):
            but_clear['background']="black"
            but_clear['foreground']="cyan"
            
            

        def on_leave2(e):
            but_clear['background']="SystemButtonFace"
            but_clear['foreground']="SystemButtonText"



        def web():
            try:
                if url.get()!="":
                    with open("C:/TEMP/weburl.txt","w",encoding='utf-8') as f:

                        web=url.get()
                        urlname=urlopen(web)
                        soup=BeautifulSoup(urlname.read(),"lxml")
                        segment=soup.findAll("a")
                        get_urls=set()
                        for anchors in segment:                           
                            try:
                                if anchors.get("href")!="#" or anchors.get("href")!=str("") :
                                    fullurl=web+anchors.get("href")
                                    get_urls.add(fullurl)
                            except Exception as e:
                                print(e)
                        for a in get_urls:
                            f.write(a+"\n\n")                   
                    with open("C:/TEMP/weburl.txt","r",encoding='utf-8') as f:
                        text.insert('end',f.read())

                    
                else:
                    tkinter.messagebox.showerror("Error","Please Enter Url")
            except Exception as e:
                tkinter.messagebox.showerror("Error","Network Error")

        
        def thread_website():
            t=threading.Thread(target=web)
            t.start()
                





        def clear():
            url.set("")
            text.delete('1.0','end')



#==================frame=========================#
        mainframe=Frame(self.root,width=500,height=400,relief="ridge",bd=3)
        mainframe.place(x=0,y=0)


        firstframe=Frame(mainframe,width=494,height=130,relief="ridge",bd=3,bg="#e842ff")
        firstframe.place(x=0,y=0)

        secondframe=Frame(mainframe,width=494,height=264,relief="ridge",bd=3)
        secondframe.place(x=0,y=130)

#=========================firstframe========================================#
        

        lab_website_url=Label(firstframe,text="Please Enter Website Url",font=('times new roman',12),bg="#e842ff",fg="white")
        lab_website_url.place(x=150,y=10)

        ent_website_url=Entry(firstframe,width=38,font=('times new roman',12),relief="ridge",bd=4,textvariable=url)
        ent_website_url.place(x=80,y=40)

        but_scrape=Button(firstframe,text="Scrape",width=18,font=('times new roman',12),cursor="hand2",command=thread_website)
        but_scrape.place(x=40,y=80)
        but_scrape.bind("<Enter>",on_enter1)
        but_scrape.bind("<Leave>",on_leave1)




        but_clear=Button(firstframe,text="Clear",width=18,font=('times new roman',12),cursor="hand2",command=clear)
        but_clear.place(x=270,y=80)
        but_clear.bind("<Enter>",on_enter2)
        but_clear.bind("<Leave>",on_leave2)





#=========================secondframe======================================#

        scol=Scrollbar(secondframe,orient="vertical")
        scol.place(relx=1, rely=0, relheight=1, anchor='ne')
        
        text=Text(secondframe,height=13,width=58,font=('times new roman',12),yscrollcommand=scol.set,relief="sunken",bd=3,fg="black")      
        text.place(x=0,y=0)
        scol.config(command=text.yview)
        


        



        










if __name__ == "__main__":
    root=Tk()
    app=Website_url(root)
    root.mainloop()
