import numpy as np

# Simulated coin toss data (1 for heads, 0 for tails)
data = np.array([1, 0, 1, 1, 1, 0, 0, 1, 0, 1])

# Number of iterations
num_iterations = 10

# Initial parameter estimates
initial_prob_heads = 0.6  # Initial probability of getting heads
initial_prob_tails = 1 - initial_prob_heads

for iteration in range(num_iterations):
    print(f"Iteration {iteration + 1}:")

    # Expectation (E-step): Calculate the expected number of heads and tails
    expected_heads = np.sum(data * initial_prob_heads)  # E[Heads]
    expected_tails = np.sum((1 - data) * initial_prob_tails)  # E[Tails]

    # Maximization (M-step): Update the parameter estimates
    total_tosses = len(data)
    updated_prob_heads = expected_heads / total_tosses  # M[Heads]
    updated_prob_tails = expected_tails / total_tosses  # M[Tails]

    # Print the updated parameters
    print(f"Updated Probability of Heads: {updated_prob_heads:.3f}")
    print(f"Updated Probability of Tails: {updated_prob_tails:.3f}")

    # Update the initial parameter estimates for the next iteration
    initial_prob_heads = updated_prob_heads
    initial_prob_tails = updated_prob_tails

# Final parameter estimates
print("\nFinal Parameter Estimates:")
print(f"Probability of Heads: {updated_prob_heads:.3f}")
print(f"Probability of Tails: {updated_prob_tails:.3f}")
