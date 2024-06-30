# Deriving $TK_{ST}$

## Algorithm 1 Description
### Step 1

As $MESG_1$ traversed an open channel, the adversary gained access to $P_R$, $CH_R$, and $TI_R$. The hash output being 160 bits limits the Hamming weight to a maximum of 160. Identifiers $IDN_T$, $IDN_S$, $IDN_R$, and random numbers like $R_O$ are all 160 bits. Timestamps are 32 bits per ULBRAPS specifications. On the Reader side, computing $P_R$ involves $(RO \oplus IDN_T \oplus TI_R)$, where $(TI_R \oplus IDN_T)$ has a Hamming weight ranging from 0 to 160. With the adversary's access to $TI_R$, $(R_O \oplus IDN_T)$ offers 161 potential states. Given $P_R$ and $CH_R$, $(R_O \oplus IDN_T)$ is reliably obtained by verifying $h(IDNT \oplus RO \oplus PR) = CH_R$, requiring 161 hash calculations.

<img src="https://github.com/nargesmokhtari/ULBRAP-Protocol/assets/126694721/bd1eedef-851c-45cd-a5d0-e4c53fb80e98" alt="Step 1" width="500"/>

### Step 2

Employing the same approach and considering the transparency of $\{P_T, TI_T\}$ of $MESG_2$ to the attacker, we will have 160 states for $(R_O \oplus IDN_S)$. Therefore, since the value of $(TI_T \oplus IDN_T)$ could rotate zero to 161 bits, we will have 161 states for $(R_O \oplus IDN_S)$. 

<img src="https://github.com/nargesmokhtari/ULBRAP-Protocol/assets/126694721/4a8f28dc-32e2-4d1b-be29-d270e94eb9ac" alt="Step 1" width="500"/>

### Step 3
By XORing the known value of $(R_O \oplus IDN_T)$ with known 161 values of $(R_O \oplus IDN_S)$, we can derive 161 candidates for $(IDN_S \oplus IDN_T)$ with at most 161 hash calculations.

<img src="https://github.com/nargesmokhtari/ULBRAP-Protocol/assets/126694721/db48147f-7598-450a-a155-dda672114166" alt="Step 1" width="500"/>

### Step 4

When the Supply chain node (S) receives $MESG3$, it computes $(S_E)$ and $(S_F)$ and sends them in $MESG_4$ through an open channel. $MESG4$ consists of ${S_E, S_F, S_G, TI_S}$, making $(S_E)$ known to the network. $(S_E)$ is computed using two terms with bit-by-bit exclusive-OR. The first rotation, $(IDN_S \oplus Y_RS)$, has 161 possible hamming weights, resulting in 33 possible states after rotation. The second rotation, involving the 160-bit value $(Y_{RS})$, also has 161 possible states. Thus, $(S_O)$ is calculated as: 
$$S_O = RROT(S_E \oplus ROT(TI_S,IDN_S \oplus Y_{RS}), Y_{RS})$$ 
with 5313 possible candidates for $(S_O)$, saved in list $L_{S_O}$. 

<img src="https://github.com/nargesmokhtari/ULBRAP-Protocol/assets/126694721/7d69ce19-5281-4baf-89b4-872e66a2f2ce" alt="Step 1" width="500"/>

### Step 5
Assuming the Balance amount as a network value, along with 161 candidates of $IDN_S \oplus IDN_T$ and 5313 candidates of $S_O$ obtained in Steps 3 and 4, respectively, we will have $161 \times 5313$ potential candidates for $TK_{ST}$. Among these candidates, the key satisfying $S_G$ will match the candidate key. Consequently, this step will require $2 \times (161 \times 5313)$ hash calculations.

<img src="https://github.com/nargesmokhtari/ULBRAP-Protocol/assets/126694721/fb5a42e6-67e1-46d2-932f-48cd76ed02a1" alt="Step 1" width="500"/>



