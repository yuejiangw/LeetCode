"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""
from typing import List

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        employee_map = {employee.id: employee for employee in employees}

        def helper(idx):
            employee = employee_map[idx]
            total = employee.importance + sum(helper(subIdx) for subIdx in employee.subordinates)
            return total
        
        return helper(id)
