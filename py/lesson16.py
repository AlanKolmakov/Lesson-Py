# Модуль os.
import os

# print(os.getcwd())  # путь к текущей директории
# print(os.listdir(".."))
# os.mkdir(r"folder")  # создать папку
# os.makedirs("nested1/nested2/nested3")  # создать дерево папок
# os.remove("test.py")  # удаляет файл
# os.rename("nested1", "test")  # переименовать папку/файл
# os.rename("test.txt", "test/test.txt")  # переместить файл
# os.renames("test.txt", "text/three.py")  # работает с путями, которые не существуют
# os.rmdir("text")  # удаляет пустую папку
# os.walk("путь к директории", topdown=True/False)
# for root, dirs, files in os.walk("../py", topdown=False):
#     print("Root:", root)
#     print("\tSubdirs:", dirs)
#     print("\tFiles:", files)

# Вариант 1
# for path, names, files in os.walk(os.getcwd(), topdown=False):
#     if not names and not files:
#         os.rmdir(path)
#         print(f"Директория {path} удалена")

# Вариант 2
# for path, names, files in os.walk(os.getcwd(), topdown=False):
#     if not os.listdir(path):
#         os.rmdir(path)
#         print(f"Директория {path} удалена")

import os.path

# print(os.path.split(r"C:\Users\Genio_Loci\Desktop\Lessons-Python\Lesson-Py\py\test\test.txt")[1])
# print(os.path.dirname(r"C:\Users\Genio_Loci\Desktop\Lessons-Python\Lesson-Py\py\test\test.txt"))
# print(os.path.basename(r"C:\Users\Genio_Loci\Desktop\Lessons-Python\Lesson-Py\py\test\test.txt"))
#
# print(os.path.join(r"C:\Users\Genio_Loci\Desktop\Lessons-Python\Lesson-Py\py\test", "files", "dir",
#                    "test.txt"))

# dirs = ["work/F1", "Work/F2/F21"]
#
# for dir1 in dirs:
#     os.makedirs(dir1)
# #
# files = {
#     'Work': ['w.txt'],
#     'Work/F1': ['f11.txt', 'f12.txt', 'f13.txt'],
#     'Work/F2/F21': ['f211.txt', 'f212.txt'],
# }
#
# for dir1, files in files.items():
#     for file in files:
#         file_path = os.path.join(dir1, file)
#         open(file_path, 'w').close()
#
# file_with_text = ['Work/w.txt', 'Work/F1/f12.txt', 'Work/F2/F21/f211.txt', 'Work/F2/F21/f212.txt']
# for file in file_with_text:
#     with open(file, "w") as f:
#         f.write(f"some sample text for {file} file")
#
#
# def print_tree(root, topdown):
#     print(f"обход {root} {'сверху вниз' if topdown else 'снизу вверх'}")
#     for root, dirs, files in os.walk(root, topdown=topdown):
#         print(root)
#         print(dirs)
#         print(files)
#     print("-" * 40)
#
#
# print_tree("Work", topdown=False)
# print_tree("Work", topdown=True)
