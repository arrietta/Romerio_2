import subprocess
from PIL import Image
import tkinter as tk
from tkinter import filedialog
import os


def select_images():
    """Открывает диалог выбора файлов и возвращает список путей к изображениям."""
    root = tk.Tk()
    root.withdraw()  # Скрыть главное окно
    file_paths = filedialog.askopenfilenames(
        title="Выберите изображения",
        filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.bmp;*.gif")]
    )
    return list(file_paths)


def select_output_directory():
    """Открывает диалог выбора папки и возвращает путь к выбранной папке."""
    root = tk.Tk()
    root.withdraw()  # Скрыть главное окно
    folder_path = filedialog.askdirectory(title="Выберите папку для сохранения изображений")
    return folder_path


def main():
    # Выбор изображений
    input_images = select_images()
    if not input_images:
        print("Изображения не выбраны.")
        return

    # Выбор папки для сохранения изображений
    output_directory = select_output_directory()
    if not output_directory:
        print("Папка не выбрана.")
        return

    # Список желаемых размеров
    sizes = [
        (640, 640),
    ]

    for input_image in input_images:
        # Получаем имя и расширение файла
        file_name, file_extension = os.path.splitext(os.path.basename(input_image))
        # output_original = os.path.join(output_directory, f"{file_name}_original{file_extension}")
        #
        # # Создаем оригинальную копию с 8-битной глубиной
        # subprocess.run(["magick", "convert", input_image, "-depth", "8", output_original])

        # Изменяем размеры
        for width, height in sizes:
            output_filename = os.path.join(output_directory, f"{file_name}{file_extension}")

            # Используем Pillow для обработки миниатюр
            if width < 720:  # для миниатюр используем метод thumbnail
                with Image.open(input_image) as img:
                    img.thumbnail((width, height))
                    img.save(output_filename)
            else:  # для остальных размеров используем ImageMagick с 8-битной глубиной
                subprocess.run(["magick", "convert", input_image, "-resize", f"{width}x{height}", "-depth", "8", output_filename])

    print("Изображения созданы.")


if __name__ == "__main__":
    main()
