# O problema das N damas
Dado um tabuleiro de Xadrez N x N, em quais casas podemos posicionar N rainhas sem que nenhuma rainha seja ameaçada por outra?

Para resolver esse problema, é necessário implementar um algoritmo recursivo de **tentativa e erro** (Backtracking) para econtrar a solução. Como mostrado nesta imagem, temos uma árvore de recursão que mostra todas as tentativas de alocar as N rainhas no tabuleiro.

![diagram](image.png)
<sup>_Fonte: GeeksForGeeks_</sup>

Esta é a função recursiva que resolve o tabuleiro:
```
Função solve(board, col):
    Se col >= N:
        Retorne Verdadeiro

    Para cada i de 0 até N-1:
        Se é seguro colocar a rainha em board[i][col]:
            board[i][col] <- 1
            Se solve(board, col + 1) for Verdadeiro:
                Retorne Verdadeiro
            board[i][col] <- 0
    
    Retorne Falso
```