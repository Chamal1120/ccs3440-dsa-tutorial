class EmployeeDirectory:
    """Employee directory with multiple search indices."""

    def __init__(self):
        self.by_id = {}  # Primary index
        self.by_department = {}  # Department index
        self.by_salary_range = {}  # Salary range index

    def add_employee(self, emp_id, name, department, salary):
        """Add employee with multiple indices."""
        # Create employee record
        employee = {
            "id": emp_id,
            "name": name,
            "department": department,
            "salary": salary,
        }
        # Add to primary index
        self.by_id[emp_id] = employee

        # Add to department index
        if department not in self.by_department:
            self.by_department[department] = []
        self.by_department[department].append(employee)

        # Add to salary range index
        salary_range = (salary // 10000) * 10000  # Group by salary ranges of 10,000
        if salary_range not in self.by_salary_range:
            self.by_salary_range[salary_range] = []
        self.by_salary_range[salary_range].append(employee)

    def find_by_id(self, emp_id):
        """O(1) lookup by ID."""
        return self.by_id.get(emp_id)

    def find_by_department(self, department):
        """O(1) lookup by department."""
        return self.by_department.get(department, [])

    def find_by_salary_range(self, min_salary, max_salary):
        """Find employees within a specified salary range."""
        results = []
        for range_start in self.by_salary_range:
            if min_salary <= range_start <= max_salary:
                results.extend(self.by_salary_range[range_start])
        return results


# Example Usage
def demonstrate_employee_directory():
    print("\n=== Employee Directory Example ===")
    directory = EmployeeDirectory()

    # Add sample employees
    employees = [
        ("E001", "John Doe", "IT", 75000),
        ("E002", "Jane Smith", "HR", 65000),
        ("E003", "Bob Wilson", "IT", 80000),
        ("E004", "Alice Brown", "Finance", 70000),
    ]

    for emp_id, name, dept, salary in employees:
        directory.add_employee(emp_id, name, dept, salary)
        print(f"Added: {name} ({dept})")

    # Demonstrate different search methods
    print("\nSearching by ID (E003):")
    emp = directory.find_by_id("E003")
    if emp:
        print(f"Found: {emp['name']} - {emp['department']}")
    else:
        print("Employee not found.")

    print("\nIT Department employees:")
    it_emps = directory.find_by_department("IT")
    for emp in it_emps:
        print(f"{emp['name']} - ${emp['salary']}")

    print("\nEmployees with salary 70000-80000:")
    salary_range = directory.find_by_salary_range(70000, 80000)
    for emp in salary_range:
        print(f"{emp['name']} - ${emp['salary']}")


# Run the example
demonstrate_employee_directory()
