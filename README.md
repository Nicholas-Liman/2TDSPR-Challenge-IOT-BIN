# 2TDSPR-Challenge-IOT-BIN

## Criamos um dataset mockado de 100 pessoas num span de 50 dias, o dataset contém IDs anonimizados dos usuários, além de indicar os habitos de higiene bucal deles.

O dataset contém:
* 14 Colunas
* 3000 Linhas

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


Caso tenha sido utilizado 1, caso não tenha 0.
Para criar um dataset que possa treinar o modelo de IA para avaliar a higiene bucal dos usuários, precisamos estruturar os dados de forma a representar corretamente os hábitos de escovação, a frequência e o uso do fio dental e enxaguante bucal ao longo do tempo.


