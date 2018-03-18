
# coding: utf-8

# <h1>Venda de videogames na História</h1>
# <br>
# Este projeto foi criado por <b>epistemophile</b>.Aqui irie realizar algumas analises sobre os dados
# encontrados <a herf='https://gist.github.com/zhonglism/f146a9423e2c975de8d03c26451f841e'>neste data set</a>
# 

# In[20]:


get_ipython().magic(u'matplotlib inline')
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('ggplot')


# In[21]:


#leitura do arquivo
videogames = pd.read_csv('vgsales.csv')


# In[22]:


#exibindo as 10 primeiros linha do dataframe
videogames.head(10)


# In[23]:


#resumo de todas as informações
videogames.describe()


# In[24]:


#tipo de dado de cada coluna
videogames.dtypes


# In[25]:


#quantidade de colunas no dataset
videogames.shape


# In[26]:


#Renomeando colunas
videogames.columns = ['Ranking', 'Nome', 'Plataforma', 'Ano','Gênero', 
                      'Editora', 'Vendas América do Norte', 'Vendas EUA',
                        'Vendas Japão', 'Outras vendas', 'Vendas Global']


# In[27]:


#exibindo as primeiras linhas do programa
videogames.head(10)


# In[28]:


videogames[videogames['Ano'].isnull()].head()


# In[29]:


# jogos que foram lançados para cada plataforma
titulos_lancados = videogames['Plataforma'].value_counts()
titulos_lancados.plot()
videogames['Plataforma'].value_counts().plot()


# In[30]:


#função que criar grafico em uma linha
videogames['Plataforma'].value_counts().head(10).plot(kind='bar',figsize=(11,5), grid = False , rot = 0,color ='green')

#enfeitando o grafico.Abaixo,definimos um titulo
#plt.title('Os videosgames com mais titulos lançados')
#plt.xlabel('Videogame')
#plt.ylabel('Quantidade de jogos lançados')
#plt.show()#exibindo o grafic



# In[31]:


#os 10 jogos mais vendidos
top_10_vendidos = videogames[['Nome','Vendas Global']].head(10).set_index('Nome').sort_values('Vendas Global', ascending=True)
top_10_vendidos.plot(kind='barh',figsize=(11,5),grid=False,color='darkred', legend=False)

plt.title('10 Jogos mais vendidos do mundo')
plt.xlabel('Total de vendas(em milhões de dolares)')
plt.show()


# In[32]:


crosstab_vg = pd.crosstab(videogames['Plataforma'],videogames['Gênero'])
crosstab_vg.head()



# In[33]:



crosstab_vg['Total'] = crosstab_vg.sum(axis=1)
crosstab_vg.head()


# In[34]:


top10_platforms = crosstab_vg[crosstab_vg['Total']>1000].sort_values('Total',ascending = False)
top10_final = top10_platforms.append(pd.DataFrame(top10_platforms.sum(),columns=['total']).T, ignore_index=False)

sns.set(font_scale=1)
plt.figure(figsize=(18,9))
sns.heatmap(top10_final, annot=False, vmax=top10_final.loc[:'PS', :'Strategy'].values.max(), vmin=top10_final.loc[:,:'Strategy'].values.min(), fmt='d')
plt.xlabel('Gênero')
plt.ylabel('console')
plt.title('Quantidade de titulos por Gênero e console')
plt.show()



