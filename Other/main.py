from tests import test_cases
from linear_search import locate_num

for test in test_cases:
    print(f"Numbers:{test['input']['numbers']}")
    print(f"Query:{test['input']['query']}")
    print("output:",locate_num(**test['input']))    #multiple dictioanry values as argument , use **

    if(locate_num(**test['input'])==test['output']):
        print("This Test run sucessfully")
    else:
        temp=locate_num(**test['input'])
        print("Your output={},Test_output={}".format(temp, test['output']))


