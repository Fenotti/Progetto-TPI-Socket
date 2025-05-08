
## Obiettivo del programma
Abbiamo creato un gioco del **Tris (Tic Tac Toe)** a due giocatori, dove uno fa da **server** e l’altro da **client**. I due giocatori si trovano su due programmi distinti e comunicano tra loro tramite **connessione TCP**. Ognuno ha una propria interfaccia grafica in cui può cliccare sulle caselle per giocare.
---
## Divisione dei ruoli
* **Il server (Giocatore 1)** inizia la partita e gioca con la **X**
* **Il client (Giocatore 2)** si connette al server e gioca con la **O**
---
## Comunicazione tra client e server
* Si utilizza la **libreria socket di Python**, che permette a due programmi di comunicare tramite rete.
* Il **server** si mette in ascolto su una porta specifica (porta 5000).
* Il **client** inserisce l’indirizzo IP del server (in locale: `127.0.0.1`) e si collega.
---
##  Interfaccia grafica
* La GUI è realizzata con **Tkinter**, che mostra una griglia 3x3 con pulsanti.
* Ogni pulsante rappresenta una casella del Tris.
* Cliccando su un pulsante, viene fatta una mossa, il simbolo viene mostrato, e la mossa viene inviata all’altro giocatore.
---
##  Flusso della partita
1. Il **server** parte e aspetta una connessione.
2. Il **client** si collega al server.
3. Il **server (X)** fa la prima mossa cliccando sulla griglia.
4. Il server invia le coordinate della mossa al client.
5. Il client riceve le coordinate, aggiorna la sua griglia con la **X**.
6. Ora il **client (O)** può fare la sua mossa, che invia al server.
7. Si continua così finché:
  * uno dei due vince
  * oppure la griglia è piena (pareggio)
---
## 🧾 Logica del gioco
* Dopo ogni mossa, si controlla se c’è una **vittoria** (3 simboli in fila, colonna o diagonale).
* Se nessuno vince e tutte le caselle sono piene, è un **pareggio**.
* Quando si verifica una delle due condizioni, compare un **messaggio di fine partita**.
---
##  Controlli fondamentali
* Si può cliccare solo sulla propria GUI e **solo quando è il proprio turno**.
* Una cella può essere cliccata **una sola volta**.
* Ogni mossa viene **sincronizzata** tra client e server per tenere la griglia allineata.
---
##  In sintesi
* Il programma dimostra come combinare:
 * programmazione di rete (**socket TCP**)
 * interfaccia grafica (**tkinter**)
 * logica di gioco (**controllo turni e vincita**)
È un esempio pratico di come due programmi distinti possano comunicare in tempo reale e sincronizzare azioni tra due utenti.
