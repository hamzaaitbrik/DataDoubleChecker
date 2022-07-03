print('----------------------------------------------- DataDoubleChecker')
print('----------------------------------------------- Discord: Ozym1ndias#3112\n')

_Data = []
__Data = []




def txt2list():
    with open('Data.txt', 'r') as Data:
        for line in Data.readlines():
            _Data.append(line.replace('\n', ''))
        #print(_Data)
        print(f'The length of the raw data is: {len(_Data)}') # Check for the length of the list

def removedoubles(_Data):
    __Data = list(set(_Data))
    #print(__Data)
    print(f'The length of the unique data is: {len(__Data)}') # Check for the length of the unique list
    return __Data

def write2txtfile(__Data):
    #print(len(__Data))
    #print('This works!')
    with open('uData.txt', 'w') as uData:
        for number in __Data:
            uData.write(number)
            uData.write('\n')

def main():
    txt2list()
    __Data = removedoubles(_Data)
    write2txtfile(__Data)



if __name__ == '__main__':
    main()
