import demographic_data_analyzer
from unittest import main

# Run the demographic data analyzer
print("Demographic Data Analyzer Output:\n")
demographic_data_analyzer.calculate_demographic_data(print_data=True)

print("\n" + "="*50 + "\n")

# Run unit tests if test_module.py is available
print("Running unit tests...")
try:
    import test_module
    main(module='test_module', exit=False, verbosity=2)
except ImportError:
    print("test_module.py not found - skipping unit tests")