
import tkinter as tk
from tkinter import ttk
import socket
import threading

class ChannelListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Channel List App")
        
        # Create main frame
        self.frame = ttk.Frame(self.root, padding="10")
        self.frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Channel list
        self.channel_list = ttk.Treeview(self.frame, columns=("Channel", "Instrument", "Notes"))
        self.channel_list.heading("Channel", text="Channel")
        self.channel_list.heading("Instrument", text="Instrument")
        self.channel_list.heading("Notes", text="Notes")
        self.channel_list.grid(row=0, column=0, columnspan=3)
        
        # Entry fields
        ttk.Label(self.frame, text="Channel:").grid(row=1, column=0)
        self.channel_entry = ttk.Entry(self.frame)
        self.channel_entry.grid(row=1, column=1)
        
        ttk.Label(self.frame, text="Instrument:").grid(row=2, column=0)
        self.instrument_entry = ttk.Entry(self.frame)
        self.instrument_entry.grid(row=2, column=1)
        
        ttk.Label(self.frame, text="Notes:").grid(row=3, column=0)
        self.notes_entry = ttk.Entry(self.frame)
        self.notes_entry.grid(row=3, column=1)
        
        # Add button
        self.add_button = ttk.Button(self.frame, text="Add Channel", command=self.add_channel)
        self.add_button.grid(row=4, column=0, columnspan=2)

    def add_channel(self):
        channel = self.channel_entry.get()
        instrument = self.instrument_entry.get()
        notes = self.notes_entry.get()
        
        self.channel_list.insert("", "end", values=(channel, instrument, notes))
        
        # Clear entries
        self.channel_entry.delete(0, tk.END)
        self.instrument_entry.delete(0, tk.END)
        self.notes_entry.delete(0, tk.END)

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 5000))
    server.listen(5)
    
    while True:
        client, addr = server.accept()
        print(f"Connection from {addr}")
        client.close()

if __name__ == "__main__":
    # Start server in separate thread
    server_thread = threading.Thread(target=start_server, daemon=True)
    server_thread.start()
    
    # Start Tkinter app
    root = tk.Tk()
    app = ChannelListApp(root)
    root.mainloop()
