import random
import string

def get_password_length():
    """Phase 1: Input & Data Validation"""
    while True:
        try:
            user_input = input("Enter desired password length (Minimum 8, Recommended 15+): ")
            length = int(user_input)
            
            
            if length < 8:
                print("❌ Security warning: Length must be at least 8 characters.")
                continue
            if length > 64:
                print("❌ Systems must support up to 64 characters, please choose a value <= 64.")
                continue
                
            return length
        except ValueError:
            print("❌ Invalid input! Please enter a valid target integer.")

def generate_secure_password(length):
    """Phase 2: Backend Transformation Engine"""
    
    character_pool = string.ascii_letters + string.digits

    password = "".join(random.choice(character_pool) for _ in range(length))
    return password

def main():
    print("--- Random Password Generator ---")
    
    
    password_length = get_password_length()
    
    
    secure_password = generate_secure_password(password_length)
    
    
    print("\n--- Generated Provision ---")
    print(f"Your Secure Password: {secure_password}")
    print("----------------------------")

if __name__ == "__main__":
    main()