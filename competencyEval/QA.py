from AutoQA.compromise import Compromise


class QA:
    def __init__(self):
        self._q = None
        self._a = None

    @property
    def q(self):
        return self._q

    @q.setter
    def q(self,question):
        self._q = question

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, question):
        self._a = question


class SetOfQA:

    def q_and_a():
        listQA = []
        compromise = Compromise()
        a_array = compromise.aArry()
        q_array = compromise.qArry()
        count = 0
        for ques in q_array:
            qa = QA()
            qa.a = a_array[count]
            qa.q = q_array[count]
            listQA.append(qa)
            count +=1
        return listQA


def main():
    list = SetOfQA.q_and_a()
    var = list[3].q
    print(var)
if __name__ == '__main__':
    main()

