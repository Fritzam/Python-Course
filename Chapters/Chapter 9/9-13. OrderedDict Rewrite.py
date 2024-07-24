from collections import OrderedDict
glossary = OrderedDict()
glossary['dictionary'] = "Useful data structure"
glossary['loop'] = 'Helps You do the same thing multiple times'
glossary['conditionals'] = 'Allow you to create logic in Your program'
glossary['enumerate'] = "Allows You to loop by index"
glossary['rm -rf /'] = "Will brick Your system"

for key, value in glossary.items():
    print(key + ": " + value)