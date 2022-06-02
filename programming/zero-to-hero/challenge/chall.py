#!/usr/bin/env python3

from random import choice
from random import randint
from string import ascii_letters
from string import digits
from sys import exit
import graphlib
from time import time 

FLAG = "shellmates{T0POLOGICAL_$0RTING_FTW____!!!}"

charset = ascii_letters + digits
gen = lambda n : "".join(choice(charset) for i in range(n))

def make_depends(n):
    skills = [gen(10) for i in range(n)]
    depnds = {}
    for skill in skills :
        depnds[skill] = [sk for sk in set([choice(skills) for i in range(randint(0,2))]) if sk!=skill]
    return depnds,skills

def welcome():
    print('''You are a cybersecurity enthusiast looking to join the most 1337 team, "CyberErudites".

In order to do so, you need to gain some skills, but some of them require other prerequisites skills. That's why you decided to make a roadmap and order the skills you have to learn.

Rules : 
1- There are 90 phases.
2- All phases are independent.
3- At the end of the phase, all skills must be acquired.
4- The answer will be the skills separated by "-" : "skill1-skill2-skill3"
5- The path is not unique
6- If there is no possible path send "impossible"

Note : skills' names are generated randomly
''')

def pprint(dpnds):
    for skill in dpnds :
        print("To learn {} you must know : {}".format(skill, "-".join(sk for sk in dpnds[skill])))

class user:
    def __init__(self,goal):
        self.skills = []
        self.goal = goal
    
    def complete(self):
        if len(self.goal) != len(self.skills):
            return False
    
        return sorted(self.skills) == sorted(self.goal)

    def add(self,skill):
        self.skills.append(skill)


def main():
    welcome()
    for i in range(10,100):
        dpnds,skills = make_depends(i)
        pprint(dpnds)
        begin = time()
        path = input("Path -> ").strip()
        taken = time() - begin
        if taken > 2 :
            print("too slow")
            exit()
        if path == "impossible" :
            try : 
                tuple(graphlib.TopologicalSorter(dpnds).static_order())
                print("WRONG!")
                exit()
            except graphlib.CycleError : 
                continue
        u = user(skills)
        try : 
            path = path.split("-")
            for sk in path :
                if any(skill not in u.skills for skill in dpnds[sk]): 
                    print("WRONG PATH")
                    exit()   

                u.add(sk)
        except Exception as e:
            print("something went wrong")
            exit()
        if not u.complete():
            print("You didn't learn all the skills")
            exit(   )

    print(FLAG)

if __name__ == '__main__':
    main()