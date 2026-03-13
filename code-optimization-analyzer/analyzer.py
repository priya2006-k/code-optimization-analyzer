import os
import re

# folder containing C programs
folder = "sample_programs"

print("=================================")
print("      Code Optimization Analyzer")
print("=================================\n")

# counters for summary
total_files = 0
unused_variables = 0
dead_code_count = 0
loop_count = 0

# go through each file in the folder
for file in os.listdir(folder):

    if file.endswith(".c"):

        total_files += 1

        print("Analyzing:", file)

        path = os.path.join(folder, file)

        with open(path, "r") as f:
            code = f.read()

        issue_found = False

        # 1️⃣ Detect variables
        variables = re.findall(r'int\s+(\w+)', code)

        for var in variables:
            if code.count(var) == 1:
                print("  Warning: unused variable ->", var)
                unused_variables += 1
                issue_found = True

        # 2️⃣ Detect dead code
        if "return" in code:
            after_return = code.split("return")[1]

            if "printf" in after_return:
                print("  Dead code detected after return statement")
                dead_code_count += 1
                issue_found = True

        # 3️⃣ Detect loops
        loops = re.findall(r'for\s*\(', code)

        if loops:
            print("  Loop detected (possible optimization)")
            loop_count += 1
            issue_found = True

        if not issue_found:
            print("  No issues detected")

        print()

# final summary
print("=================================")
print("Analysis Summary")
print("=================================")

print("Files analyzed:", total_files)
print("Unused variables detected:", unused_variables)
print("Dead code blocks:", dead_code_count)
print("Loops detected:", loop_count)

print("\nAnalysis complete.")