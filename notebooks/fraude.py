# Projeto Detecção de Fraude 
# Classificação s/n, 1/2

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, classification_report, PrecisionRecallDisplay, RocCurveDisplay
from sklearn.tree import plot_tree

# 1. Carregar os dados reais
df = pd.read_csv('../data/creditcard_reduzido10milfraudes.csv')
print("\n ^^^^^^^^^^^ Dados Arquivo ^^^^^^^^^^")
print(df.head(10))
print(df.info())
print(df['Class'].value_counts())
print(df['Class'].value_counts(normalize=True))

# 2. Preparação (X = características, y = alvo/fraude)
X = df.drop('Class', axis=1) # Remove a coluna target Class
y = df['Class']              # Define a coluna resposta/target (0=Bom, 1=Fraude)

# 3. Divisão Treino e Teste (80% treina, 20% testa)
# todo modelo utiliza sempre esta linha de separaçao treino, teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)


# ----- 1º modelo
# 4. ------  Random Forrest ------- 
# Criando e treinando o modelo / algoritimo 
# algoritmo com nome RandomForestClassifier, modelo de aprendizado por conjunto
# segue regras de If/then, classifica
# mais lento
# n_estimators = 100 é o padrao, mas posso aumentar o modelo vai demorar mas ficara mais preciso,
# se dimuinuir o modelo ficará mais rápido e menos preciso
# mas 100 já está ótimo 
modelo = RandomForestClassifier(n_estimators=100, random_state=42)
modelo.fit(X_train, y_train) # treino

#  ------- 2º modelo
# 5. --------- Regression logistic / Regressao logistica ------- 
# Criando o modelo de Regressão Logística
# segue uma fórmula matemática de soma e pesos
# mais rápido
# max_iter = 1000 é o limite de tentativa e erro
modelo_log = LogisticRegression(max_iter=1000)
modelo_log.fit(X_train, y_train) # treino


# 6. Previsões com os dados de teste
# previsao random forest
y_pred = modelo.predict(X_test)
# previsao modelo regressao logistica^
y_pred_log = modelo_log.predict(X_test)


# 7. Relatório de Métricas (Precision, Recall e F1-Score)
print("\n ^^^^^^^^^^^ Random Forest ^^^^^^^^^^")
print(classification_report(y_test, y_pred))
print("\n ^^^^^^^^^^^ Logistic Regression ^^^^^^^^^^")
print(classification_report(y_test, y_pred_log))


# 8. Gráficos --------- Random Forest --------
#  Matriz de Confusão visual
# diz onde modelo errou
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['Legítimo', 'Fraude'], yticklabels=['Legítimo', 'Fraude'])
plt.xlabel('Previsão do Modelo')
plt.ylabel('Valor Real (Gabarito)')
plt.title('Matriz de Confusão: Detecção de Fraude')
plt.show()

#  Features --- Gráfico de Importância das Variáveis/features
# diz o porquê. 
# Se a variável V14 está no topo, você sabe que o comportamento dessa variável é o maior "dedo-duro" da fraude.
"""  Como você usou RandomForestClassifier, o modelo "sabe" quais colunas foram mais importantes para decidir se era fraude ou não. 
Isso ajuda a entender o modelo.
"""
importancias = modelo.feature_importances_
df_importancia = pd.DataFrame({'Feature/Variavel': X.columns, 'Importancia': importancias}).sort_values(by='Importancia', ascending=False)
plt.figure(figsize=(10, 6))
sns.barplot(x='Importancia', y='Feature/Variavel', data=df_importancia.head(10), palette='viridis', hue='Feature/Variavel')
plt.title('Top 10 Variáveis mais importantes para detectar Fraude')
plt.show()

# CURVA PRECISION-RECALL ----
# O melhor gráfico para dados desbalanceados, como este
# diz a estabilidade. Se a linha cair muito rápido, o modelo é instável para casos raros.
plt.figure(figsize=(8, 6))
# ax = plt.gca()
PrecisionRecallDisplay.from_estimator(modelo, X_test, y_test, ax=plt.gca(), color='red')
plt.title('Curva Precision-Recall')
plt.show()

# VISUALIZAÇÃO DE UMA ÁRVORE  ---
# O Random Forest cria várias árvores. 
# Vamos ver apenas a primeira que é o index 0
# mostra a lógica. É aqui dá pra ver o modelo fazendo perguntas do tipo: "O valor da compra é maior que X? Se sim, vá para a esquerda...". É a melhor forma de entender como ele pensa
plt.figure(figsize=(20, 10))
plot_tree(modelo.estimators_[0], 
          feature_names=X.columns, 
          class_names=['Normal', 'Fraude'], 
          filled=True, 
          max_depth=3) # Limitamos a profundidade para conseguir enxergar
plt.title('Visualização de 1 Árvore da Floresta-- Nível 3')
plt.show()


# 9  Comparando uma variável específica entre as classes
# Boxplot de Distribuição (Outliers)
# Para entender por que o modelo escolheu certas variáveis, escolha a variável mais importante 
# (geralmente a V17, V14 ou V12 nesse dataset) e veja como ela se comporta em transações normais vs. fraudes.

plt.figure(figsize=(10, 6))
sns.boxplot(x='Class', y='V14', data=df) # V14 costuma ser muito relevante
plt.title('Distribuição da Variável V14: Legítimo (0) vs Fraude (1)')
plt.show()
