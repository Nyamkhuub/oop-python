#Outline:
#1. File unshaad List butsaadag class
#2. List ~ QuestionAnswer/Class/ 
#3. Play
class ReadFile():
    def __init__(self, fileName):
        self.fileName = fileName
    def getList(self):
        myFile = open(self.fileName, 'r')
        fullText = myFile.read()
        fullText = fullText[:-1]
        allData = fullText.split('\n')
        #question answer split(',') object/QuesAns/ -> list 
        questions = []
        for data in allData:
           #Undsen gurvan ogno yu ve?,rgb 
           quesAndAns = data.split(',')
           #QuestAns object uusgeed teriigee questions list append hiij bna
           questions.append(QuestAns(quesAndAns[0], quesAndAns[1]))
        return questions
class QuestAns():
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

class Play():
    def __init__(self):
        self.counter = 0
        self.mustPoint = 0
    def getStarted(self):
        test = ReadFile('ques.txt')
        test = test.getList()
        self.mustPoint = len(test)
        for data in test:
            print(data.question)
            answer = input('Tanii hariult?')
            if data.answer == answer:
                print('Bayar hurgye ta zov hariulla!')
                self.counter = self.counter + 1
            else:
                print('Uuchlaarai hariult buruu baina!')
        if self.counter == self.mustPoint:
            print('Bayar hurgye ta buh asuultand zow hariulla!')
        else:
            print('Ta', self.mustPoint, 'asuultnaas', self.counter, 'asuultand zow hariullaa!')

gameTest = Play()
gameTest.getStarted()
