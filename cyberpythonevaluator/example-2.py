from cyberpythonevaluator import CyberPythonEvaluator

cpe = CyberPythonEvaluator()

challenge = cpe.get_challenge(2)

print "Description", challenge.description
print "Example Input", challenge.example_input
print "Example Output", challenge.example_output

def solution (number, group) :
    group = '10201'
    if number in group:
        number % 2 == 0
        print true
    else:
        print false


#print challenge.validate(solution, debug=True)
print challenge.validate(solution, debug=True)