import customtkinter
import os
from PIL import Image
from tkinter import filedialog
from rembg import remove

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Remove Background")
        self.geometry("800x400")

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # load images with light and dark mode image
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "assets")
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "icon.png")), size=(26, 26))
        self.iconbitmap(os.path.join(image_path,"icon.ico"))
        self.large_test_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "rmbg.jpeg")), size=(500, 150))
        self.image_icon_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "image_icon_light.png")), size=(20, 20))
        self.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "home_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "home_light.png")), size=(20, 20))
        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="  Remove Background", image=self.logo_image,
                                                             compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Home",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=self.home_image, anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame, values=["Light", "Dark", "System"],
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")

        # create home frame
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)

        self.home_frame_large_image_label = customtkinter.CTkLabel(self.home_frame, text="", image=self.large_test_image)
        self.home_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10)
        # Create a button and place it into the window using grid layout
    
        self.home_frame_button_1 = customtkinter.CTkButton(self.home_frame, text="Select Image", compound="right", command = self.open_img)
        self.home_frame_button_1.grid(row=2, column=0, padx=20, pady=10)

        self.home_frame_button_2 = customtkinter.CTkButton(self.home_frame, text="Select Images", compound="right", command = self.open_imgs)
        self.home_frame_button_2.grid(row=3, column=0, padx=20, pady=10)

        self.perCompletion = customtkinter.CTkLabel(self.home_frame, text ='0%')
        self.perCompletion.grid(row=4, column=0, padx=20, pady=10)

        self.progressBar = customtkinter.CTkProgressBar(self.home_frame)
        self.progressBar.set(0)
        self.progressBar.grid(row=5, column=0, padx=20, pady=10)

        self.finishLabel = customtkinter.CTkLabel(self.home_frame, text ='')
        self.finishLabel.grid(row=5, column=0, padx=20, pady=10)
        # create second frame
        self.second_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # create third frame
        self.third_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # select default frame
        self.select_frame_by_name("home")


    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")

        # show selected frame
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "frame_2":
            self.second_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.second_frame.grid_forget()
        if name == "frame_3":
            self.third_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.third_frame.grid_forget()

    def home_button_event(self):
        self.select_frame_by_name("home")

    def frame_2_button_event(self):
        self.select_frame_by_name("frame_2")

    def frame_3_button_event(self):
        self.select_frame_by_name("frame_3")

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def openfilename(self):
 
        # open file dialog box to select image
        # The dialogue box has a title "Open"
        filename = filedialog.askopenfilename(
    title="Choose a image",
    filetypes=[('all files', '.*'),
               ('image files', ('.png', '.jpg','jpeg')),
           ])
        return filename
    
    def openfilenames(self):
 
        # open file dialog box to select image
        # The dialogue box has a title "Open"
        files = filedialog.askopenfilenames(
    title="Choose a images",
    filetypes=[('all files', '.*'),
               ('image files', ('.png', '.jpg','jpeg')),
           ]
           )
        if len(files) > 100:
            self.finishLabel.configure(text="Please select up to 100 files", text_color="red",font=("Comic Sans MS", 20, "bold"))
            return []
        return files

    def save_file(self):
        filepath = filedialog.asksaveasfile(mode='w',defaultextension=".png")
        if not filepath:
            return
        return filepath

    def initialize(self):
        self.progressBar.set(0)
        self.progressBar.update()
        self.perCompletion.configure(text='0%')
        self.perCompletion.update()
        self.finishLabel.configure(text="")
        self.finishLabel.update()
    def open_img(self):
        self.initialize()
        total_iterations = 1
        # Select the Imagename  from a folder
        input_filepath = self.openfilename()
        # opens the image
        img = Image.open(input_filepath)
        
        output = remove(img)
        # filepath = self.save_file()
        input_path = "/".join(input_filepath.split('/')[:-1])
        input_filename = input_filepath.split('/')[-1]
        output = output.convert('RGB')
        output.save(input_path+'/bg_'+input_filename)
        percentage_complete = 1 / total_iterations * 100
        self.perCompletion.configure(text=str(int(percentage_complete))+'%')
        self.perCompletion.update()
        self.progressBar.set(float(percentage_complete)/100)
        self.finishLabel.configure(text="Done!", text_color="green",font=("Comic Sans MS", 20, "bold"))
    
    def open_imgs(self):
        # Select the Imagename  from a folder
        self.initialize()
        input_files = self.openfilenames()
        total_iterations = len(input_files)
        i = 0
        for input_filepath in input_files:
            img = Image.open(input_filepath)
        
            output = remove(img)
            # filepath = self.save_file()
            input_path = "/".join(input_filepath.split('/')[:-1])
            input_filename = input_filepath.split('/')[-1]
            output = output.convert('RGB')
            output.save(input_path+'/bg_'+input_filename)
            i=i+1
            percentage_complete = i / total_iterations * 100
            self.perCompletion.configure(text=str(int(percentage_complete))+'%')
            self.perCompletion.update()
            self.progressBar.set(float(percentage_complete)/100)
        if input_files:
            self.finishLabel.configure(text="All Done!", text_color="green",font=("Comic Sans MS", 20, "bold"))
        # opens the image
        # img = Image.open(input_filename)
        
        # output = remove(img)
        # filepath = self.save_file()
        # output.save(filepath.name)


if __name__ == "__main__":
    app = App()
    app.mainloop()

