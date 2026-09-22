print("Payment processed successfully")
print("Payment failed. Please try again.")


try:
    amount = float(input("Enter the payment amount: "))
    if amount <= 0:
        raise ValueError("Amount must be greater than zero.")
    print(f"Payment of ${amount:.2f} processed successfully.")
except ValueError as ve:
    print(f"Invalid input: {ve}")
except Exception as e:
    print(f"An error occurred: {e}")