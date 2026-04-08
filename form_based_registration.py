#!/usr/bin/env python3
"""
Form-Based User Registration with Validation
Features: Email validation, Password strength check, Save to file
"""

import re
import json
from datetime import datetime

def validate_email(email):
    """Validate email format"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validate_password(password):
    """Validate password - must be at least 8 characters"""
    if len(password) < 8:
        return False, "Password must be at least 8 characters long."
    return True, "Password is valid."

def save_registration(data, filename="registrations.txt"):
    """Save registration details to a file"""
    try:
        with open(filename, "a") as file:
            file.write("=" * 50 + "\n")
            file.write(f"Registration Date: {data['timestamp']}\n")
            file.write(f"Name: {data['name']}\n")
            file.write(f"Email: {data['email']}\n")
            file.write(f"Age: {data['age']}\n")
            file.write("=" * 50 + "\n\n")
        return True
    except Exception as e:
        print(f"Error saving to file: {e}")
        return False

def form_based_registration():
    print("=" * 50)
    print("--- User Registration Form ---")
    print("=" * 50)
    
    # Name input
    name = input("Enter your name: ").strip()
    while not name:
        print("Name cannot be empty.")
        name = input("Enter your name: ").strip()
    
    # Email input with validation
    while True:
        email = input("Enter your email: ").strip()
        if validate_email(email):
            break
        else:
            print("Invalid email format. Please enter a valid email (e.g., user@example.com)")
    
    # Password input with validation
    while True:
        password = input("Enter your password: ").strip()
        is_valid, message = validate_password(password)
        if is_valid:
            break
        else:
            print(f"Invalid password: {message}")
    
    # Age input with validation
    while True:
        age = input("Enter your age: ").strip()
        try:
            age_int = int(age)
            if age_int < 0 or age_int > 150:
                print("Please enter a valid age.")
            else:
                break
        except ValueError:
            print("Please enter a valid number for age.")
    
    # Display registration details
    print("\n" + "=" * 50)
    print("--- Registration Details ---")
    print("=" * 50)
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Password: {'*' * len(password)}")
    print(f"Age: {age}")
    print("=" * 50)
    
    # Save to file
    registration_data = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "name": name,
        "email": email,
        "age": age
    }
    
    if save_registration(registration_data):
        print("\n✓ Registration successful!")
        print("✓ Details saved to 'registrations.txt'")
    else:
        print("\n✓ Registration successful!")
        print("✗ Failed to save to file.")

if __name__ == "__main__":
    form_based_registration()
