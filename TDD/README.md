# Run the test module by name
python -m unittest tests.test_bank_account

# Run a TestCase class by name
python -m unittest tests.test_bank_account.BankAccountTestCase

# Discover and run all unit tests in a project
python -m unittest discover

# Write XML test report using unittest-xml-reporting
# Requires the appropriate "main" logic
python -m tests.test_bank_account
