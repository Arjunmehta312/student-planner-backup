
## Public Key Cryptosystem


```mermaid
sequenceDiagram
    participant Alice as Alice (Sender)
    participant Bob as Bob (Receiver)
    
    Note over Alice: Has private key (kR_A) and public key (kU_A)
    Note over Bob: Has Alice's public key (kU_A)
    
    Alice->>Alice: 1. Create message M
    Alice->>Alice: 2. Generate digital signature<br/>S = signing_algorithm(M, kR_A)
    Alice->>Bob: 3. Send message and signature (M, S)
    
    Bob->>Bob: 4. Apply verification algorithm<br/>verification_algorithm(M, S, kU_A)
    
    alt Signature Valid
        Note over Bob: Output: Valid - Message is from Alice<br/>and has not been modified
    else Signature Invalid
        Note over Bob: Output: Invalid - Message may be<br/>forged or modified in transit
    end
```


---


## Access Control

- InfoSec process which enables organizations to manage who is authorized to access data and resources

```mermaid
graph TD;
    Alice["Alice (Admin)"] --> |"Grants Access"| Bob["Bob (User)"];
    Database["Resources"] --> |"Accessible by"| Alice;
    Database --> |"Limited Access"| Bob;
```


---


## To achieve data integrity (example of violation)


```mermaid
sequenceDiagram
    participant Alice as Alice
    participant Oscar as Oscar (Hacker)
    participant Bob as Bob
    
    Note over Alice: Creates message M
    Note over Alice: Calculates checksum C(M)
    Alice->>Oscar: Sends M and C(M)
    Note over Oscar: Intercepts message
    Note over Oscar: Attempts to modify M to M'
    Oscar->>Bob: Forwards modified M' and original C(M)
    Note over Bob: Calculates checksum C(M')
    Note over Bob: Compares C(M') with received C(M)
    Note over Bob: C(M') ≠ C(M), integrity violation detected
```


---


## Traffic Padding

- Insert some bogus data into traffic data
- Avoids traffic analysis attack

---


## Routing Control

- Selecting and continuously changing available routes between sender and receiver
- Prevents eavesdropping

---


## Authentication Exchange

- Entities exchange some message to prove identity to each other
- **Nonce: A time varying-random number with one-time-usage**

---


## Notarization

- The use of a trusted third-party to assure certain properties of a data exchange

```mermaid
sequenceDiagram
    participant Alice as Alice (Sender)
    participant TTP as Trusted Third Party
    participant Bob as Bob (Receiver)
    
    Alice->>TTP: 1. Sends message with request for delivery proof
    TTP->>Bob: 2. Forwards message to Bob
    Bob->>TTP: 3. Acknowledges receipt (origin proof)
    TTP->>Alice: 4. Sends delivery proof to Alice
    TTP->>Bob: 5. Sends origin proof to Bob
    
    Note over Alice,Bob: Alice has proof Bob received the message
    Note over Bob,Alice: Bob has proof message came from Alice
```


---


## Pervasive Security Mechanisms


Mechanisms not specific to an particular OSI service or similar protocol layers

- Trusted Functionality
	- Example: As established by a security policy
- Security Label
	- Marking bound to a resource (may be a data unit)
- Event Detection
	- Detection of security relevant events
- Security Audit Trail
- Security Recovery

---

