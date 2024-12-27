import pandas as pd

#df = pd.read_csv('hh.csv')
#df['Test'] = [new for new in range(29)]
#print(df)
#df.drop('Test', axis=1, inplace=True)
# либо df.drop(28, axis=0, inplace=True)
#print(df)


df = pd.read_csv("animal.csv")
print(df)
# для замены:
#df.fillna(0, inplace=True)

# для удаления:
#df.dropna(inplace=True)
#print(df)

#. Данные можно группировать по конкретным характеристикам, чтобы, например, выводить средние значения.
# В рассматриваемом датасете мы можем сгруппировать данные, например, по виду корма — растительный или мясной.
# Представим, что нам надо узнать среднюю продолжительность жизни животных в зависимости от того, чем они питаются.
# Для создания группы мы используем переменную group, для подсчёта среднего значения — mean. Прописываем:#df = pd.read_csv("animal.csv")
#group = df.groupby('Пища')['Средняя продолжительность жизни'].mean()
#print(group)

# для сохранения данных используем:
df.to_csv('output.csv', index=False)

# пример:
data = {
    'Name': ['Alice', 'Bob', 'Roma', 'Anna'],
    'Age': [23, 45, 17, 24],
    'City': ['New York', 'LA', 'Chicago', 'Moscow']
}
df = pd.DataFrame(data)
df.to_csv('output.csv', index=False)