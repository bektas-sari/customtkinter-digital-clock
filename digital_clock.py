import customtkinter as ctk
import time
from datetime import datetime

# CustomTkinter Settings
ctk.set_appearance_mode("dark")  # Default mode: dark
ctk.set_default_color_theme("blue")  # Default theme

# Create the main window
app = ctk.CTk()
app.title("Digital Clock")
app.geometry("500x350")

# **Stylish Background**
app.configure(bg="#121212")  # Dark gray background

# **Clock Label (Always Visible)**
clock_label = ctk.CTkLabel(
    app,
    text="",
    font=("Montserrat", 65, "bold"),
    fg_color="#222831",  # Dark gray clock box
    text_color="#00ADB5",  # Turquoise clock text (Always visible)
    width=400,
    height=120,
    corner_radius=15
)
clock_label.pack(pady=20)

# **Date Label**
date_label = ctk.CTkLabel(
    app,
    text="",
    font=("Montserrat", 22),
    fg_color="#393E46",  # Gray background
    text_color="#EEEEEE",  # White text color
    width=350,
    height=50,
    corner_radius=10
)
date_label.pack(pady=5)

# **Update Time Function**
def update_time():
    now = datetime.now()
    time_string = now.strftime("%H:%M:%S")  # 24-hour format
    date_string = now.strftime("%d %B %Y, %A")  # Example: 16 February 2025, Sunday
    clock_label.configure(text=time_string)
    date_label.configure(text=date_string)
    app.after(1000, update_time)  # Update every second

# **Automatic Day/Night Mode Switching**
def auto_theme():
    now = datetime.now()
    hour = now.hour

    if 8 <= hour < 20:  # Day mode (08:00 - 20:00)
        bg_color = "#F0F0F0"  # Light gray background
        clock_color = "#EEEEEE" 
        date_color = "#EEEEEE" 
        text_color = "#222831"  # Black text
        mode = "light"
    else:  # Night mode (20:00 - 08:00)
        bg_color = "#121212"  # Dark gray
        clock_color = "#222831"  # Dark background for clock
        date_color = "#393E46"
        text_color = "#EEEEEE"  # White text
        mode = "dark"

    app.configure(bg=bg_color)
    clock_label.configure(fg_color=clock_color, text_color=text_color)  # Clock remains always visible
    date_label.configure(fg_color=date_color, text_color=text_color)
    ctk.set_appearance_mode(mode)  # Update Tkinter theme

    app.after(60000, auto_theme)  # Check every minute

# **Hover (Glow) Effect (Clock Will Not Disappear!)**
def on_hover(event):
    clock_label.configure(text_color="#FFD700")  # Change to gold on hover

def off_hover(event):
    clock_label.configure(text_color="#00ADB5")  # Revert to turquoise

clock_label.bind("<Enter>", on_hover)
clock_label.bind("<Leave>", off_hover)

# **Initialize Functions**
auto_theme()  # Start automatic day/night mode
update_time()  # Start clock update

app.mainloop()
