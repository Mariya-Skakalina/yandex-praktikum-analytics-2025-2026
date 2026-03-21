import os

folders = [
    'russia_tourism_analysis/data/raw',         # Сюда кладем скачанные файлы (не трогаем их)
    'russia_tourism_analysis/data/processed',   # Сюда сохраним очищенные таблицы (df.to_csv)
    'russia_tourism_analysis/notebooks',        # Для ваших .ipynb файлов
    'russia_tourism_analysis/reports/figures',  # Для графиков (plt.savefig)
    'russia_tourism_analysis/src'               # Для функций (если будут)
]


for folder in folders:
    os.makedirs(folder, exist_ok=True)
    print(f"Папка создана или уже существует: {folder}")

# Создаем пустой README.md для описания проекта
if not os.path.exists('russia_tourism_analysis/README.md'):
    with open('russia_tourism_analysis/README.md', 'w', encoding='utf-8') as f:
        f.write('# Анализ туристической отрасли РФ\nПроект в рамках обучения на продуктового аналитика.')
    print("Файл README.md создан")
