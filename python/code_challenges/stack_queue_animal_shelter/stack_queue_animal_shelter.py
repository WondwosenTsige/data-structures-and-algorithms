from code_challenges.stacks_and_queue.queue.queue import Queue

class AniamlShelter():
    def __init__(self):
        self.dogs = Queue()
        self.cats = Queue()

    def enqueue(self, animal):

            if animal == "dog":
                self.dogs.enqueue(animal)
            elif animal == "cat":
                self.cats.enqueue(animal)

            else:
                raise Exception("You can add only cats or dogs")

    def dequeue(self, pref):

        if pref == "dog":
            if self.dogs.front == None:
                raise Exception("Sorry! we do not have dogs for the time being")
            else:
                return self.dogs.dequeue()

        elif pref == "cat":
            if self.cats.front == None:
                raise Exception("Sorry! we do not have cats for the time being")
            else:
                return self.cats.dequeue()

        return None



