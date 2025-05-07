import socket
import threading
import tkinter as tk
from tkinter import messagebox

class TrisClient:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tris - Client (O)")

        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.buttons = [[None]*3 for _ in range(3)]
        self.current_turn = "X"
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        server_ip = input("Inserisci l'IP del server: ")
        self.sock.connect((server_ip, 5000))
        threading.Thread(target=self.receive_move, daemon=True).start()

        self.build_gui()
        self.root.mainloop()

    def build_gui(self):
        for i in range(3):
            for j in range(3):
                btn = tk.Button(self.root, text="", font=("Helvetica", 32), width=5, height=2,
                                command=lambda row=i, col=j: self.make_move(row, col))
                btn.grid(row=i, column=j)
                self.buttons[i][j] = btn

    def make_move(self, row, col):
        if self.board[row][col] == "" and self.current_turn == "O":
            self.board[row][col] = "O"
            self.buttons[row][col].config(text="O", state="disabled")
            self.sock.send(f"{row},{col}".encode())
            if self.check_winner("O"):
                messagebox.showinfo("Vittoria", "Hai vinto!")
                self.root.quit()
            elif self.is_draw():
                messagebox.showinfo("Pareggio", "Pareggio!")
                self.root.quit()
            else:
                self.current_turn = "X"

    def receive_move(self):
        while True:
            data = self.sock.recv(1024).decode()
            row, col = map(int, data.split(","))
            self.board[row][col] = "X"
            self.buttons[row][col].config(text="X", state="disabled")
            if self.check_winner("X"):
                messagebox.showinfo("Sconfitta", "Hai perso!")
                self.root.quit()
            elif self.is_draw():
                messagebox.showinfo("Pareggio", "Pareggio!")
                self.root.quit()
            else:
                self.current_turn = "O"

    def check_winner(self, symbol):
        b = self.board
        return any([
            all(b[i][j] == symbol for j in range(3)) for i in range(3)
        ]) or any([
            all(b[i][j] == symbol for i in range(3)) for j in range(3)
        ]) or all([
            b[i][i] == symbol for i in range(3)
        ]) or all([
            b[i][2 - i] == symbol for i in range(3)
        ])

    def is_draw(self):
        return all(cell in ["X", "O"] for row in self.board for cell in row)

if __name__ == "__main__":
    TrisClient()
