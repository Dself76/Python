import csv

def collect_data():
    data = []
    
    while True:
        name = input("Enter name (or 'q' to quit): ")
        
        if name == 'q':
            break
        
        age = input("Enter age: ")
        email = input("Enter email: ")
        
        # Create a dictionary to store the data
        person = {
            'Name': name,
            'Age': age,
            'Email': email
        }
        
        data.append(person)
    
    return data

def save_data(data, filename):
    keys = data[0].keys()
    
    with open(filename, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)
    
    print(f"Data saved to {filename}.")

if __name__ == '__main__':
    filename = 'data.csv'
    data = collect_data()
    save_data(data, filename)
