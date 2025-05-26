import tkinter as tk
import pyshorteners

def shorten_url():
    long_url = entry_long_url.get()
    s = pyshorteners.Shortener()
    short_url = s.tinyurl.short(long_url)
    entry_short_url.delete(0,tk.END)
    entry_short_url.insert(tk.END , short_url)

# Create the main window
window = tk.Tk()
window.title("URL Shortener")

# Create labels and textboxes
label_long_url = tk.Label(window , text = "Long URL:")
label_long_url.pack(pady = 10)
entry_long_url = tk.Entry(window , width = 150)
entry_long_url.pack(pady = 10)

label_short_url = tk.Label(window , text = "Short URL:")
label_short_url.pack(pady = 10)
entry_short_url = tk.Entry(window , width = 150)
entry_short_url.pack(pady = 10)

# Create the command button
button_shorten = tk.Button(window, text = "Shorten URL" , command = shorten_url)
button_shorten.pack(pady = 10)

# Start the main loop
window.mainloop()
