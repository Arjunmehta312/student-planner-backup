
## Feature Selection Methods


### Filter Method

- Selected on basis of statistical measures
- Dropped on basis on relation to the output
- Check correlation to find out if positively or negatively correlated
- Low computational time and avoids overfitting
- Some common techniques:
	- Information Gain: Variable with high IG are retained
	- Chi square test: Best Chi square value is selected
	- Fisher’s score method: The rank of the variable , larger fishers score is selected

### Wrapper Method

- Search problem
- Different combinations are made, evaluated and compared with different combinations
- Some techniques:
	- Forward selection:
		- Begins with empty set
		- After each iteration, keeps adding and keeps evaluating also
		- Until additions of new variable does not improve performance
	- Backward selection:
		- Starts with considering all features and removes least significant features
		- Starts with considering all features and removes least significant features
		- Continues removing until performance stops improving
	- Exhaustive feature selection:
		- Best feature selections method, evaluates each feature set as a brute force
		- It tries and makes each possible

### Embedded Method

- Takes advantage of both filter and wrapper methods.

## Dimensionality Reduction

- Columns are dimension
- More the features greater is the difficulty of making the model. This is the Curse of Dimensionality.
1. Performed before modelling
2. Might be performed after data cleaning and scaling
3. Reduction done on training data, same reduction to be done on test data or validation data and other data that gets used in the whole process.
4. Process is basically converting high dimension data to low dimension data

### Techniques for DR


![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/cb8bfd8d-d68b-81fa-ac15-000328a0aab4/97b11d8d-330c-4aad-9215-1c847798f6ab/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XPIIULUM%2F20250815%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250815T064757Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA8aCXVzLXdlc3QtMiJGMEQCIHjWZoEbYYHFzDCn0AIHt3fIOsQu3CG2DCO%2BFN5ZKVr2AiBHM0FUuShoQD5a12l1G6Cmw1qDwwrqKTHi8au80WCXQCr%2FAwhXEAAaDDYzNzQyMzE4MzgwNSIM6yk2yI2hIw9T8z2lKtwDwJ4MZ6N45wQleGFeoM%2FcAL9FgWrhqFF3Qg0Dyq6SVxQFhsaWNPMWgaBHmUsRiUh%2BefD59JtpMcjmhjtabDPG8PKXbE5eRlvDDPaRqDsHT4blGSkMGkKy4rt%2BOzgUn3dxckSAcPWrUUYBRjE2rruCzMRWG0bcnyHHhmjdlX1oAKtAGjuIoPMBY6OUcLRCegb%2Bb0mRgKn8P41BmAWvoEUt2H1E6i3JsLUFG%2FsjKIabmIdTd4o6eKNpFrwCQH4vZC89Sm5EpC%2Frt9hYafoFHexUPmAw8SE1IMBcl4mZ7y9YG%2FYyi2D92EPL2AddOsWQ3JxCnRFjqStsMrGpnGtJDKZcB5FRBpsYVRYw0MUdXdh0dTZvkBpzMr208BPOB8U%2FhPxfJSYVYZSzOqNlfA5JoBBPICajbQ%2FUAbTvENxhd63kEEu2udPzUQcr2l4kdxQhHxUwW1jCx6OnQchERgpvhH%2F%2BuPpqimdvR4deqyio%2Fo%2Bbl3eFW6x6hL1cZ7OCUgUoqcn79syiotXYq2V6ZKwOjvyKnfiXBmHEQCxggahKOmaMe3HkA6QseKVY1jKlZndxL1KlKCA8fK7sV%2FAvzioOKevGbm7dxWExAdgZTcFXW2QmagSDJIsGONSxph%2BGPm4w0qL7xAY6pgG%2B1mxa13Kk8GatlFMF98tv7VobprKE0O%2BAexBOq0oKFy0gpaC0zXoGkLdG0xu9In1FIM9EkOjFFp2gGzQ2y7trgAN%2B31kH9CIaaT9XIK4srZtYF%2BWpPizEvR7Tf4R5RwfHgEyi%2BASnJbI6ik7L%2Btj0msMzp0VG9lZ0Oll2czYfC205PjupW5QYQljFE8fTCMDpztIXJYTMrcrnGH7asrQeDVbKeMfW&X-Amz-Signature=1e6b3861f57d4ece6db2f0a1dce019ff7d9584dc922acb5d7c7f323e53ca09e0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

