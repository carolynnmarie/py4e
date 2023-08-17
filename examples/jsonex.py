import json

def exampleDictionaries():
    data = '''
    {
        "name" : "Chuck",
        "phone" : {
            "type" : "intl",
            "number" : "+1 734 303 4456"
        },
        "email" : {
            "hide" : "yes" "
        }
    }'''

    info = json.loads(data)
    print('Name:', info["name"])
    print('Hide:', info["email"]["hide"])

def exampleList():
    input = '''
    [
        {"id" : "001",
        "x" : "2",
        "name" : "Chuck"
        },
        {"id" : "009",
        "x" : "7",
        "name" : "Charlie"
        }
    ]'''

    info = json.loads(input)
    print('User count:', len(info))
    for item in info:
        print('Attribute', item['x'])