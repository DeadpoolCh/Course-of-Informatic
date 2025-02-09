import os
import shutil
from PIL import Image
import pytesseract
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import numpy as np

# Путь к папке с изображениями
source_folder = r"E:\Денис\ВУЗ\2 курс\ФизХимия 3кол"

# Папка для хранения групп
output_folder = r"E:\Денис\ВУЗ\2 курс\ФизХимия 3кол\Группы"

# Создаем папку для групп, если её нет
os.makedirs(output_folder, exist_ok=True)

# Функция для извлечения текста с изображения
def extract_text_from_image(image_path):
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img)
    return text.strip()

# Извлекаем текст с каждого изображения и сохраняем в список
texts = []
image_paths = []
for filename in os.listdir(source_folder):
    file_path = os.path.join(source_folder, filename)
    if filename.lower().endswith(('png', 'jpg', 'jpeg')):
        try:
            text = extract_text_from_image(file_path)
            if text.strip():  # Проверяем, что текст не пустой
                texts.append(text)
                image_paths.append(file_path)
            else:
                print(f"Текст не извлечен из {filename}")
        except Exception as e:
            print(f"Ошибка при обработке изображения {filename}: {e}")

# Печать извлеченных текстов для отладки
for i, text in enumerate(texts):
    print(f"Текст {i+1}: {text}")

# Преобразуем текст в векторы с использованием TF-IDF
if texts:  # Убедимся, что есть текст для обработки
    vectorizer = TfidfVectorizer(stop_words='english')
    try:
        X = vectorizer.fit_transform(texts)
    except ValueError as ve:
        print(f"Ошибка при векторизации: {ve}")
        X = None
else:
    print("Нет текста для обработки.")
    X = None

if X is not None:
    # Кластеризация текста с помощью KMeans
    num_clusters = 5  # Количество групп (можно настроить)
    kmeans = KMeans(n_clusters=num_clusters, random_state=42)
    kmeans.fit(X)

    # Создаем папки для каждого кластера
    for i in range(num_clusters):
        cluster_folder = os.path.join(output_folder, f'group_{i+1}')
        os.makedirs(cluster_folder, exist_ok=True)

    # Перемещаем изображения в соответствующие группы
    for idx, label in enumerate(kmeans.labels_):
        cluster_folder = os.path.join(output_folder, f'group_{label+1}')
        shutil.move(image_paths[idx], os.path.join(cluster_folder, os.path.basename(image_paths[idx])))

    print(f"Группировка завершена! Изображения сохранены в {output_folder}")
else:
    print("Не удалось выполнить кластеризацию. Возможно, извлеченные тексты пусты или содержат только стоп-слова.")
