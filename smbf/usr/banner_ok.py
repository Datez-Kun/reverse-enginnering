# Filenames : 
# Python bytecode : 3.8
# Time succses decompiled Sat Sep 26 03:37:56 2020
# Selector <module> in line 1 file 
# Timestamp in code : 2020-06-27 04:07:18

from colorama import init, Fore, Back
C = '\x1b[94;m'
G = '\x1b[92;m'
r = '\x1b[0;m'
P = '\x1b[93;m'
init(autoreset=True)

def banner():
    print(f"\n      {C}╔═╗{r}  ┌┬┐  ┌┐   ┌─┐\n      {C}╚═╗{r}  │││  ├┴┐  ├┤\n      {C}╚═╝{r}  ┴ ┴  └─┘  └  V{G}1.2{r}dev\n {Back.LIGHTWHITE_EX + Fore.BLACK}  Simple multi bruteforce facebook  ")


def menu():
    print()
    print(f"  [ {C}1{r} ] From friendlist")
    print(f"  [ {C}2{r} ] From likes on post")
    print(f"  [ {C}3{r} ] By search name")
    print(f"  [ {C}4{r} ] From group (only takes 100 user)")
    print(f"  [ {C}5{r} ] From friend friendlist")
    print(f"  [ {C}6{r} ] From hashtag ")
    print(f"  [ {C}7{r} ] Re-check result")


