Here we present a real example of the attack. First, we will initialize some variables named IDs of nodes and blockchain values.

- $IDN_T$: 0x430100cb10621711dadc0cdb8f62fa99c64c3bf6.
    
- $IDN_R$: 0x9f9911b71d090377cc6a25a9a9eda37672adb90a.
    
- $IDN_S$: 0x5aa7e639d5b086425e55e7de7129e43835f43aea.
    
- $Bal_N$: 0xefec6fbf7ce8a5fe56864fde510d67aebccc40e4.

- $B_S$: 0x458f8407a027da7e05961d76bd905574806d856c.

As outlined in the ULBRAP protocol, five messages are exchanged between nodes (Reader, Tag, and Supply Chain). However, only four of these messages are needed to recover the session key ($TK_{ST}$). Using the values mentioned above and following the ULBRAP protocol, we generate the following messages:

$MESG1$: From Reader to Tag.
- $P_R$: 0xbb5da7ee364a11cc7c8658e835f72883268a0820.
- $CH_R$: 0xe0582a582ec916a24c4afea237cOd3ff72693438.
- $TI_R$: 0xafd62668.

$ MESG2$: From Tag to Reader.
- $CH_T$: 0x133e3a1be92825fd89cad9312e059544d325e079.
- $Aut_R$: 0x18196f1ab4171d389355b3f67345fb62e1697069.
- $P_T$: 0x2195b51083eaa5828251a29f8c988ed237a0dadd.
- $TI_T$: 0xc058957f.

$MESG3$: From Reader to Supply Chain.
- $P_P$: 0xf737cf4fd247d1634b8ec22e29c69434df7fdaf1.
- $P_Q$: 0x92ef8cd46453a908e263b46bdd13e2ffe28f6fff.-
- $Reader_{check}$: 0x47ef6a1ab807db583bba440624b33b853e249cf6.
- $TI_R^{\prime}$: 0x2e94e020.

$MESG4$: From Supply Chain to Reader.
- $S_E$: 0x4085257b1e47c646afbea11fd09e548f0da67e27.
- $S_F$: 0x94085257b1e47c646afbea11fd09e548a0233f0c.
- $S_G$: 0x7e6f93be8990ebcc1c8e790a6ad6bb3b5daf4f52.
- $TI_S$: 0x55a36e0e.

With these values, session key will be:
- $TK_{ST}$: 0xb31d7ad0f4ab796e3264ea208b79c2950e15af8d.

Based on the [Algorithm](Algorithm.md) descriptions, it can be recovered in reasonable amount of time.

The video of detailing the process is available in the [video](/README.md#video) section. Please note that some values in the video are presented in binary format.