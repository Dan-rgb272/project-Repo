# Your data
data <- c(100,126,130,131,131,132,133,137,138,139,140,140,141,142,142,142,142,145,147,149,151,153,153,153,155,156,158,158,165,191,200)

# Calculate Q1
q1 <- quantile(data, 0.25)

# Display the result using cat
cat("First Quartile (Q1) =", q1, "\n")
