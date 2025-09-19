import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Товар': ['Яблоки', 'Бананы', 'Люди','Апельсины'],
    'Цена': [100, None, 150, 200],
    'Количество': [50, 200, 1500, 30]
}

df = pd.DataFrame(data)

# Заполнение пропусков медианой
df['Цена'] = df['Цена'].fillna(df['Цена'].median())

# Удаление выбросов
df = df[(df['Количество'] >= 1) & (df['Количество'] <= 1000)]

# Новая колонка
df['Общая_стоимость'] = df['Цена'] * df['Количество']

# Группировка и график
grouped = df.groupby('Товар')['Общая_стоимость'].sum()
grouped.plot(kind='bar', title='Выручка по товарам', color='pink', edgecolor='black')
plt.ylabel('Выручка')
plt.savefig('1.png', dpi=300, bbox_inches='tight')
plt.show()
