import seaborn as sns
import plotly.express as px

df = sns.load_dataset('diamonds')
df = df.sample(n=500, random_state=50)
print(df)

def scatterplot(dataset, x_column, y_column, color_set):
    fig = px.scatter(
        dataset,
        x=x_column,
        y=y_column,
        color=color_set)
    fig.update_layout(
        title='Зависимость цены от веса алмаза (учитывая огранку)',
        xaxis_title = 'Вес',
        yaxis_title = 'Цена',
        legend_title_text = 'Огранка')
    fig.show()

def line_plot(dataset, x_column, y_column):
    df_sorted = dataset.sort_values([x_column, y_column])
    fig = px.line(df_sorted, x=x_column, y=y_column)
    fig.update_layout(
        title='Стоимость алмазов в зависимости от веса',
        xaxis_title = 'Вес',
        yaxis_title = 'Цена')
    fig.show()

def bar_chart(dataset, x_column, y_column):
    df_sorted = dataset.groupby(x_column)[y_column].mean().reset_index()
    fig = px.bar(df_sorted, x=x_column, y=y_column, color='cut')
    fig.update_layout(
        title= 'Глубина алмаза в зависимости от огранки',
        xaxis_title= 'Огранка',
        yaxis_title = 'Глубина')
    fig.show()

def heatmap(dataset):
    num_column = ['carat', 'depth', 'table', 'price', 'x', 'y', 'z']
    corr = dataset[num_column].corr()
    fig = px.imshow(corr, text_auto=True, title='Матрица корреляций параметров алмазов')
    fig.show()

def dropdown(dataset, x_column, y_column, color_set):
    fig = px.scatter(
        dataset,
        x=x_column,
        y=y_column,
        color=color_set)

    cutting = [trace.name for trace in fig.data]
    n = len(cutting)

    buttons = []
    buttons.append(dict(
        label='Все огранки',
        method='update',
        args=[{'visible': [True] * n}, {'title': 'Все огранки'}]))

    for i, cut in enumerate(cutting):
        visible = [False] * n
        visible[i] = True
        buttons.append(dict(
            label=cut,
            method='update',
            args=[{'visible': visible}, {'title': f'Огранка: {cut}'}]))

    fig.update_layout(
        updatemenus=[dict(buttons=buttons)],
        xaxis_title='Цена',
        yaxis_title='Вес',
        title='Зависимость цены от веса (по огранке)')
    fig.show()

scatterplot(df, 'carat', 'price', 'cut')
line_plot(df, 'carat', 'price')
bar_chart(df, 'cut', 'depth')
heatmap(df)
dropdown(df, 'carat', 'price', 'cut')
