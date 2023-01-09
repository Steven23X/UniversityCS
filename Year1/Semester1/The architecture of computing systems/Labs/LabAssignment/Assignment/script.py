import os
import subprocess

inputArray = [
          ["test1_1.in"]  #in aceasta lista puteti adauga fisiere cu exemple de input pentru cerinta 1
        , ["test2_1.in"]  #in aceasta lista puteti adauga fisiere cu exemple de input pentru cerinta 2
        , ["test3_1.in"]  #in aceasta lista puteti adauga fisiere cu exemple de input pentru cerinta 3
]
outputArray = [
          ["0 1 1 0 0 0 1 1 0 0 0 1 0 0 0 0 "]  #output-ul pentru primul test din lista pentru cerinta 1 (in aceasta lista puteti adauga output-ul pentru testele adaugate de voi)
        , ["2"] #output-ul pentru primul test din lista pentru cerinta 2 (in aceasta lista puteti adauga output-ul pentru testele adaugate de voi)
        , ["2"] #output-ul pentru primul test din lista pentru cerinta 3 (in aceasta lista puteti adauga output-ul pentru testele adaugate de voi)
]
points = [
          [50]
        , [30]
        , [20]
]

firstSource = 0
secondSource = 0
subprocess.call(["rm","-f", "cerinta1_2", "cerinta3"])

for file in os.listdir('.'):
        if os.path.isfile(file) and "_0" in file and ".s" in file:
                        subprocess.call(["gcc", "-m32", file, "-o", "cerinta1_2"])
                        firstSource = 1
        elif os.path.isfile(file) and "_1" in file and ".s" in file:
                        subprocess.call(["gcc", "-m32", file, "-o", "cerinta3"])
                        secondSource = 1

executables = [("./cerinta1_2", firstSource), ("./cerinta1_2", firstSource), ("./cerinta3", secondSource)]

estimatedGrade = 0


for taskIndex in range(len(executables)):
        if executables[taskIndex][1] == 0:
                print("Executable for task " + str(taskIndex + 1) + "not found!")
                continue

        print("Task " + str(taskIndex + 1 ) + ":")

        taskInputArray = inputArray[taskIndex]
        taskOutputArray = outputArray[taskIndex]
        taskPoints = points[taskIndex]

        for i in range(0, len(taskInputArray)):
                try:
                        output = subprocess.check_output(executables[taskIndex][0] + " < " + taskInputArray[i], shell = True, timeout=10).decode("utf-8")
                        output = output.replace("\n", "")
                        if output == taskOutputArray[i]:
                                estimatedGrade += taskPoints[i]
                                print("\tTest " + str(i) + ": OK (" + str(taskPoints[i]) + ")")
                        else:
                                print("\tTest " + str(i) + " failed (0p)")
                                print("\t   Input: ")
                                with open(taskInputArray[i], "r") as f:
                                        lines = f.readlines()
                                        for line in lines:
                                                print(line[:-1])
                                print("\t   Your output:", end =" ")
                                print(output)

                                arr = bytes(output, 'utf-8')
                                print("\t   Your output in bytes:", end =" ")
                                # actual bytes in the the string
                                for byte in arr:
                                        print(byte, end=' ')
                                print("\n")


                                print("\t   Expected output:", end = " ")
                                print(taskOutputArray[i])

                                arr = bytes(taskOutputArray[i], 'utf-8')
                                print("\t   Expected output in bytes:", end =" ")
                                # actual bytes in the the string
                                for byte in arr:
                                        print(byte, end=' ')
                except:
                        print("\tTest " + str(i) + ": exception! (0p)")
        print("\n")

print("Estimated grade %dp / 100" % (estimatedGrade))