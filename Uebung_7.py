from queue import Queue, LifoQueue

class Uebung:

    def FIFO(self):
        # FIFO Queue
        q1 = Queue()
        q1.put(10)
        print(q1)

        q2 = Queue(maxsize=5)
        q2.put(1)
        q2.put(2)
        q2.put(3)
        q2.put(4)
        q2.put(5)
        print(q2.full())
        return q1

        item = q2.get()
        print(item)

        while not q2.empty():
            print(f"The value is", q2.get())

    @staticmethod
    def LIFO():
        stack = LifoQueue()
        stack.put(1)
        stack.put(2)
        stack.put(3)
        #ggf anpassen für werte
        return stack

        print(stack.get())
        print(stack.get())
        print(stack.get())
        print(stack.empty())

    @staticmethod
    def q_4_erstellen():
        q4 = Queue()
        q4.put(11)
        q4.put(5)
        q4.put(4)
        q4.put(21)
        q4.put(3)
        q4.put(10)
        return q4

    def revers_queue(self, qsrc, qdest, zaehler_laenge):
        if not qsrc.empty():
            zaehler_laenge.append(qsrc.qsize())
            buffer = qsrc.get()
            self.revers_queue(qsrc, qdest, zaehler_laenge)
            qdest.put(buffer)
            #print(qdest.qsize())
        return qdest

    @staticmethod
    def peek(q,i):
        print(f'Stackelement {i} anschauen, WERT {q.queue[i]}')

    @staticmethod
    def show(q):
        for i in range(q.qsize()):
            print(f"{i:3d}tes Element {q.queue[i]:3d}")

    @staticmethod
    def main():
        zaehler_laenge = []
        q4dest = Queue()
        #q4 = Uebung.q_4_erstellen()
        uebung_instance = Uebung()
        #qReversed = uebung_instance.revers_queue(q4, q4dest, zaehler_laenge)
        #while not qReversed.empty():
         #   print(qReversed.get())

        #print(len(zaehler_laenge), zaehler_laenge)

        test = uebung_instance.LIFO()
        q4dest = LifoQueue()
        qtest = uebung_instance.revers_queue(test, q4dest, zaehler_laenge)
        qtest2 = LifoQueue()
        qtest2 = qtest
        while not qtest2.empty():
            print(qtest2.get())

if __name__ == "__main__":
    uebung = Uebung()
    uebung.main()