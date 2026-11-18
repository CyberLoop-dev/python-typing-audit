import unittest
from main import audit_source

class TypingAuditTests(unittest.TestCase):
    def test_reports_unannotated_parameters_and_return(self):
        findings=audit_source("def greet(name, age: int):\n    return name\n")
        self.assertEqual([(x["kind"],x["name"]) for x in findings],[("argument","name"),("return","return")])

    def test_ignores_self_and_annotated_functions(self):
        findings=audit_source("class A:\n    def run(self, count: int) -> bool:\n        return True\n")
        self.assertEqual(findings,[])

if __name__=="__main__": unittest.main()
