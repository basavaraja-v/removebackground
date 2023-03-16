import customtkinter
import os
from PIL import ImageTk, Image
from tkinter import filedialog
from rembg import remove

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Remove Background")
        self.geometry("760x400")

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
    
        self.home_frame_button_2 = customtkinter.CTkButton(self.home_frame, text="Select Image", compound="right", command = self.open_img)
        self.home_frame_button_2.grid(row=2, column=0, padx=20, pady=10)

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
        filename = filedialog.askopenfilename(title ='"pen')
        return filename

    def save_file(self):
        filepath = filedialog.asksaveasfile(mode='w',defaultextension=".png")
        if not filepath:
            return
        return filepath

    def open_img(self):
        # Select the Imagename  from a folder
        input_filename = self.openfilename()
        # opens the image
        img = Image.open(input_filename)
        
        output = remove(img)
        filepath = self.save_file()
        output.save(filepath.name)

        # # # resize the image and apply a high-quality down sampling filter
        # # # img = img.resize((250, 250), Image.ANTIALIAS)

        # # PhotoImage class is used to add image to widgets, icons etc
        # img = ImageTk.PhotoImage(img)
    
        # # create a label
        # input_img = customtkinter.CTkLabel(self, image = img)
        
        # # set the image as img
        # input_img.image = img
        # input_img.grid(row=3, column=1, padx=20, pady=10)

        # output = ImageTk.PhotoImage(output)
        # # create a label
        # output_img = customtkinter.CTkLabel(self, image = output)
        
        # # set the image as img
        # output_img.image = output
        # output_img.grid(row=3, column=2, padx=20, pady=10)

if __name__ == "__main__":
    app = App()
    app.mainloop()

