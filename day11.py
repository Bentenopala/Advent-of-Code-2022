
def parse(data):
    mky, tdict, test_prod = dict(), dict(), 1
    for i in range(len(data)):
        mdata = data[i].split('\n')
        mid = f"m{i}"
        mky[mid] = dict()
        for j in range(len(mdata)):
            if mdata[j].startswith('  Starting'):
                items = mdata[j][18:].split(', ')
                mky[mid]['items'] = []
                for worry in items:
                    mky[mid]['items'].append(int(worry))
            elif mdata[j].startswith('  Operation'):
                if mdata[j][23:24] == '*' and mdata[j][25:] == 'old':
                    mky[mid]['opion'] = '**'
                    mky[mid]['opand'] = 2
                else: 
                    mky[mid]['opion'] = mdata[j][23:24]
                    mky[mid]['opand'] = int(mdata[j][25:])
            elif mdata[j].startswith('  Test'):
                mky[mid]['testn'] = int(mdata[j][21:])
                tdict[mid] = int(mdata[j][21:])
                test_prod *= int(mdata[j][21:])
            elif mdata[j].startswith('    If true'):
                mky[mid]['mtrue'] = 'm' + mdata[j][29:]
            elif mdata[j].startswith('    If false'):
                mky[mid]['mfalse'] = 'm' + mdata[j][30:]
    tdict['prod'] = test_prod
    return mky, tdict

def monkey_moves(data, rounds, part):
    r, p = rounds, part
    mky, testns = parse(data)
    monkeys = list(mky.keys())
    inspection = {key:0 for key in mky.keys()}
    testprod = testns.get('prod')
    for i in range(r):
        for m in monkeys:
            while len(mky[m].get('items')) > 0:
                worry = mky[m].get('items')[0]
                # calculate new worry and update on dictionary
                match mky[m]['opion']:
                    case '+':
                        new = worry+mky[m]['opand']
                    case '*':
                        new = worry*mky[m]['opand']
                    case '**':
                        new = worry**mky[m]['opand']
                if p == 1:
                    new_worry = new//3
                else:
                    new_worry = new % testprod
                # Test and throw
                if new_worry % mky[m]['testn'] == 0:
                    mky[mky[m]['mtrue']]['items'].append(new_worry)
                else:
                    mky[mky[m]['mfalse']]['items'].append(new_worry)
                # update number of inspections
                inspection[m] += 1
                # Erase item from monkey item list
                mky[m].get('items').pop(0)
    return inspection


def monkey_business(inspection_dict):
    insp_d = inspection_dict
    top_two = sorted(insp_d, key=insp_d.get, reverse=True)[:2]
    return insp_d.get(top_two[0])*insp_d.get(top_two[1])


with open("day11.txt", "rt") as myfile:
    data = myfile.read().strip().split('\n\n')

    print(monkey_business(monkey_moves(data,20,1)))
    print(monkey_business(monkey_moves(data,10000,2)))
    #p1: 110264
    #p2: 23612457316
