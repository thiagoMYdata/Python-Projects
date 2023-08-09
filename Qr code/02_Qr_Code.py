import customtkinter as ctk
from PIL import ImageTk
import qrcode
from tkinter import filedialog


class App(ctk.CTk):
    def __init__(self,):
        super().__init__(ctk.set_appearance_mode('light'))
        # root
        self.geometry('500x600')
        self.title('Qr Code')

        # widgets
        ## top
        self.qrframe = ctk.CTkFrame(self)
        self.qrframe.pack(expand=True, fill='both')

        self.qrcanvas = ctk.CTkCanvas(self.qrframe, background='#fff')
        self.qrcanvas.pack(expand=True, fill='both')

        ## bottom
        self.bottom_frame = ctk.CTkFrame(self,bg_color='#fff', fg_color='#10168f',corner_radius=30)
        self.bottom_frame.place(relx=0, rely=1.1,relwidth =1 , anchor='sw', relheight=0.25)

        self.blocotxt = ctk.CTkEntry(self.bottom_frame, fg_color='#3d56a6',  corner_radius=10)
        self.blocotxt.place(relx=0.1, rely=0.2, relwidth=0.55)
        self.blocotxt.bind('<Key>', lambda event:  self.blocotxt.after(10,self.on_entry_change))

        self.botao = ctk.CTkButton(self.bottom_frame, text='save',fg_color='#3d56a6', command=lambda :  self.botao.after(10,self.salvar_png))
        self.botao.place(relx=0.75, rely=0.2, relwidth=0.15)

        # run
        self.mainloop()

    def qrcode_generator(self):
        self.text = self.blocotxt.get() # tira o texto de Entry widget
        self.img = qrcode.make(self.text) # transforma text em qrcode object (img) 
        return self.img

    def on_entry_change(self):
        self.img = self.qrcode_generator()  # recebe o qrcode em na forma de qrcode object 
        self.img_PIL = self.img.resize((300,300)) # trava as dimensões da img
        self.qr_code_image = ImageTk.PhotoImage(self.img_PIL) # converte pra ImageTK, é a que funciona com Tkinter aparentemente...

        self.qrcanvas.destroy()
        self.qrcanvas = ctk.CTkCanvas(self.qrframe,background='#fff') # cria o qrcanvas de novo
        self.qrcanvas.pack(expand=True, fill='both')

        if self.text != '':     # essa condição so deixa mostrar qrcode, que foram digitados no entry box nada de string vazia!
            self.qrcanvas.create_image(250 ,250 , anchor='center', image=self.qr_code_image)

    def salvar_png(self):
        self.qr_code_image = self.qrcode_generator()  # recebe o qrcode em na forma de qrcode object 
        self.file_path = filedialog.asksaveasfilename( # filedialog é a função que abre o 'salvar como' do windows ## certeza que devem existir outros jeitos fora do tkinter
            initialdir='c:/Users/Thiago/Pictures', 
            title='You \'re actually blind LULE ', 
            initialfile='qrcode_img', # nome do file default
            defaultextension=".png", 
            filetypes=[("PNG files", "*.png"),('all files','*.*')])
        self.qr_code_image.save(self.file_path) # recebe o file_path que a metodo save salva a img qr_code_image em.

App()