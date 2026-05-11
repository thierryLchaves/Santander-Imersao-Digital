# Conteúdo Live 04/05/2026
## Introdução de lógica de programação (Tipos de variáveis e operações)

## Sumário: 

- [Conteúdo Live 04/05/2026](#conteúdo-live-04052026)
  - [Introdução de lógica de programação (Tipos de variáveis e operações)](#introdução-de-lógica-de-programação-tipos-de-variáveis-e-operações)
  - [Sumário:](#sumário)
- [Introdução de comandos](#introdução-de-comandos)
  - [Variáveis](#variáveis)
    - [Tipos de variáveis](#tipos-de-variáveis)
    - [Números](#números)
    - [Operadores Aritméticos](#operadores-aritméticos)
      - [Input do usuário](#input-do-usuário)

Conforme descrito um algorítimo e uma sequências de passos pre-determinado que se tem um __input__ e pelo passos dados se tem um __output__.  
Um dos exemplos que podemos ter e de ordenação, e laço de repetição demonstrado passo a passo conforme exemplo abaixo:  
```text
[7,7,1,5,2,6,4]
[]
[3,7,5,2,6,4]
[1]
[3,7,5,6,4]
[]
[1,2]
```
Esse exemplo demonstrado acima, e nomeado de  <a href="#select_sort"> <b> SELECTION SORT </b> </a>
<details id="select_sort">
<summary> SELECTION SORT </summary>
    <p> O Selection Sort é um algoritmo de ordenação simples, baseado em comparação, que organiza uma lista dividindo-a logicamente em duas partes: uma parte ordenada (à esquerda) e uma parte não ordenada (à direita). </br>
    O funcionamento básico segue estes passos repetitivos: </p>
    <ul>
        <li> Busca: Procura o menor elemento dentro de toda a parte não ordenada da lista. </li>
        <li> Troca: Troca esse elemento encontrado com o primeiro elemento da parte não ordenada (colocando-o na posição correta). </li>
        <li>Avanço: Move a fronteira entre as partes ordenada e não ordenada uma posição para a direita.</li>
    </ul>
    <p> Pontos-chave para desenvolvedores: </p>
    <ul>
        <li> Complexidade de Tempo: É ineficiente para grandes conjuntos de dados, possuindo uma complexidade de tempo de $O(n^2)$ tanto no melhor quanto no pior caso, já que ele sempre percorre a lista para encontrar o menor valor, independentemente de ela já estar parcialmente ordenada. </li>
        <li> Espaço: É um algoritmo in-place, ou seja, não requer memória adicional significativa, apenas uma variável temporária para a troca.</li>
        <li> Estabilidade: O Selection Sort clássico não é estável (a ordem relativa de elementos iguais pode ser alterada durante as trocas).</li>
    </ul>
</details>

A linguagem a ser utilizada durante o curso será `PYTHON`, conforme demonstrado no [código](src/Live04052026.py), foi demonstrado o primeiro comando de print
```py
print("Hello World")
```

# Introdução de comandos
## Variáveis
Seguindo os preceitos de código limpo, foi demonstrado que ao invés de se repetir uma mesma sentença __N__ vezes, podemos utilizar uma variável, e que facilita o processo tanto de escrita, quanto de manutenibilidade de código, uma variável pode ser utilizada tanto para reduzir o repetitividade do código visto que ao se realizar a modificação da variável, tal modificação será replicada nos demais locais, em vias de regra como é o funcionamento de uma variável e um valor que é alocado em um local da memoria ram, em comandos no python isso poderia ser escrito como 
```py 
# Introdução de variável
saudacao = "Hello World"
print(saudacao)
```

### Tipos de variáveis
Como realizamos já realizamos a introdução de variáveis, vamos aos tipos no exemplo acima da variável iremos realizar a introdução de __tipos__, tipos de variáveis são as classes que ele pertencem então letras são do tipo string desde que estejam entre `""`, e uma das possibilidades de fazer com strings são as concatenações ou soma de strings, conforme exemplo abaixo:
```py
palavra_1 = "Hello"
palavra_2 = "World"

saudacao =  palavra_1 + " "+ palavra_2
print(saudacao)

```
O resultado do código será :
```cmd 
Hello World
```
### Números
O python por ser dinamicamente tipado, ele já interpreta a qual classe ou tipo aquela variável pertence, portanto podemos seguir com o seguinte código:
```py
a = 2
b = 3 
print(f"A operacação {a}+{b} resulta em {a+b}")
```
Conforme vemos no exemplo acima temos a introdução do `F-string` a letra pós _()_, possibilita a concatenação  de strings com outros tipos o que possibilita por exemplo uma saída melhor formatada

### Operadores Aritméticos 
No `python`, temos a possibilidade de alguns operadores aritméticos, sendo eles 
> - Soma : Caracterizada pelo caractere __`+`__
> - Subtração : Caracterizada pelo caractere  __`-`__
> - Multiplicação : Caracterizada pelo caractere  __`*`__
> - Divisão  : Caracterizada pelo caractere  __`/`__
> - Potência : Caracterizada pelo caractere  __`**`__

#### Input do usuário
    Para que seja realizada a inserção via teclado é utilizado o comando `input`. 
    É valido ressaltar que a diferença entre `input` X `print`, e que o `input` estará sempre associado a uma variável.

Sobre a tipagem e apresentação do `f-string`, devido a dinâmica de tipagem do python ao se realizar __inputs__ com aprestação e necessário informar ao programa o tipo da variável , conforme exemplo: 
```py
a = int(input("Diga um número: "))
b = int(input("Diga outro número: "))
# Operadores Artiméticos +,-,*,/,**
print(f"A operacação {a}+{b} resulta em {a+b}")
```
<table align="center" style="border-collapse: collapse; margin-left: auto; margin-right: auto;"> 
  <caption><b>Skills do projeto</b></caption>
  <tr>
    <td style="padding: 5px;">
      <img alt="VS Code" src="https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white"/>
    </td>
    <td style="padding: 5px;">
      <img alt="Markdown" src="https://img.shields.io/badge/markdown-%23000000.svg?style=for-the-badge&logo=markdown&logoColor=white"/>
    </td>
    <td style="padding: 5px;">
      <img alt="Python" src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54"/>
    </td>
  </tr>
</table>


---
__Titulo:__ Introdução a lógica de programação (Tipos de variáveis e operações)  
__Autor:__ Thierry Lucas Chaves  
__Data de Criação:__ 04-05-2026  
__Data de Modificação:__ 04-05-2026  
__Versão:__ "1.0"