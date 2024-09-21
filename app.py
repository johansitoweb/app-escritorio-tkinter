import tkinter as tk  
from tkinter import messagebox, simpledialog  

class TodoApp:  
    def __init__(self, root):  
        self.root = root  
        self.root.title("Lista de Tareas")  
        self.root.geometry("400x300")  
        
        # Menú  
        menu_bar = tk.Menu(root)  
        file_menu = tk.Menu(menu_bar, tearoff=0)  
        file_menu.add_command(label="Salir", command=root.quit)  
        menu_bar.add_cascade(label="Archivo", menu=file_menu)  
        root.config(menu=menu_bar)  

        # Lista de tareas  
        self.task_listbox = tk.Listbox(root, selectmode=tk.SINGLE)  
        self.task_listbox.pack(pady=20, fill=tk.BOTH, expand=True)  

        # Botones  
        button_frame = tk.Frame(root)  
        button_frame.pack(pady=10)  

        add_button = tk.Button(button_frame, text="Agregar Tarea", command=self.add_task)  
        add_button.pack(side=tk.LEFT, padx=5)  

        delete_button = tk.Button(button_frame, text="Eliminar Tarea", command=self.delete_task)  
        delete_button.pack(side=tk.LEFT, padx=5)  

        edit_button = tk.Button(button_frame, text="Modificar Tarea", command=self.edit_task)  
        edit_button.pack(side=tk.LEFT, padx=5)  

    def add_task(self):  
        task = simpledialog.askstring("Nueva Tarea", "Ingresa la tarea:")  
        if task:  
            self.task_listbox.insert(tk.END, task)  

    def delete_task(self):  
        try:  
            selected_task_index = self.task_listbox.curselection()[0]  
            self.task_listbox.delete(selected_task_index)  
        except IndexError:  
            messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminar.")  

    def edit_task(self):  
        try:  
            selected_task_index = self.task_listbox.curselection()[0]  
            current_task = self.task_listbox.get(selected_task_index)  
            new_task = simpledialog.askstring("Modificar Tarea", "Edita la tarea:", initialvalue=current_task)  
            if new_task:  
                self.task_listbox.delete(selected_task_index)  
                self.task_listbox.insert(selected_task_index, new_task)  
        except IndexError:  
            messagebox.showwarning("Advertencia", "Selecciona una tarea para modificar.")  

# Inicializar la aplicación  
if __name__ == "__main__":  
    root = tk.Tk()  
    app = TodoApp(root)  
    root.mainloop()