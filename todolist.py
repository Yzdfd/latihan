import json
import os

FILE_NAME = "tasks.json"

# Load dan save data

def load_data():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file :
            return json.load(file)
        
    return[]

def save_data(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

def show_menu():
    print("=====Main Menu=====")
    print("1. Tambah Tugas")
    print("2. Lihat Tugas")
    print("3. Tandai Selesai")
    print("4. Hapus Tugas")
    print("5. Keluar")
    
def add_tasks(tasks):
    task = input("Masukan Tugas : ")
    tasks.append({"task": task, "done": False})
    save_data(tasks)
    print("Tugas berhasil ditambahkan")
    
def show_tasks(tasks):
    if not tasks:
        print("Belum ada tugas")
        return
    
    for i, task in enumerate(tasks, start=1) :
        status = "Done" if task["done"] else "not done yet"
        print(f"{i}. [{status}] {task['task']}")
      
def mark_done(tasks):
      show_tasks(tasks)
      try:
        index = int(input("Nomor Tugas yang Selesai : ")) -1
        tasks[index]["done"] = True
        save_data(tasks)
        print("Tugas ditandai selesai!")
      except(ValueError,IndexError):
          print("Input tidak valid !")
          
def delete_task(tasks):
    show_tasks(tasks)
    try:
        index = int(input("Nomor tugas yang ingin dihapus :")) - 1
        tasks.pop(index)
        save_data(tasks)
        print("Tugas berhasil dihapus")
    except(IndexError, ValueError):
        print("Input tidak valid !")

def main():
    task = load_data()
    
    while True:
        show_menu()          
        pilih = input("Pilih Menu (1-5) : ")
        
        if pilih == "1":
            add_tasks(task)
        elif pilih == "2":
            show_tasks(task)
        elif pilih == "3" :
            mark_done(task)
        elif pilih == "4" :
            delete_task(task)
        elif pilih == "5":
            print("Program selesai !")
            break
        else :
            print("Pilihan tidak valid !")
            
main()