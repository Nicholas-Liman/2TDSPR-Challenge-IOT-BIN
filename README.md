# 2TDSPR-Challenge-IOT-BIN

## Criamos um dataset mockado de 100 pessoas num span de 50 dias, o dataset contém IDs anonimizados dos usuários, além de indicar os habitos de higiene bucal deles.

O dataset contém:
* 14 Colunas
* 3000 Linhas

## Data Set
### **Atributos**
| Coluna                   | Descrição |
|-------------------------|------------|
| `user_id`              | Identificador único do usuário |
| `date`                 | Data do registro |
| `morning_brush`        | 1 se escovou, 0 se não |
| `afternoon_brush`      | 1 se escovou, 0 se não |
| `night_brush`         | 1 se escovou, 0 se não |
| `morning_floss`        | 1 se usou fio dental, 0 se não |
| `afternoon_floss`      | 1 se usou fio dental, 0 se não |
| `night_floss`          | 1 se usou fio dental, 0 se não |
| `morning_mouthwash`    | 1 se usou enxaguante bucal, 0 se não |
| `afternoon_mouthwash`  | 1 se usou enxaguante bucal, 0 se não |
| `night_mouthwash`      | 1 se usou enxaguante bucal, 0 se não |
| `total_brushes`        | Soma das escovações no dia (0 a 3) |
| `total_floss`          | Soma do uso de fio dental no dia (0 a 3) |
| `total_mouthwash`      | Soma do uso de enxaguante bucal no dia (0 a 3) |
| `streak_days`          | Quantidade de dias consecutivos seguindo um bom hábito |
| `score`               | Nota atribuída ao usuário naquele dia |

## Dados que o modelo realmente precisa para fazer a predição
### **Entrada de Dados Esperada**
| Feature           | Tipo  | Descrição |
|-------------------|------|-----------|
| `total_brushes`  | `int` (0-3) | Total de escovações no dia |
| `total_floss`    | `int` (0-3) | Total de vezes que usou fio dental |
| `total_mouthwash`| `int` (0-3) | Total de vezes que usou enxaguante bucal |
| `streak_days`    | `int` (0+)  | Quantidade de dias consecutivos seguindo um bom hábito |

--------------------------------------------------------------------------------------------------------------------------------------

## Exemplo de entrada
novo_usuario = np.array([[3, 2, 1, 5]])  # 3 escovações, 2 fios dentais, 1 enxaguante, 5 dias seguidos

## Exemplo de saída
92 [Plain number]


