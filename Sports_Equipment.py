'''Sports Equipment Rental System POC
*CRUD: Equipment rental records.'
*rent_sports_equipment(equipment id):
Manage rentals of sports equipment to students.
*track_equipment_return(return_id):
Track returns and condition of rented equipment.'''


import os

class SportsEquipmentRentalSystem:
    def __init__(self, equipment_file='equipment_records.txt', rental_file='rental_records.txt'):
        self.equipment_file = equipment_file
        self.rental_file = rental_file
        self.equipment_records = self.load_records(self.equipment_file)
        self.rental_records = self.load_records(self.rental_file)
        self.next_equipment_id = max(self.equipment_records.keys(), default=0) + 1
        self.next_rental_id = max(self.rental_records.keys(), default=0) + 1

    def load_records(self, filename):
        records = {}
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                for line in file:
                    parts = line.strip().split(',')
                    id = int(parts[0])
                    if 'equipment' in filename:
                        records[id] = {
                            'name': parts[1],
                            'condition': parts[2],
                            'is_rented': parts[3] == 'True'
                        }
                    elif 'rental' in filename:
                        records[id] = {
                            'equipment_id': int(parts[1]),
                            'student_name': parts[2],
                            'rental_status': parts[3],
                            'return_condition': parts[4] if len(parts) > 4 else None
                        }
        return records

    def save_records(self, filename, records):
        with open(filename, 'w') as file:
            for id, data in records.items():
                if 'equipment' in filename:
                    file.write(f"{id},{data['name']},{data['condition']},{data['is_rented']}\n")
                elif 'rental' in filename:
                    return_condition = data['return_condition'] if data['return_condition'] else ''
                    file.write(f"{id},{data['equipment_id']},{data['student_name']},{data['rental_status']},{return_condition}\n")

    def create_equipment(self, name, condition):
        equipment_id = self.next_equipment_id
        self.equipment_records[equipment_id] = {
            'name': name,
            'condition': condition,
            'is_rented': False
        }
        self.next_equipment_id += 1
        self.save_records(self.equipment_file, self.equipment_records)
        return equipment_id

    def read_equipment(self, equipment_id):
        return self.equipment_records.get(equipment_id, "Equipment not found")

    def update_equipment(self, equipment_id, name=None, condition=None):
        if equipment_id in self.equipment_records:
            if name:
                self.equipment_records[equipment_id]['name'] = name
            if condition:
                self.equipment_records[equipment_id]['condition'] = condition
            self.save_records(self.equipment_file, self.equipment_records)
            return True
        return False

    def delete_equipment(self, equipment_id):
        if equipment_id in self.equipment_records:
            del self.equipment_records[equipment_id]
            self.save_records(self.equipment_file, self.equipment_records)
            return True
        return False

    def rent_sports_equipment(self, equipment_id, student_name):
        if equipment_id in self.equipment_records and not self.equipment_records[equipment_id]['is_rented']:
            rental_id = self.next_rental_id
            self.rental_records[rental_id] = {
                'equipment_id': equipment_id,
                'student_name': student_name,
                'rental_status': 'rented',
                'return_condition': None
            }
            self.equipment_records[equipment_id]['is_rented'] = True
            self.next_rental_id += 1
            self.save_records(self.equipment_file, self.equipment_records)
            self.save_records(self.rental_file, self.rental_records)
            return rental_id
        return "Equipment not available for rent"

    def track_equipment_return(self, rental_id, return_condition):
        if rental_id in self.rental_records and self.rental_records[rental_id]['rental_status'] == 'rented':
            equipment_id = self.rental_records[rental_id]['equipment_id']
            self.equipment_records[equipment_id]['condition'] = return_condition
            self.equipment_records[equipment_id]['is_rented'] = False
            self.rental_records[rental_id]['rental_status'] = 'returned'
            self.rental_records[rental_id]['return_condition'] = return_condition
            self.save_records(self.equipment_file, self.equipment_records)
            self.save_records(self.rental_file, self.rental_records)
            return True
        return False

def main():
    system = SportsEquipmentRentalSystem()
    while True:
        print("\nSports Equipment Rental System")
        print("1. Create Equipment")
        print("2. Read Equipment")
        print("3. Update Equipment")
        print("4. Delete Equipment")
        print("5. Rent Equipment")
        print("6. Return Equipment")
        print("7. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            name = input("Enter equipment name: ")
            condition = input("Enter equipment condition: ")
            equipment_id = system.create_equipment(name, condition)
            print(f"Equipment created with ID: {equipment_id}")
        
        elif choice == '2':
            equipment_id = int(input("Enter equipment ID: "))
            print(system.read_equipment(equipment_id))
        
        elif choice == '3':
            equipment_id = int(input("Enter equipment ID: "))
            name = input("Enter new equipment name (leave blank to skip): ")
            condition = input("Enter new equipment condition (leave blank to skip): ")
            updated = system.update_equipment(equipment_id, name if name else None, condition if condition else None)
            print("Equipment updated" if updated else "Equipment not found")
        
        elif choice == '4':
            equipment_id = int(input("Enter equipment ID: "))
            deleted = system.delete_equipment(equipment_id)
            print("Equipment deleted" if deleted else "Equipment not found")
        
        elif choice == '5':
            equipment_id = int(input("Enter equipment ID: "))
            student_name = input("Enter student name: ")
            rental_id = system.rent_sports_equipment(equipment_id, student_name)
            print(f"Rental ID: {rental_id}" if isinstance(rental_id, int) else rental_id)
        
        elif choice == '6':
            rental_id = int(input("Enter rental ID: "))
            return_condition = input("Enter return condition: ")
            returned = system.track_equipment_return(rental_id, return_condition)
            print("Equipment returned" if returned else "Rental not found or already returned")
        
        elif choice == '7':
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
