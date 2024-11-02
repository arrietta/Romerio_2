import os
from wand.image import Image


def combine_images_layers(image_paths, output_path):
    try:
        with Image(filename=image_paths[0]) as result_image:
            for image_path in image_paths[1:]:
                with Image(filename=image_path) as img:
                    result_image.composite(img, operator='over')
            result_image.save(filename=output_path)
    except Exception as e:
        print(f"Ошибка при обработке файла: {image_paths}, ошибка: {e}")


image_groups = [

    ['static/Catalog/Background.png', "media/Shape/Plain_1.1_White.png", 'media/Portals/PORTAL_White.png',
     'static/Catalog/SIZE1.png'],

]

output_names = [

]

output_folder = 'output'  # Папка для сохранения результата
os.makedirs(output_folder, exist_ok=True)

if len(image_groups) != len(output_names):
    raise ValueError("Количество названий выходных файлов должно совпадать с количеством групп изображений.")

for i in range(len(image_groups)):
    output_filename = output_names[i]
    output_path = os.path.join(output_folder, output_filename)
    combine_images_layers(image_groups[i], output_path)
    print(f'Скомбинировано изображение: {output_path}')
