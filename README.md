### 🦷 **Sistema de Gestão Odontológica - B.I.N.**

## 📌 **Sobre o Projeto**  
Este projeto foi desenvolvido como parte da disciplina **ADVANCED BUSINESS DEVELOPMENT WITH .NET** pela equipe **B.I.N.**, composta por:

👥 **Integrantes**  
- 🏆 **Igor Gabriel Marcondes** - RM553544  
- 🏆 **Maria Beatriz Fogolin** - RM552669  
- 🏆 **Nicholas Barbosa Lima** - RM552744  

🎯 **Objetivo**  
O sistema foi desenvolvido em **ASP.NET Core C#** para fornecer um **backend escalável** para a **gestão de dentistas e clientes**. Ele permite:  
✔️ **Cadastro, atualização, consulta e exclusão** de clientes e funcionários.  
✔️ Integração com um **banco de dados Oracle SQL**.  
✔️ Uso de **inteligência artificial** para análise de dados coletados.

---

## 📊 **2TDSPR-Challenge-IOT-BIN**

A equipe **B.I.N.** criou um dataset **mockado** de 100 pessoas ao longo de 50 dias, contendo hábitos de higiene bucal com IDs anonimizados.  

O **dataset** contém:  
* **14 colunas**  
* **3000 linhas**

Cada linha representa um **dia** e guarda dados relacionados aos **hábitos de higiene bucal** de um usuário.  
Abaixo estão os detalhes do dataset.

---

### **Data Set**

#### **Atributos**  
| Coluna                | Descrição |
|-----------------------|-----------|
| `user_id`             | Identificador único do usuário |
| `date`                | Data do registro |
| `morning_brush`       | 1 se escovou de manhã, 0 se não |
| `afternoon_brush`     | 1 se escovou à tarde, 0 se não |
| `night_brush`         | 1 se escovou à noite, 0 se não |
| `morning_floss`       | 1 se usou fio dental de manhã, 0 se não |
| `afternoon_floss`     | 1 se usou fio dental à tarde, 0 se não |
| `night_floss`         | 1 se usou fio dental à noite, 0 se não |
| `morning_mouthwash`   | 1 se usou enxaguante bucal de manhã, 0 se não |
| `afternoon_mouthwash` | 1 se usou enxaguante bucal à tarde, 0 se não |
| `night_mouthwash`     | 1 se usou enxaguante bucal à noite, 0 se não |
| `total_brushes`       | Soma de escovações no dia (0 a 3) |
| `total_floss`         | Soma de uso de fio dental no dia (0 a 3) |
| `total_mouthwash`     | Soma de uso de enxaguante bucal no dia (0 a 3) |
| `streak_days`         | Quantidade de dias consecutivos mantendo bons hábitos |
| `score`               | Nota atribuída ao usuário no dia |

---

### **Entrada de Dados Esperada para Previsão**

| Feature            | Tipo  | Descrição |
|--------------------|-------|-----------|
| `total_brushes`    | `int` (0-3) | Total de escovações no dia |
| `total_floss`      | `int` (0-3) | Total de vezes que usou fio dental |
| `total_mouthwash`  | `int` (0-3) | Total de vezes que usou enxaguante bucal |
| `streak_days`      | `int` (0+)  | Quantidade de dias consecutivos com bons hábitos |

---

### **Exemplo de Entrada**  
```python
novo_usuario = np.array([[3, 2, 1, 5]])  # 3 escovações, 2 fios dentais, 1 enxaguante, 5 dias seguidos
```

### **Exemplo de Saída**  
```text
92  # Número simples (nota atribuída)
```

### 📥 **Formato da Requisição**

O servidor foi configurado para **receber apenas dados numéricos**. Isso torna o pacote de dados mais seguro e difícil de ser manipulado por agentes maliciosos.  

Exemplo de entrada via JSON:
```json
[3, 2, 1, 5]
```
Esse é um vetor simples, representando **3 escovações**, **2 usos de fio dental**, **1 uso de enxaguante bucal** e **5 dias consecutivos** com bons hábitos.
