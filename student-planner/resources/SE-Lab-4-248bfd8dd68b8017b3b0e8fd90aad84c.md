
## Activity Diagram

## By K036 and K005


```mermaid
---
title: Activity Diagram for Bluetooth Social Messaging App
---
flowchart TD
    A([Start]) --> B(User opens app)
    B --> C{Is user authenticated?}
    C -- No --> D[Show login/register screen]
    D --> E[User logs in or signs up]
    E --> F[Load user profile]
    C -- Yes --> F[Load user profile]
    F --> G{Bluetooth ON?}
    G -- No --> H[Prompt to turn on Bluetooth]
    H --> I[User enables Bluetooth]
    I --> J[Scan for nearby users/groups]
    G -- Yes --> J[Scan for nearby users/groups]
    J --> K{What does user want to do?}
    K -- "Send Message" --> L[Select contact or group]
    K -- "Join/Create Group" --> M[Show group options]
    K -- "Broadcast Message" --> N[Compose broadcast]
    K -- "Nearby Discovery" --> O[Show nearby anonymous users]
    L --> P[Compose message]
    P --> Q{Send media/file/location?}
    Q -- No --> R[Send text message]
    R --> S[Deliver message via Bluetooth/mesh]
    Q -- Yes --> T[Attach media, file, or location]
    T --> R
    S --> U{Message delivered?}
    U -- Yes --> V[Show delivery/read receipts]
    U -- No --> W[Retry sending via mesh/store for later]
    M --> X{Create or Join Group?}
    X -- Create --> Y[Create group; invite users]
    X -- Join --> Z[Select/join from available groups]
    Y --> AA[Group chat session]
    Z --> AA
    AA --> AB[User sends/receives group messages]
    N --> AC[Deliver broadcast to all nearby users]
    O --> AD[Start anonymous/interest-based chat]
    AB --> F
    AC --> F
    AD --> F
    V --> F
    W --> F
    F --> AE{Does user log out or exit?}
    AE -- Yes --> AF([End])
    AE -- No --> J
```


## Faculty provided lab document


[EXP-4-ACTIVITY.docx](https://prod-files-secure.s3.us-west-2.amazonaws.com/cb8bfd8d-d68b-81fa-ac15-000328a0aab4/4d3728d2-134d-42d8-8dab-e0f64e2d814d/EXP-4-ACTIVITY.docx?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TZO6TCNG%2F20250815%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250815T064756Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA8aCXVzLXdlc3QtMiJHMEUCIE08FKz6aP79x7zDtlFKbi78spcctlnibg6OFhk1UIoZAiEA2u8wR0YZJEMSHOr0FJyZybcv1yXG4gIu3XhoXol7c0Iq%2FwMIVxAAGgw2Mzc0MjMxODM4MDUiDNEISNSuhp204VtY5ircA7x8BNEm062hnOV2MosCJsWm2tOJQ8UZuZfAMRBnC7kGfHTibZL8sj6LXqoOEMuqZWjNqtHCtoqHXCaA5IFEtQA2jvZiZdrArZKsCCWWu%2Bjb5zTThT%2FM%2FBz9MXysNmkM5qxlWeRT6SRb%2B0AcFCDO3kjkNfmDT8snVGcCBes4GQArvd2rXkAQcttF72w2JU93c9wIP4mQyZ419s0b1%2FiSlvxNrNd0L%2B8Sd4yRicKh0RqVCuTdnf1cct%2FoxPZS7l1j6NMSj3mdRSeMtJr93KTakVy9I5Uq2pAm8a47OMxatFKWGQrXhl6a7qwS5VzyeiNjNoOyjsM7U5fvWK12EZ8HSXQIPg8ezNwkYLa3H2WSEZozF2uKlX7n2gKK1w%2BsYck0k6L3d6RBs39EpqlUVF%2F82IjFfRTVuHRc4Fmih9CsdRq1FZi3o6qn9Mt1dX2mdjprcVY1vUzu994%2Bk%2F7AwvU0F%2BAIBcj%2FpjpHjDQbeeC6Bcdb6Ek12DcF3d%2BUtMrAIwDwsCUu2%2Fa7AIkHsNTe3HNJyI4Sj2%2BPqcCIXGJlXXwE%2BpYdw9Lpfo8szQJLz%2Btf0z1fAXBs4z6NNEqnpuszqsqzEJRxTRY31R15XI6N8pjB8AGmCGw3OR%2BbDY%2FEgGoyMM6i%2B8QGOqUB0CA5LO2fz8BiSpJL5pB94BFW4r3Y7EjiS9GsWxFJkCdUggYAsrGSfyX4nw0Cm1fv2ZwP7wtf83pKN54BzrLBue8lza0PpWFjLiCsNEOgZEFyGw1L7fJ9ab4jMKvWcfoX2f4D7kjXWeE8MBx5%2FkTg6x0Wsj3mdspi190UOJRKpeI%2FJfQqOKQtszdKFta1zKiAX0iH7Mqbg9%2F3GJBOjXwzaexo2WEn&X-Amz-Signature=86643f291fc8b2a99cc6d24f98ad2a7279af247bad2322cf55164f40b10b072a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

