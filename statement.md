# Date due liste ordinate di interi, fonderle in un'unica lista ordinata

Ricevete in input due array $A$ e $B$ di numeri interi. Compito della procedura

```get_two_sorted_lists_and_store_their_merge```

da voi implementata è collocare tutti gli elementi ricompresi in $A$ e tutti quelli ricompresi in $B$ in un'unico array $C$ che risulti esso stesso ordinato. L'ordinamento è sempre quello non-decrescente e la lunghezza (ossia il numero di elementi) di $C$ sarà la somma delle lunghezze di $A$ e di $B$.
Dopo aver costruito e memorizzato $C$ e quando la procedura `get_two_sorted_lists_and_store_their_merge` sarà ormai terminata, verrà più volte chiamata la funzione
```tell_element_in_pos```$(pos)$
con la quale vi chiederemo di specificare il valore dell'intero situato nella posizione $pos$ di $C$.
Per questo esercizio le posizioni partono da $0$.


### Goals:

 1. Correttezza. Tutte le tue risposte alle chiamate della seconda funzione devono essere corrette.
 2. Merge rapido: Il tempo di calcolo speso nella prima funzione deve essere al più lineare nell'input.
 3. Retrival efficiente. Alle singole domande devi rispondere in $O(1)$. Chiaramente, per rispondere in tempo costante dovrai aver utilizzato una struttura ad accesso diretto per la rappresentazione interna di $C$.

 Facciamo infine presente che per la memorizzazione di $C$ devi avvalerti di una variabile globale o quantomeno condivisa tra le due funzioni che sei chiamato ad implementare.
