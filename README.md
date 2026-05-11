## Projeto Detecção de Fraude - Classificação
Este projeto usa Machine Learning para identificar transações fraudulentas. 
O foco principal é equilibrar a detecção de fraude (Recall) com uma boa experiência para o cliente (Precision).
Objetivo é analisar as transações: valor, hora, local e classificar: 
**Isso é Legítimo/não fraude** 
ou
**Isso é Fraude**

**🚀 Insight Principal:** A redução estratégica do dataset onde revelou que a variável **V14** é o real indicador de fraude. 
Isso permitiu um modelo leve, rápido e com alto Recall, sem perda de precisão diagnóstica.
O arquvio base foi o creditcard.csv do site do Kaggle

---

### 🛠️ 1. Metodologia e Ferramentas

* **Modelo Supervisionado de Classificação**
Realizei um teste comparativo entre os 2 algoritmos Random Forest e Logistic Regression.
O modelo **Random Forest** teve o melhor desempenho.  
* **Random Forest:** Utilizado para lidar com a complexidade e evitar pequenos erros do modelo.
    Como usei o RandomForestClassifier, o modelo "sabe" quais colunas foram mais importantes para decidir se era fraude ou não. 
    Isso ajuda a entender o modelo.
    * **Matriz de Confusão:** Essencial para saber se o modelo está errando mais o "falso positivo" (bloquear um cliente honesto) ou o "falso negativo" = não detectar a fraude. Aqui diz **onde** o modelo errou.
    * **Features/Gráfico de Importância:** Diz o **porquê**. Se a variável **V14** está no topo, sabemos que o comportamento dela é o maior **"dedo-duro"** da fraude. O modelo identifica quais colunas foram mais importantes para a decisão.
    * **Curva Precision-Recall:** O melhor gráfico para dados desbalanceados. Diz a estabilidade; se a linha cair muito rápido, o modelo é instável para casos raros.
    * **Visualização de uma Árvore:** O Random Forest cria várias árvores. Analisei a primeira/index 0 para entender a lógica e as perguntas que o modelo faz tipo "O valor da compra é > X?"  Se sim, vá para a esquerda...".
    * **BoxPlot:** Para visualização da variável importante.
* **Logistic Regression:** Para entender a probabilidade base (0 a 1).

---

### 📈 2. Fluxo do Projeto

a. **Coleta:** Download do dataset original no Kaggle creditcard.csv.
b. **Ajuste de Escala:** Diminui o dataset para reduzir o tamanho, com o original não foi possível fazer download no GitHub, nome = creditcard_reduzido10mil.csv.
Observação: eu fiz análise tanto no dataset original quanto neste reduzido e obtive resultados diferentes.
c. **Limpeza:** Remover dados nulos e normalizar valores, exemplo: transformar R$1,00 e R$10.000,00 para uma escala entre 0 e 1.
d. **Divisão:** Separar 80% dos dados para treino e 20% para modelo testar e ver se aprendeu.
e. **Treino:**  comando `fit` para treinar o modelo.

##### 🔬 Experimentos com Amostragem = Prova Técnica
Para chegar ao modelo ideal, testei o comportamento do algoritmo **Random Forest** em três cenários = 3 tamanhos de dataset:

* **Cenário 1 = dataset Original:** 284.807 registros (apenas 0,17% são fraudes). O desbalanceamento extremo mascara a realidade através da acurácia.
* **Cenário 2 = redução proporcional :** 10.000 registros, mantendo a proporção original que eram apenas **17 casos de fraudes**. O modelo não teve dados suficientes para aprender o padrão.
* **Cenário 3 = redução estratégica :** 10.000 registros, mas mantendo todos os **492 casos de fraude** originais, não reduzi os casos de fraude. A proporção subiu para **4,92%**.

| Cenário | Descrição | Resultado |
| :--- | :--- | :--- |
| **1. Original** | 284.807 registros (0,17% fraude) | Acurácia enganosa; V17 parecia mais importante. |
| **2. Proporcional** | 10.000 registros (17 fraudes) | Dados insuficientes para o aprendizado. |
| **3. Estratégico** | 10.000 registros (**492 fraudes**) | **V14 revelada como indicador crítico.** Equilíbrio ideal. |

**Conclusão:** O **3º cenário** foi o único que permitiu ao modelo identificar a variável **V14** como o real indicador crítico, alcançando o equilíbrio ideal entre Recall e Precision. Os demais cenários inclusive identificaram a V17 como  variável de importância.

---

### 📊 3. Avaliação: Ver a precisão do modelo -- Acurácia /Accuracy

O passo crucial é entender como medir se o seu modelo é realmente bom não podemos apenas olhar para **acurácia**
Em problemas de classificação, **não basta olhar apenas para a "acurácia"** que é a porcentagem de acertos totais.
> **Por que ela engana?** > Se o modelo fosse "burro" e simplesmente dissesse que toda transação é legítima, ele teria **99,8% de acurácia**, pois acertaria todos os casos normais. Porém, ele falharia em detectar 100% das **fraudes**.

##### Olhar ... Macro Avg
1º. **Recall:** A métrica mais importante em detecção de fraude onde captura a fraude.
2º. **Macro Avg:** O "juiz rigoroso". Se ele estiver baixo, o modelo não aprendeu a classe minoritária (fraude), mesmo que a média geral pareça boa.
3º. **F1-Score:** O equilíbrio real =média harmônica entre precisão e revocação.

> **Exemplo:** Se em um banco 99% das transações são legítimas e o modelo diz que "tudo é legítimo", ele terá 99% de acurácia, mas falhará em detectar todas as fraudes. É aqui que entra a **Matriz de Confusão**.


##### Entendendo a Matriz de Confusão
Ela divide os resultados em quatro quadrantes:
* ✅ **Verdadeiro Positivo (TP):** = SUCESSO - Era fraude e o modelo acertou.
* ✅ **Verdadeiro Negativo (TN):** = SUCESSO - Era compra normal e o modelo liberou.
* ❌ **Falso Positivo (FP):** = ERRO - Era compra normal, mas o modelo bloqueou (Gera atrito).
* ❌ **Falso Negativo (FN):** = ERRO - Era fraude, mas o modelo deixou passar (Prejuízo).

##### Métricas utilizadas:
* **Precision (Precisão):** De todas as vezes que o modelo disse ser "Fraude", quantas eram mesmo? Evita o Falso Positivo.
* **Recall (Revocação):** De todas as fraudes reais, quantas o modelo pegou Evita Falso Negativo. Era fraude mas nao marcou como fraude
* **F1-Score:** Equilíbrio entre Precisão e Recall. É a melhor métrica para este projeto. É a média harmônica.

---
### 🔍 4. O que observar no resultado

* **Quadrante "Fraude x Fraude" (Recall):** Se houver muitos casos onde era Fraude mas o modelo previu Legítimo (Falso Negativo), a Empresa perde dinheiro.
* **Quadrante "Legítimo x Fraude" Falso Positivo:** Se esse número for alto, bloqueia clientes bons e gera reclamações.
* **Métrica F1-Score:** Como as fraudes são poucas, ou seja, dados desbalanceados, esta métrica resume se o modelo está equilibrado.
A resposta nao será de  "sim" ou "não". 
Várias métricas coom uma visão analítica completa da "inteligência" do modelo.

### 🎯 5. Tenho três tipos de respostas do modelo

1º. **Resposta Visual = Matriz de Confusão:** Gráfico de calor (heatmap).
   Mostra onde o modelo acertou e onde ele se confundiu
   * *Eixo Vertical:* Realidade / *Eixo Horizontal:* Previsão.
   * Canto superior esquerdo: SUCESSO=CORRETOS - Legítimo/Não fraude (clientes honestos).
   * Canto inferior direito: SUCESSO=CORRETOS -  Fraude (capturados).
   * Canto inferior esquerdo (**O Perigo**): ERRO=PREJUIZOS - Fraudes (que passaram como normais).
   * Canto superior direito: RRO=PREJUIZOS - Não Fraude (bloqueio indevido eram compras normais).

2º. **Resposta Estatística (Relatório de Classificação):** Tabela de 0 a 1 (0% a 100%). 
Com respostas de Precision, Recall e F1-Score
   * **Precision:** Chance de acerto ao dizer que é fraude.
   * **Recall:** Porcentagem de fraudes totais capturadas.
   * **F1-Score:** "Nota final" do modelo. Se o valor estiver baixo, o modelo precisa de mais treino ou dados melhores.

3º. **Resposta Prática (Predição Individual):** Teste com dados novos, é uma simulação em tempo real. Resposta 0 ou 1
   * `[0]`: transação legítima=Não Fraude.
   * `[1]`: transação Fraude.

---

### 📝 6. Resumo Final

O modelo Random Forest demonstrou um desempenho sólido e consistente. No Cenário 3, consegui um resultado técnico muito próximo ao do arquivo completo (284 mil linhas), mas processando apenas 10 mil registros.

Resultados do Cenário 3:
Recall = 80,61%: O modelo identificou corretamente 79 das 98 fraudes presentes no teste.

Precisão Elevada: O modelo cometeu apenas 1 erro ao classificar uma transação legítima (era OK e ele disse ser fraude), mantendo a experiência do cliente protegida.

Insight da V14: A estratégia de amostragem permitiu identificar que a variável V14 é o indicador mais forte de comportamento fraudulento neste conjunto de dados.

##### Conclusão:
O modelo é conservador e eficiente. 
Ele prioriza a precisão para não bloquear clientes honestos sem necessidade, enquanto mantém uma taxa de captura de fraude superior a 80%. 
O meu experimento prova que a qualidade da amostragem  de manter todos os casos de fraude é mais importante do que o volume total de dados.