import tkinter as tk

def animate_confession():
    global index
    confession = """
    Dear Best Friends,

    As Valentine's Day dawns,
    I want to share my love and appreciation
    for each and every one of you.

    You're the stars that light up my darkest nights,
    the laughter that fills my days with joy,
    and the shoulders I lean on when times get tough.

    Our friendship is a treasure beyond measure,
    a bond that grows stronger with each passing day.

    So here's to us, my dear friends,
    united by love, laughter, and endless memories.

    Happy Valentine's Day!

    With all my love,
    
    Your Awesome Buddy: FranssVin
    """

    if index < len(confession):
        confession_label.config(text=confession[:index])
        index += 1
        window.after(50, animate_confession)

# Create the main window
window = tk.Tk()
window.title("Animated Valentine's Day Confession for Best Friends")

# Create a label to display the animated confession text
confession_label = tk.Label(window, text="", bg="white", fg="red", font=("Arial", 12), justify="left", wraplength=300)
confession_label.pack(padx=20, pady=20)

# Start the animation when the window is opened
index = 0
animate_confession()

# Run the Tkinter event loop
window.mainloop()
