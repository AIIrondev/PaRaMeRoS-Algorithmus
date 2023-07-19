# importe der verschiedenen Unterbausteine (Spike Umwandler, 
# deep_learning(PPO), Ant_colony_algorithmus) + andere Importe
import Ant_colony_algorithmus

# Variables
output_1 = True
output_2 = True
output_3 = True
output_4 = True



# Def Area
def data_save():
   with open("protokol.fll", "a") as DONE:
       DONE.write(output_1, output_2, output_3, output_4)


def spike_umwandler():
    print("Spike Umwandler")
       
       
# define classes 
class call_lissen_Ki():
    print("Hello")
    def main():
        print("bye")

'''
class supervision_learning_Ki1():
    print("Hello2")
    def main():
        print("bye2")
'''    

class deep_learning_Ki():
    print("Hello3")
    def main():
        print("bye3")
    
'''    
class supervision_learning_Ki2():
    print("Hello4")
    def main():
        print("bye4")
'''

class logic():
    def call_lissen():
        call_lissen_Ki.main()
'''    def supervision_learning1():
        supervision_learning_Ki1.main()'''
    def deep_learning():
        deep_learning_Ki.main()
'''    def supervision_learning2():
        supervision_learning_Ki2.main()'''
