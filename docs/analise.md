## 🕵️ Análise: Arquivo `creditcard_reduzido10milfraudes.csv`

O objetivo deste Projeto foi verificar qual modelo é o melhor para detectar fraude em uma compra de cartão de crédito.
* **0** = OK=Legítimo=Não fraude
* **1** = Fraude

### 🧪 Meus Testes com o Random Forest

Eu testei o modelo Random Forest com 80% para treino e 20% para teste nos 3 arquivos para ver a diferença de aprendizado.

| Arquivo | Descrição | Registros OK (0) | Registros Fraude (1) | Total de Dados |
| :--- | :--- | :--- | :--- | :--- |
| **1º Original** | Dataset completo do Kaggle | 284.315 (99,82%) | 492 (0,17%) | 284.807 |
| **2º Reduzido** | Proporcional ao original | 9.983 | 17 | 10.000 |
| **3º Estratégico** | Todos os casos de fraude | 9.508 | 492 | 10.000 |

**Observação:** No 3º arquivo, a proporção é diferente do original..  
O usei Random Undersampling, reduzi os dados em 96%, mantendo todos os 492 casos de fraude..  


#### 📊 1º Arquivo original
Total de 284.807 reegistros/dados, sendo 284.315=0=99.8272%=OKnaofraude e 492=1=1.01728%=fraude

| Classe | Precision | Recall | F1-Score | Support |
| :--- | :--- | :--- | :--- | :--- |
| **0 = Legítimo** | 1.00 | 1.00 | 1.00 | 56.864 |
| **1 = Fraude** | 0.94 | 0.82 | 0.87 | 98 |
| | | | | |
| **Acurácia (Accuracy)** | | | **1.00** | 56.962 |
| **Macro Avg** | **0.97** | **0.91** | **0.94** | 56.962 |
| **Weighted Avg** | 1.00 | 1.00 | 1.00 | 56.962 |

Estes são os números finais obtidos após o treinamento e teste do modelo..  
Note que a métrica **Macro Avg** é a que melhor representa o sucesso do aprendizado equilibrado.

#### 📊 2º Arquivo reduzido 
Total 10mil dados, sendo  9983=0=OKnaofraude e 17=1=fraude, mesma proporcao original

| Classe | Precision | Recall | F1-Score | Support |
| :--- | :--- | :--- | :--- | :--- |
| **0 = Legítimo** | 1.00 | 1.00 | 1.00 | 1.997 |
| **1 = Fraude** | 0.75 | 1.00 | 0.86 | 3 |
| | | | | |
| **Acurácia (Accuracy)** | | | **1.00** | 2.000 |
| **Macro Avg** | **0.88** | **1.00** | **0.93** | 2.000 |
| **Weighted Avg** | 1.00 | 1.00 | 1.00 | 2.000 |

Este cenário demonstra as métricas quando mantemos a proporção original de 0,17% de fraudes em um dataset menor.. 
Com apenas 3 casos de fraude no suporte de teste, os resultados podem ser instáveis.

#### 📊 3º Arquivo reduzido com todos os casos de fraude
Total 10 mil dados mas com todos os registros/casos de fraude do arquivo original, sendo 9.508=0=95.08%=naofraude e  
492=1=4.92%=fraude, proporcao diferente do arquivo original

| Classe | Precision | Recall | F1-Score | Support |
| :--- | :--- | :--- | :--- | :--- |
| **0 = Legítimo** | 0.99 | 1.00 | 0.99 | 1.902 |
| **1 = Fraude** | **0.99** | 0.81 | 0.89 | 98 |
| | | | | |
| **Acurácia (Accuracy)** | | | **0.99** | 2.000 |
| **Macro Avg** | **0.99** | **0.90** | **0.94** | 2.000 |
| **Weighted Avg** | 0.99 | 0.99 | 0.99 | 2.000 |

Este cenário representa o equilíbrio ideal alcançado no projeto. 
 concentrar todos os casos de fraude originais em um dataset de 10 mil registros, o modelo obteve a melhor performance de precisão.

              
### ⚖️ Comparativo Geral dos Experimentos

Esta tabela compara o desempenho do modelo Random Forest nos três cenários de dados testados.

| Métrica | Arquivo Completo | Arquivo Reduzido | Com Fraude / Reduzido |
| :--- | :--- | :--- | :--- |
| **Total de Registros** | 284.807 | 10.000 | 10.000 |
| **Amostra (Teste)** | 56.692 | 2.000 | 2.000 |
| **Classe 0 (Total/Teste)** | 284.315 / 56.864 | 9.983 / 1.997 | 9.508 / 1.902 passou 19 como legitimo e eram fraude|
| **Classe 1 (Total/Teste)** | 492 / 98 | 17 / 3 | 492 / 98 (*) aqui igual completo |
| **Porcentagem (0/1)** | 99,82% / 0,17% | 99,82% / 0,17% | **95,08% / 4,92%** |
| **Variável Importante** | V17 | V17 | **V14** |
| **Acerto Fraude (Recall)** | 80/98 (**81,63%**) | 3/3 (100%) | 79/98 (**80,61%**) |
| **Erro (Era Fraude)** | 18/98 (18,37%) | 0/3 | 19/98 (19,39%) |
| **Acerto OK (Legítimo)** | 56.859/56.864 (99,99%) | 1.996/1.997 (99,95%) | 1.901/1.902 (99,95%) |
| **Erro (Era OK)** | 5/56.864 (0,01%) | 1/1.997 (0,05%) | 1/1.902 (0,05%) |

(*) *Neste cenário, mantive o mesmo número de casos de fraude do arquivo completo para garantir o aprendizado.*

---

### 📊 Resultado das métricas ---------------------------------------

* **Precision /Precisão:** de todas as vezes que o modelo disse é "Fraude", ele acertou..  
   Portanto o modelo é confiável para evitar o **Falso Positivo** que é bloquear um caso que não e fraude (cliente honesto).
* **Recall /Revocação:** de todas as fraudes que realmente aconteceram o modelo conseguiu pegar 81%..  
   Portanto o modelo é conservador, deixa passar algumas fraude mas não interrompe o cliente honesto. 
   * **Observação:** o desafio é equilibrar o Recall com a Precision para não bloquear **Não freaud** clientes honesto.
* **F1-Score:** é a média harmônica entre a Precisão e o Recall. Como os dois estão altos, o F1 mostra que o modelo  é equilibrado..  
   Mas temos que olhar então para o Macro AVG, será decisivo.
* **Macro Avg:** ele está alto, tem 99%, significa que aprendeu e prova que o modelo é um sucesso.
* **Acurácia:** Aqui está o maior perigo do modelo, tem 100% de acurácia, mas ela sozinha não diz nada.

---

## 📊 Modelo Random Forest teve um deempenho excelente
O modelo é um sucesso com um aprendizado equilibrado garantindo uma confiabilidade de 99% definido pela métrica Macro Avg..  
Insight : ele identificou a V14 como outra variável importante para distinguir o tipo de transação..  
No 3º arquivo  consegui um resultado técnico muito próximo ao do arquivo completo que era muito grande processando apenas 10 mil registros..  
* Cuidado, nem sempre a Acurácia de 100% define se o modelo e bom ou ruim, temos que também olhar para as outras métricas : precision, recall e macro avg.