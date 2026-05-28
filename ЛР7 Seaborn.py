import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('diamonds')
df = df.sample(n=500, random_state=50)
print(df)

def kde(dataset, x_column):
    plt.figure(figsize=(10, 6))
    sns.histplot(data=dataset, x=x_column, kde=True)
    plt.title('Распределение цены алмазов')
    plt.xlabel('Цена')
    plt.ylabel('Количество')
    plt.show()

def scatterplot(dataset, x_column, y_column, color_set):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=dataset, x=x_column, y=y_column, hue=color_set)
    plt.title('Зависимость цены от веса алмаза (учитывая огранку)')
    plt.xlabel('Вес')
    plt.ylabel('Цена')
    plt.legend(title='Огранка')
    plt.legend()
    plt.show()

def boxplot(dataset, x_column, y_column):
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=dataset, x=x_column, y=y_column)
    plt.title('Распределение цены по типу огранки')
    plt.xlabel('Огранка')
    plt.ylabel('Цена')
    plt.show()

def violinplot(dataset, x_column, y_column):
    plt.figure(figsize=(10, 6))
    sns.violinplot(data=dataset, x=x_column, y=y_column)
    plt.title('Распределение цены по типу огранки')
    plt.xlabel('Огранка')
    plt.ylabel('Цена')
    plt.show()

def heatmap(dataset):
    plt.figure(figsize=(10, 6))
    num_column = ['carat', 'depth', 'table', 'price', 'x', 'y', 'z']
    corr = dataset[num_column].corr()
    sns.heatmap(corr, annot=True)
    plt.title('Матрица корреляций параметров алмазов')
    plt.show()


kde(df, 'price')
scatterplot(df, 'carat',  'price', 'cut')
boxplot(df, 'cut', 'price')
violinplot(df, 'cut', 'price')
heatmap(df)
