from threading import Thread
import time

class AsyncWrite(Thread):
    def __init__(self, text, out):
        Thread.__init__(self)
        self.text = text
        self.out = out

    def run(self):
        with open(self.out, 'a') as f:
            f.write(self.text+'\n')
        time.sleep(2)
        print (f'Finished Background file write to {self.out}')

def Main():
    message = input("Enter a string to store:")
    background = AsyncWrite (message, 'out.txt')
    background.start()
    print('The program can continue while it writes in another thread')
    print(f'100+400 = {100+400}')

    background.join()
    print('Waited until thread was complete')

if __name__ == '__main__':
    Main()