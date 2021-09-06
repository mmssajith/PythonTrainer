"""
An insurance company has decided to change data format
"""
# Import Package to identify data to be replaced by the program
import re

# Define a function 

def change_format(paragraph):
  return re.sub(r'(\d+)-(\d+)-(\d+)', r'\3/\1/\2', paragraph)
"""
  pairs = {}
  for policyNo in re.findall(r'\d{3}-\d{2}-\d{4}', paragraph):
    # IDentify the parts of the policy number
    firstPart = policyNo[0:3]
    secondPart = policyNo[4:6]
    thirdPart = policyNo[7:11]

    # Prepare for new policy Number
    newPolicyNumber = firstPart + '/' + thirdPart + '/' + secondPart

    # keep the pairs
    pairs[policyNo] = newPolicyNumber

  for key, value in pairs.items():
    #substitute
    paragraph = re.sub(key, value, paragraph)

  return paragraph
"""
print(change_format('Please type your policy number: 112-39-5698'))
print(change_format('Please type your policy number: 112-39-5698 , 558-69-8951'))


