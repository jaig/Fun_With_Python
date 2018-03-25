# BY JAY GULRAJ
# 25/03/2018

from win10toast import ToastNotifier
import pandas as pd
import time
import random


toaster = ToastNotifier()


while True:
    f = pd.read_csv("Quotes.csv")
    tm1 = random.randint(1,10)
    time.sleep(tm1)
    ind = random.randint(1,f.shape[0])
    tm2= random.randint(1,10)
    toaster.show_toast(f['By'][ind-1],
                   f['Quote'][ind-1],
                   duration=5+tm2)